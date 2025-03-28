import pyttsx3
import speech_recognition as sr


class AI():
    __name = ""
    __skill = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',voices[4].id)
        name = voices[4].name
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if name is not None:
            self.__name = name

        print("Listening")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        sentence = "Hello, my name is" + self.__name
        self.__name = value
        self.engine.say(sentence)
        self.engine.runAndWait()

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

    def listen(self):
        print("Say something")
        with self.m as source:
            audio = self.r.listen(source)
        print("Got it")
        try:
            phrase = self.r.recognize_google(audio, show_all=True, language="en")
            sentence = "Got it, you said" + phrase
            self.engine.say(sentence)
            self.engine.runAndWait()
        except:
            print("Sorry, didn't catch that")
            self.engine.say("Sorry, didn't catch that")
            self.engine.runAndWait()
        print("You said", phrase)
        return phrase