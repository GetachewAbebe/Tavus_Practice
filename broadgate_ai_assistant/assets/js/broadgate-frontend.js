jQuery(document).ready(function ($) {
    let call = null;
    let isMuted = false;

    function cfg() {
        return (window.broadgateAjax && window.broadgateAjax.ajaxurl) ? window.broadgateAjax :
               (window.broadgateAI && window.broadgateAI.ajaxurl) ? window.broadgateAI : null;
    }

    function setInCallState(inCall) {
        if (inCall) {
            $('#broadgate-ai-card').addClass('broadgate-ai--in-call');
            $('#broadgate-ai-close').attr('aria-disabled', 'true').prop('disabled', true);
        } else {
            $('#broadgate-ai-card').removeClass('broadgate-ai--in-call');
            $('#broadgate-ai-close').removeAttr('aria-disabled').prop('disabled', false);
        }
    }

    function showLoading() {
        $('#broadgate-ai-error').hide().text('');
        $('#broadgate-ai-loading').show();
        $('#broadgate-ai-talk-now').hide().prop('disabled', true).css('opacity', 0.95);
    }

    function hideLoading() {
        $('#broadgate-ai-loading').hide();
        $('#broadgate-ai-talk-now').prop('disabled', false).css('opacity', 1);
    }

    function showError(msg) {
        hideLoading();
        $('#broadgate-ai-error').show().text(msg || 'Something went wrong.');
        $('#broadgate-ai-talk-now').show().prop('disabled', false);
        setInCallState(false);
    }

    function getIdleVideoEl() {
        return document.getElementById('broadgate-ai-idle-video');
    }

    function setIdleVideoSrc(url) {
        const v = getIdleVideoEl();
        if (!v || !url) return;

        // Replace the <source> src
        let source = v.querySelector('source');
        if (!source) {
            source = document.createElement('source');
            source.type = 'video/mp4';
            v.appendChild(source);
        }

        source.src = url;
        v.load();

        // Always muted for autoplay
        v.muted = true;
        v.setAttribute('muted', 'muted');
        v.setAttribute('playsinline', 'playsinline');

        const p = v.play();
        if (p && typeof p.catch === 'function') p.catch(() => {});
    }

    function playIdleVideoFallback() {
        const v = getIdleVideoEl();
        if (!v) return;
        const fallback = v.getAttribute('data-fallback-src');
        if (fallback) setIdleVideoSrc(fallback);
    }

    function fetchTavusAvatarOnLoad() {
        const c = cfg();
        if (!c) {
            playIdleVideoFallback();
            return;
        }

        $.ajax({
            url: c.ajaxurl,
            type: 'POST',
            dataType: 'json',
            data: { action: 'broadgate_get_avatar', nonce: c.nonce },
            success: function (resp) {
                // Expect: { success:true, data:{ avatar_url:"..." } }
                if (resp && resp.success === true && resp.data && resp.data.avatar_url) {
                    setIdleVideoSrc(resp.data.avatar_url);
                } else {
                    playIdleVideoFallback();
                }
            },
            error: function () {
                playIdleVideoFallback();
            }
        });
    }

    function resetUI() {
        hideLoading();
        $('#broadgate-ai-error').hide().text('');

        $('#broadgate-ai-controls').hide();
        $('#broadgate-ai-remote-wrap').hide();

        $('#broadgate-ai-idle').show();

        // keep idle looping
        const v = getIdleVideoEl();
        if (v) {
            v.muted = true;
            const p = v.play();
            if (p && typeof p.catch === 'function') p.catch(() => {});
        }

        setInCallState(false);
        $('#broadgate-ai-talk-now').show().prop('disabled', false).css('opacity', 1);

        isMuted = false;
        $('#broadgate-ai-mute').text('Mute');
    }

    async function hangup() {
        try {
            if (call) {
                await call.leave();
                call.destroy();
            }
        } catch (e) {}
        call = null;
        resetUI();
    }

    function extractUrl(resp) {
        const top = (resp && resp.data) ? resp.data : (resp || {});
        const payload = top.raw || top.data || top;
        return payload.conversation_url || payload.embed_url || payload.iframe_url || payload.url || null;
    }

    function attachRemoteTrack(track) {
        const videoEl = document.getElementById('broadgate-ai-remote-video');
        if (!videoEl) return;
        const stream = new MediaStream([track]);
        videoEl.srcObject = stream;
        videoEl.play().catch(() => {});
    }

    async function startAudioOnlyCall(roomUrl) {
        if (!window.Daily || !window.Daily.createCallObject) {
            showError("Daily Video API not loaded. (Daily.createCallObject missing)");
            return;
        }

        await hangup();

        setInCallState(true);
        showLoading();

        call = window.Daily.createCallObject({
            videoSource: false, // user audio-only
            audioSource: true
        });

        call.on('track-started', (ev) => {
            if (ev && ev.track && ev.track.kind === 'video' && ev.participant && !ev.participant.local) {
                $('#broadgate-ai-idle').hide();
                $('#broadgate-ai-remote-wrap').show();
                attachRemoteTrack(ev.track);
            }
        });

        call.on('joined-meeting', () => {
            hideLoading();
            $('#broadgate-ai-controls').show();
            $('#broadgate-ai-talk-now').hide();
            setInCallState(true);
        });

        call.on('error', (e) => {
            console.error("Daily error:", e);
            showError("Could not start the conversation. Please try again.");
        });

        call.on('left-meeting', () => {
            hangup();
        });

        try {
            await call.join({ url: roomUrl });
            try { await call.setLocalVideo(false); } catch (e) {}
        } catch (e) {
            console.error("Join failed:", e);
            showError("Join failed. Please allow microphone permission and try again.");
        }
    }

    // ✅ Fetch Tavus avatar video on page load
    fetchTavusAvatarOnLoad();

    // Talk Now
    $(document).on('click', '#broadgate-ai-talk-now', function (e) {
        e.preventDefault();

        const c = cfg();
        if (!c) {
            showError("Plugin config missing (broadgateAjax/broadgateAI not found).");
            return;
        }

        setInCallState(true);
        showLoading();

        $.ajax({
            url: c.ajaxurl,
            type: 'POST',
            dataType: 'json',
            data: { action: 'broadgate_create_conversation', nonce: c.nonce },
            success: function (resp) {
                if (!resp || resp.success !== true) {
                    const msg = (resp && resp.data && resp.data.message) ? resp.data.message : "Failed to start conversation.";
                    showError(msg);
                    return;
                }

                const url = extractUrl(resp);
                if (!url) {
                    showError("No conversation URL returned by API.");
                    return;
                }

                startAudioOnlyCall(url);
            },
            error: function (xhr) {
                console.error("AJAX error:", xhr);
                let msg = "Request failed.";
                if (xhr && xhr.responseJSON && xhr.responseJSON.data && xhr.responseJSON.data.message) {
                    msg = xhr.responseJSON.data.message;
                }
                showError(msg);
            }
        });
    });

    // Mute
    $(document).on('click', '#broadgate-ai-mute', async function () {
        if (!call) return;
        try {
            isMuted = !isMuted;
            await call.setLocalAudio(!isMuted);
            $('#broadgate-ai-mute').text(isMuted ? 'Unmute' : 'Mute');
        } catch (e) { console.error(e); }
    });

    // End
    $(document).on('click', '#broadgate-ai-hangup', function () {
        hangup();
    });

    // Close (only when not in call)
    $(document).on('click', '#broadgate-ai-close', function (e) {
        e.preventDefault();
        if ($('#broadgate-ai-card').hasClass('broadgate-ai--in-call')) return;
        hangup();
        $('#broadgate-ai-container').hide();
    });

    resetUI();
});
