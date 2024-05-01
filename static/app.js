document.addEventListener('DOMContentLoaded', function() {
    fetchGames();

    // Event listener for filter submission
    document.getElementById('filterForm').addEventListener('submit', function(event) {
        event.preventDefault();
        fetchFilteredGames();
    });
});

// Fetch and display all games
function fetchGames() {
    fetch('http://localhost:8000/games/')
        .then(response => response.json())
        .then(data => displayGames(data, 'listView'))
        .catch(error => console.error('Error fetching games:', error));
}

// Fetch and display filtered games
function fetchFilteredGames() {
    // Implement fetching based on filter criteria
    // Placeholder function call to simulate
    console.log('Filter function not yet implemented');
}

// Display games in a specified element
function displayGames(games, elementId) {
    const tableBody = document.getElementById(elementId).querySelector('tbody');
    tableBody.innerHTML = ''; // Clear existing entries
    games.forEach(game => {
        const row = tableBody.insertRow();
        row.innerHTML = `
            <td>${game.game_title}</td>
            <td>${game.system}</td>
            <td>${game.year_published}</td>
            <td>${game.genre}</td>
            <td>${game.time_vibe}</td>
        `;
    });
}

// More functionality like handling modal pop-up for detailed views can be added here
