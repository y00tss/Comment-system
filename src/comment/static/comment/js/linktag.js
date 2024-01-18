function addLinkTag(textareaId) {
    var textarea = document.getElementById(textareaId);
    var start = textarea.selectionStart;
    var end = textarea.selectionEnd;
    var selectedText = textarea.value.substring(start, end);

    var link = prompt('Enter the URL for the link:', '');
    if (link === null) {
        return;  // Пользователь отменил ввод URL
    }

    var displayText = prompt('Enter the text to display:', '');
    if (displayText === null) {
        return;  // Пользователь отменил ввод текста
    }

    var openingTag = '<a href="' + link + '" target="_blank">' + displayText + '</a>';
    var newText = textarea.value.substring(0, start) + openingTag + textarea.value.substring(end);
    textarea.value = newText;
}