from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle mood-based song recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json  # Get the JSON data from the frontend
    user_mood = data.get('mood', '').lower()

    # Predefined mood-based song recommendations
    if 'happy' in user_mood or 'joy' in user_mood:
        recommendations = [
            "Happy - Pharrell Williams", "Dynamite - BTS", "Levitating - Dua Lipa",
            "Gallan Goodiyan - Dil Dhadakne Do", "Dance Monkey - Tones and I",
            "Abhi Toh Party Shuru Hui Hai - Badshah"
        ]
    elif 'sad' in user_mood or 'down' in user_mood:
        recommendations = [
            "Someone Like You - Adele", "Drivers License - Olivia Rodrigo", "Fix You - Coldplay",
            "Agar Tum Saath Ho - Tamasha", "Tadap Tadap - Hum Dil De Chuke Sanam",
            "Channa Mereya - Ae Dil Hai Mushkil"
        ]
    elif 'relaxed' in user_mood or 'calm' in user_mood:
        recommendations = [
            "Peaches - Justin Bieber", "Weightless - Marconi Union", "Sunrise - Norah Jones",
            "Tum Mile - Tum Mile", "Kun Faya Kun - Rockstar", "Phir Le Aya Dil - Barfi"
        ]
    elif 'energetic' in user_mood or 'excited' in user_mood:
        recommendations = [
            "Don't Stop Me Now - Queen", "Eye of the Tiger - Survivor", "Party Rock Anthem - LMFAO",
            "Zinda - Bhaag Milkha Bhaag", "Badtameez Dil - Yeh Jawaani Hai Deewani",
            "Malhari - Bajirao Mastani"
        ]
    else:
        recommendations = ["Sorry, we couldn't match your mood. Try 'happy', 'sad', 'relaxed', or 'energetic'."]

    # Return the recommendations as a JSON response
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)


