jQuery(document).ready(function ($) {
    let currentConversationId = null;

    // Start conversation
    $(document).on('click', '[data-broadgate-trigger]', function (e) {
        e.preventDefault();

        const $container = $(this).closest('.broadgate-ai-container');
        const $modal = $container.find('.broadgate-ai-modal');
        const $loading = $modal.find('.broadgate-ai-loading');
        const $iframeContainer = $modal.find('.broadgate-ai-iframe-container');
        const $iframe = $modal.find('.broadgate-ai-iframe');
        const $error = $modal.find('.broadgate-ai-error');

        // Show modal and loading state
        $modal.fadeIn(300);
        $loading.show();
        $iframeContainer.hide();
        $error.hide();

        // Create conversation via AJAX
        $.ajax({
            url: broadgateAI.ajaxUrl,
            type: 'POST',
            data: {
                action: 'broadgate_create_conversation',
                nonce: broadgateAI.nonce
            },
            success: function (response) {
                if (response.success) {
                    currentConversationId = response.data.conversation_id;

                    // Load iframe
                    $iframe.attr('src', response.data.conversation_url);

                    // Show iframe when loaded
                    $iframe.on('load', function () {
                        $loading.hide();
                        $iframeContainer.fadeIn(300);
                    });
                } else {
                    showError($error, response.data.message || 'Failed to start conversation');
                    $loading.hide();
                }
            },
            error: function (xhr, status, error) {
                showError($error, 'Network error. Please try again.');
                $loading.hide();
            }
        });
    });

    // Close modal
    $(document).on('click', '[data-broadgate-close]', function (e) {
        e.preventDefault();
        closeModal($(this).closest('.broadgate-ai-modal'));
    });

    // Close on outside click
    $(document).on('click', '.broadgate-ai-modal', function (e) {
        if ($(e.target).hasClass('broadgate-ai-modal')) {
            closeModal($(this));
        }
    });

    // Retry button
    $(document).on('click', '.broadgate-ai-retry', function (e) {
        e.preventDefault();
        const $modal = $(this).closest('.broadgate-ai-modal');
        $modal.find('[data-broadgate-trigger]').first().trigger('click');
    });

    // Close modal and end conversation
    function closeModal($modal) {
        $modal.fadeOut(300, function () {
            // Reset modal state
            $modal.find('.broadgate-ai-loading').hide();
            $modal.find('.broadgate-ai-iframe-container').hide();
            $modal.find('.broadgate-ai-error').hide();
            $modal.find('.broadgate-ai-iframe').attr('src', '');

            // End conversation if active
            if (currentConversationId) {
                endConversation(currentConversationId);
                currentConversationId = null;
            }
        });
    }

    // End conversation via AJAX
    function endConversation(conversationId) {
        $.ajax({
            url: broadgateAI.ajaxUrl,
            type: 'POST',
            data: {
                action: 'broadgate_end_conversation',
                nonce: broadgateAI.nonce,
                conversation_id: conversationId
            }
        });
    }

    // Show error message
    function showError($errorContainer, message) {
        $errorContainer.find('.error-message').text(message);
        $errorContainer.fadeIn(300);
    }

    // Close modal on ESC key
    $(document).on('keydown', function (e) {
        if (e.key === 'Escape') {
            $('.broadgate-ai-modal:visible').each(function () {
                closeModal($(this));
            });
        }
    });
});
