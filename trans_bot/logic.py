# Задание №3 
import requests 
from collections import defaultdict 
from translate import Translator 
 
# Задание №5 
questions = {'как тебя зовут?' : "Я супер-крутой-бот и мое предназначение помогать тебе!", 
             "сколько тебе лет?" : "Это слишком философский вопрос"} 
 
class TextAnalysis():    
     
    # Задание №1 
 
    memory = defaultdict(list) 
 
    def __init__(self, text, owner): 
 
        # Задание №2 
        TextAnalysis.memory[owner].append(self) 
        self.text = text 
        self.translation = self.__translate(self.text, "ru", "en") 
        self.response = self.__get_response() 
 
        # Задание №6 
    def __get_response(self): 
        if self.text.lower() in questions: 
            return questions[self.text.lower()] 
        else: 
            return self.__deep_pavlov_answer() 
 
    def __translate(self, text, from_lang, to_lang): 
        try: 
            # Задание №4 
            translator = Translator(from_lang=from_lang, to_lang=to_lang) 
            translation = translator.translate(text) 
            return translation 
        except: 
            return "Перевод не удался" 
 
    def __deep_pavlov_answer(self): 
        try: 
            API_URL = "https://7038.deeppavlov.ai/model" 
            data = {"question_raw": [ self.translation ]} 
            res = requests.post(API_URL, json=data).json() 
            res = res[0][0] 
        except: 
            res = "I don't know how to help" 
        return res