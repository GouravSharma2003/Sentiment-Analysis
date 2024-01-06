# This paralleldots module, is NLP and ML platform that provides various APIs,
#Like : sentimental analysis, Emotion Analysis, Entity Recognition

import paralleldots
class Api:
    paralleldots.set_api_key('baLnjigzhEcLZdq8tmbQpaLPfB1Jrn2HmspltfOxnxI')
    def sentimentAnalysis(self,text):
        response=paralleldots.sentiment(text)
        print(response)
        return response


    def emotion_analysis(self,text):
        response=paralleldots.emotion(text)
        print(response)
        return response


a=Api()
#print(a.sentiment_analysis('She is good girl'))

