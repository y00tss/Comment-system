// Karma voting
function voteKarma(commentId, action) {
    fetch(`/vote_karma/${commentId}/${action}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById(`karma_${commentId}`).innerText = `Karma: ${data.karma}`;
        })
        .catch(error => console.error('Error:', error));
}
