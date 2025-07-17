import requests
import json

"""
cli run instructions
python3
from emotion_detection import emotion_detector
emotion_detector("I love this new technology")

cli package import run instructions
python3
from EmotionDetection.emotion_detection import emotion_detector
emotion_detector("I am so happy I am doing this")
emotion_detector("I hate working long hours")
"""

def emotion_detector(text_to_analyse):
    # Define the URL for the emotion_detector API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    
    #return response.text  
    

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    #return formatted_response.keys()
    #emotions = formatted_response['emotionPredictions'][0]['emotion']
    #max_emotion = max(emotions, key=emotions.get)
    #return max_emotion

    # If the response status code is 200, extract from the response
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['disgust']
        joy_score = emotions['disgust']
        sadness_score = emotions['disgust']
        dominant_emotion = max(emotions, key=emotions.get)
    # If the response status code is 500, set all to None
    elif response.status_code == 500:
        emotions = None
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    # If the response status code is 400, set all to None
    elif response.status_code == 400:
        emotions = None
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # Return the label and score in a dictionary
    #return {'label': label, 'score': score}
    return {'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }
