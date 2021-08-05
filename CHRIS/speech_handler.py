# -*- coding: utf-8 -*-
'''
Author: David J. Morfe
Application Name: Speech Handler for C.H.R.I.S.
Functionality Purpose: Intake and process speech to recognize requested action
'''


import speech_recognition as sr
import time, re, os
from .keys import CWD, api_key
os.chdir(CWD)


class SpeechHandler:
    '''This class instantiates the connector software to interface with other modules'''

    RECORD = sr.Recognizer() #Audio Record Variable
    MIC = sr.Microphone() #Microphone Variable
    API_KEY = api_key()

    def __init__(self):
        self.pat_lib = ["(java|ava|lava|guava|kaaba)"]

    #Return the intended command
    def cmd_listen(self, file: str=None):
        ret = None
        try:
            print("A moment of silence, please...")
            with self.MIC as source:self.RECORD.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(self.RECORD.energy_threshold))
            print("Say a command!")
            with self.MIC as source: audio = self.RECORD.listen(source, timeout=2, phrase_time_limit=8,)
            try:
                # recognize speech using Google Speech Recognition
                ret = self.RECORD.recognize_google(audio, key=self.API_KEY, language="en-US").lower()
                print(f"You said {ret}")
                if re.search(fr"{self.pat_lib[0]}", ret):
                    ret = "java"
                elif re.search(fr"{self.pat_lib[0]}", ret):
                    ret = "pull"
                elif re.search(fr"{self.pat_lib[0]}", ret):
                    ret = "get"
            except sr.UnknownValueError:
                print("UnknownValueError: Speech is unintelligible")
            except sr.WaitTimeoutError:
                print("WaitTimeoutError: Took to long to speak")
        except KeyboardInterrupt:
            pass
        if file:
            with open(re.sub(r"\..+", '', file) + ".txt", 'a') as f:
                f.write(ret)
        return ret
