function toggleReplyForm(commentId) {
    var formId = 'reply-form-' + commentId;
    var form = document.getElementById(formId);

    if (form.style.display === 'none') {
        form.style.display = 'block';
    } else {
        form.style.display = 'none';
    }
}