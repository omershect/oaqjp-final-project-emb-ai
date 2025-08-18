
#The File contains the Emotion Detector function that Analyze text 
import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_json = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=input_json, headers=header)
    
    if response.status_code == 200:
        json_response = response.json()   # better than json.loads(response.text)
        
        # drill into the nested structure
        emotions_dict = json_response["emotionPredictions"][0]["emotion"]
        
        # find the dominant emotion (max score)
        dominant = max(emotions_dict, key=emotions_dict.get)
        
        emotions = {
            'anger': emotions_dict.get('anger'),
            'disgust': emotions_dict.get('disgust'),
            'fear': emotions_dict.get('fear'),
            'joy': emotions_dict.get('joy'),
            'sadness': emotions_dict.get('sadness'),
            'dominant_emotion': dominant
        }
        
        return emotions
    else:
        return {"error": f"Request failed with status {response.status_code}"}

