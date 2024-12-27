document.getElementById("moodForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const moodInput = document.getElementById("mood").value.toLowerCase();
    const recommendationsDiv = document.getElementById("recommendations");

    if (!moodInput) {
        recommendationsDiv.innerHTML = "<p style='color: red;'>Please describe your mood!</p>";
        return;
    }

    let recommendations;
    if (moodInput.includes("happy") || moodInput.includes("joy")) {
        recommendations = ["Happy - Pharrell Williams", "Dynamite - BTS", "Levitating - Dua Lipa"];
    } else if (moodInput.includes("sad") || moodInput.includes("down")) {
        recommendations = ["Someone Like You - Adele", "Drivers License - Olivia Rodrigo", "Fix You - Coldplay"];
    } else if (moodInput.includes("relaxed") || moodInput.includes("calm")) {
        recommendations = ["Peaches - Justin Bieber", "Weightless - Marconi Union", "Sunrise - Norah Jones"];
    } else if (moodInput.includes("energetic") || moodInput.includes("excited")) {
        recommendations = ["Don't Stop Me Now - Queen", "Eye of the Tiger - Survivor", "Party Rock Anthem - LMFAO"];
    } else {
        recommendations = ["Sorry, we couldn't match your mood. Try 'happy', 'sad', 'relaxed', or 'energetic'."];
    }

    recommendationsDiv.innerHTML = `<h3>🎶 Recommended Songs:</h3><ul>${recommendations.map(song => `<li>${song}</li>`).join('')}</ul>`;
});

