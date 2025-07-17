from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    dominant_emotion = response['dominant_emotion']

    # Check if the label is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        #return "The given text has been identified as a {} of {}.".format(dominant_emotion.split('_')[1], dominant_emotion) 
        return dominant_emotion  

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO
    return render_template('index.html')    

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000 '''
    app.run(host="0.0.0.0", port=5000)    
