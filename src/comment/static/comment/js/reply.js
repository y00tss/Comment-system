// This file is used to toggle the reply form for each comment
function myFunction(commentId) {
    var formId = 'reply-form-' + commentId;
    var form = document.getElementById(formId);

    if (form.style.display === 'none') {
        form.style.display = 'block';
    } else {
        form.style.display = 'none';
    }
}