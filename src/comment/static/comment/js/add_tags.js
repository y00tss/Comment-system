function addTag(openingTag, closingTag, textareaId) {
    var textarea = document.getElementById(textareaId);
    var start = textarea.selectionStart;
    var end = textarea.selectionEnd;
    var selectedText = textarea.value.substring(start, end);
    var newText = textarea.value.substring(0, start) + openingTag + selectedText + closingTag + textarea.value.substring(end);
    textarea.value = newText;
}