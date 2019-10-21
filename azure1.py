import json
import requests

# Azure Portal > Text Analytics API Resource > Keys
ACCESS_KEY = 'c82709acdf2d417bbf27203bb21f72d7'
# Text Analytics API Base URL
URL = 'https://westcentralus.api.cognitive.microsoft.com/text/analytics/'

def get_insights(api, documents):
    """
    Get insights using Microsoft Cognitive Service - Text Analytics
    """
    # 1. Set a Request Header to include the Access Key
    headers = {'Ocp-Apim-Subscription-Key': ACCESS_KEY}
    # 2. Set the HTTP endpoint
    url = URL + api
    # 3. Create a POST request with the JSON documents
    request = requests.post(url, headers=headers, data=json.dumps(documents))
    # 4. Load Response
    response = json.loads(request.content)

    print('------------------------------------')
    print('API: ' + api)
    for document in response['documents']:
        print(document)

def language_detection():
    """
    The API returns the detected language and a numeric score between 0 and 1 indicating certainty.
    """
    documents = {
        'documents': [
            {"id":"1", "text":"Le renard brun rapide saute par-dessus le chien paresseux" },
            {"id":"2", "text":"敏捷的棕色狐狸跳过了懒狗" },
            {"id":"3", "text":"The quick brown fox jumps over the lazy dog" }
        ]
    }
    get_insights('languages', documents)

def key_phrases():
    """
    The API returns a list of strings denoting the key talking points in the input text.
    """
    documents = {
        'documents': [
            { "id":"1", "language":"en", "text":"Apple's plan to bring home hundreds of billions of dollars in overseas cash has triggered a guessing game on Wall Street about what it might do with all that money. The tech giant could find itself with about $200 billion to spend, after taxes, if it repatriates all its overseas holdings into the U.S." },
            { "id":"2", "language":"en", "text":"Tableau Software is revamping a core part of its technology to analyse data faster, a move intended to keep up with its customers' increasing big-data needs. The Seattle company, which makes software to visualise analytics, is introducing its so-called Hyper engine in a software update Jan 17. The technology is designed to make the data-visualisation process five times faster, meaning businesses can input millions of data points and see results in seconds." },
            { "id":"3", "language":"en", "text":"Reviews of the Tesla Model 3 praise the car as a futuristic, mold-breaking car that may be the best electric vehicle at its price point. But that doesn't mean it's perfect. Overall, Tesla's first attempt at a less expensive car than their higher-end S and X models has received strong acclaim for its smooth, quiet ride, uniquely minimalist interior and dashboard, and body design." }
        ]
    }
    get_insights('keyPhrases', documents)

def sentiment():
    """
    The API returns a numeric score between 0 and 1. Scores close to 1 indicate positive sentiment, and scores close to 0 indicate negative sentiment.
    """
    documents = {
        'documents': [
            { "id":"1", "language":"en", "text":"What a great way to run the public transport in a city ! Loved the regular frequency, clear mapping and the accessible stops. Well done Melbourne !" },
            { "id":"2", "language":"en", "text":"Boarding at Spring st, near Parliament station - initially very crowded as the previous tram broke down, the journey went half way around the city - when at the corner of Flinders and Spencer St we were ll advised to disembark - as it was the end of the drivers shift - and there was no replacement driver - over 100 people were left stranded - truly a poor example of Melbourn hospitality. - Many tourists not knowing how to get back to there original destination." },
            { "id":"3", "language":"en", "text":"What a terrific way to get around the Melbourne CBD. You can hope on any tram within the CBD area and it is free. The Number 35 tram does a complete circuit of the CBD with commentary about Melbourne landmarks but it can get very crowded. Make sure you use it." },
        ]
    }
    get_insights('sentiment', documents)

if __name__ == '__main__':
    language_detection()
    key_phrases()
    sentiment()