                                                                                   
import torch
import numpy as np
from transformers import pipeline

class EmotionsSingletonClass:
    _instance = None  # Private variable to store the instance

    def __init__(self):
        # Private constructor to prevent direct instantiation
        if self._instance is not None:
            raise Exception("This class is a singleton and cannot be instantiated directly.")
        self.data = "Singleton Data"
        self.T5 = pipeline("text2text-generation", model="google/flan-t5-base",device_map="auto")
        self.roberta = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions",top_k=None,device_map="auto")
        self.Twitter = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-irony",top_k=None,device_map="auto")
        self.twitterSent = pipeline("text-classification",model="cardiffnlp/twitter-roberta-base-sentiment-latest",top_k=None,device_map="auto")

    @classmethod
    def get_instance(cls):
        # Static method to access the instance
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def emotions(self,message):
        
        result = self.roberta(message)
        response = {}
        for i in result[0]:
            response[i['label']] = round(float(i['score']),3)
        return response
    def irony(self,message):        
        result = self.Twitter(message)
        print(result,flush=True)
        response = {}
        for i in result[0]:
            response[i['label']] = round(float(i['score']),3) 
        return response
    def sentiment(self,message):
        result = self.twitterSent(message)
        response = {}
        print(result,flush=True)
        for i in result[0]:
            response[i['label']] = round(float(i['score']),3)   
        return response
    def tryBot(self,message):
        resp = self.T5(message)
        return {'message':resp[0]['generated_text']}
    
            

