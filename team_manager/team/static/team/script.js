document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/players/')
        .then(response => response.json())
        .then(data => {
            const playerList = document.getElementById('player-list');
            data.forEach(player => {
                const listItem = document.createElement('li');
                listItem.textContent = `${player.first_name} ${player.last_name}`;
                playerList.appendChild(listItem);
            });
        });
});