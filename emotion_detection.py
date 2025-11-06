import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body =  { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers = headers, json=body)
    json_respons = json.loads(response.text)

    anger_score = json_respons["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = json_respons["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = json_respons["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = json_respons["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = json_respons["emotionPredictions"][0]["emotion"]["sadness"]

    dominant_emotion_score = max(anger_score,disgust_score,fear_score,joy_score,sadness_score)

    if dominant_emotion_score == anger_score:
        dominant_emotion = "anger"
    elif dominant_emotion_score == disgust_score:
        dominant_emotion = "disgust"
    elif dominant_emotion_score == fear_score:
        dominant_emotion = "fear"
    elif dominant_emotion_score == joy_score:
        dominant_emotion = "joy"
    elif dominant_emotion_score == sadness_score:
        dominant_emotion = "sadness"

    json_result = { 'anger': anger_score,
                    'disgust': disgust_score,
                    'fear': fear_score,
                    'joy': joy_score,
                    'sadness': sadness_score,
                    'dominant_emotion': dominant_emotion
                }
    return json_result
