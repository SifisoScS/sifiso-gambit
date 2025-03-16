// Fetch and update game state
function updateGameState() {
    fetch('/game/state')
    .then(response => response.json())
    .then(data => {
        const aiPlayersDiv = document.getElementById('ai-players');
        const humanHandDiv = document.getElementById('human-hand');
        const logMessages = document.getElementById('log-messages');

        aiPlayersDiv.innerHTML = "";
        humanHandDiv.innerHTML = "";
        logMessages.innerHTML = "";

        // Update AI player hands
        data.players.forEach(player => {
            const playerDiv = document.createElement('div');
            playerDiv.innerHTML = `<strong>${player.name}</strong>: ${player.hand.join(', ')}`;
            if (player.name === "Human") {
                humanHandDiv.appendChild(playerDiv);
            } else {
                aiPlayersDiv.appendChild(playerDiv);
            }
        });

        // Show rule shifts
        if (data.rules_active.length > 0) {
            const ruleMessage = document.createElement('li');
            ruleMessage.textContent = `🔥 Rule Shift: ${data.rules_active.join(', ')}`;
            logMessages.appendChild(ruleMessage);
        }
    });
}

function fetchGameState() {
    fetch("/game/state") // Ensure this route is correct
        .then(response => response.json())
        .then(data => updateUI(data))
        .catch(error => console.error("Error fetching game state:", error));
}

function updateUI(data) {
    // Update AI Players' hands
    let aiPlayers = document.getElementById("ai-players");
    aiPlayers.innerHTML = ""; // Clear previous data
    data.players.forEach(player => {
        if (player.name !== "Human") {
            aiPlayers.innerHTML += `<p><strong>${player.name}:</strong> ${player.hand.join(", ")}</p>`;
        }
    });

    // Update Human Player's hand
    let humanHand = document.getElementById("human-hand");
    let human = data.players.find(p => p.name === "Human");
    humanHand.innerHTML = `<p><strong>Human:</strong> ${human.hand.join(", ")}</p>`;

    // Update Game Log (if any new events)
    let gameLog = document.getElementById("game-log");
    if (data.rules_active.length > 0) {
        gameLog.innerHTML += `<p>🔥 Active Rules: ${data.rules_active.join(", ")}</p>`;
    }
}

// Fetch game state on page load
window.onload = fetchGameState;

// Play a round
function playRound() {
    fetch('/game/play', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        updateGameState();
        alert(data.message + " 🏆 Winner: " + data.winner);
    });
}

// Swap a card (for now, just refreshes)
function swapCard() {
    alert("Swapping card... (Feature coming soon)");
}

// View Rules
function viewRules() {
    alert("Rule Shifts: AI may change rules mid-game! Keep adapting!");
}

function updateGameLog(message, type="info") {
    let log = document.getElementById("game-log");
    let newEntry = document.createElement("p");

    if (type === "success") {
        newEntry.style.color = "green";
        newEntry.innerHTML = "✅ " + message;
    } else if (type === "error") {
        newEntry.style.color = "red";
        newEntry.innerHTML = "❌ " + message;
    } else {
        newEntry.style.color = "black";
        newEntry.innerHTML = "⚡ " + message;
    }

    log.appendChild(newEntry);
    log.scrollTop = log.scrollHeight; // Auto-scroll
}

// Update the game state every 3 seconds
setInterval(updateGameState, 3000);

// Initial load
updateGameState();
