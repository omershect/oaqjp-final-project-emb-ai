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
    Returns a plain text response with either emotion scores or an error.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    status = response.get("status")
    print("ststus is:",status)

    #  Case 1: Success
    if status == 200:
        anger = response.get('anger')
        disgust = response.get('disgust')
        fear = response.get('fear')
        joy = response.get('joy')
        sadness = response.get('sadness')
        dominant_emotion = response.get('dominant_emotion')

        return (
            f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy}, 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}."
        )


  

    #  Case 2: Bad input (400)
    elif status == 400 :
        return "Invalid text! Please try again!"

    #  Case 3: Other errors
    else :
        return f"Unexpected error occurred ({status})."


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
