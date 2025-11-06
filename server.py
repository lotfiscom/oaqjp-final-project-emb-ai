"""
This module re presents the main flask server entry 
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Final Project")

@app.route("/")
def home():
    """
    This is the main entry for the application
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def get_emotion():
    """
    This is the emotion detector service
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_result = emotion_detector(text_to_analyze)
    if emotion_result["dominant_emotion"] is None:
        result = "Invalid text! Please try again!."
    else:
        result = "For the given statement, the system response is 'anger': " + \
        str(emotion_result["anger"]) + ", 'disgust': " + str(emotion_result["disgust"]) + \
         ", 'fear': " + str(emotion_result["fear"]) + ", 'joy': " + str(emotion_result["joy"]) + \
         " and 'sadness': " + str(emotion_result["sadness"]) + ". The dominant emotion is " + \
         emotion_result["dominant_emotion"] + "."
    return result


if __name__ == '__main__':
    app.run(debug=False, port=5000)
