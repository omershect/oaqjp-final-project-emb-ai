# server.py
# Entry point for the Emotion Detector web server.
# Provides API endpoints to analyze emotions from text input.

from flask import Flask, render_template, request
from emotion_detection import emotion_detector  

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    API endpoint: Analyze the text provided in the query parameter 'textToAnalyze'.
    Returns detected emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze:
        return "Error: Please provide text to analyze using the 'textToAnalyze' parameter.", 400

    response = emotion_detector(text_to_analyze)

    # Extract results
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid text! Please try again.", 400

    return (
        f"For the given statement, the system detected "
        f"anger: {anger}, disgust: {disgust}, fear: {fear}, "
        f"joy: {joy}, sadness: {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the main index page (index.html).
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask server on host 0.0.0.0:5000 for external access in Watson/Cloud IDE.
    app.run(host="0.0.0.0", port=5000)
