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

    RECORD = sr.Recognizer() # Audio Record Variable
    MIC = sr.Microphone() # Microphone Variable
    API_KEY = api_key()

    def __init__(self, wait: int=8):
        self.ret = self.file = None; self.wait = wait
        self.stop_listener = None
        self.pat_lib = {"triger": "(hey chris|hay kris|ay cris|chris|kris|oi chris)",
                        "java": "(java|ava|lava|guava|kaaba)",
                        "v10": "(pull|v10|v|vee|ten)",
                        "get": "(dot|go to|search|google|com|org|net|\.)"}

    # Return value from callback
    def get_value(self) -> str:
        return self.ret

    # Call back function for background listener
    def callback(self, recognizer, audio):
        try:
            value = recognizer.recognize_google(
                audio, key=self.API_KEY, language="en-US").lower()
            self.ret = value
            if self.file:
                with open(re.sub(r"\..+$", '', self.file) + ".txt", 'a') as f:
                    f.write(self.ret + '\n')
            print("You said " + value)  # received audio data, now need to recognize it
        except sr.UnknownValueError:
            print("UnknownValueError: Speech is unintelligible")
        except sr.RequestError:
            print("RequestError: Could not requests results from API")

    # Listen for specified length of time
    def cmd_listen(self, file: str=None) -> str:
        try:
            print("A moment of silence, please...")
            with self.MIC as source:self.RECORD.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(self.RECORD.energy_threshold))
            print("Say a command!")

            with self.MIC as source:
                audio = self.RECORD.listen(source, timeout=2, phrase_time_limit=self.wait)
            try:
                # recognize speech using Google Speech Recognition API
                self.ret = self.RECORD.recognize_google(audio, key=self.API_KEY, language="en-US").lower()
                print(f"You said {self.ret}")
                if re.search(fr"{self.pat_lib['java']}", self.ret):
                    self.ret = "java"
                elif re.search(fr"{self.pat_lib['v10']}", self.ret):
                    self.ret = "pull"
                elif re.search(fr"{self.pat_lib['get']}", self.ret):
                    self.ret = "get"
            except sr.UnknownValueError:
                print("UnknownValueError: Speech is unintelligible")
            except sr.WaitTimeoutError:
                print("WaitTimeoutError: Took to long to speak")
        except KeyboardInterrupt:
            pass
        if file:
            with open(re.sub(r"\..+$", '', file) + ".txt", 'a') as f:
                f.write(self.ret + '\n')
        return self.ret

    # Listen in background for specified length of time
    def cmd_listen_background(self, file: str=None) -> str:
        try:
            self.file = file
            print("A moment of silence, please...")
            with self.MIC as source:self.RECORD.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(self.RECORD.energy_threshold))
            print("Say a command!")
            self.stop_listener = self.RECORD.listen_in_background(self.MIC, self.callback)
##            for i in range(self.wait): time.sleep(1)
##            self.stop_listener(wait_for_stop=False)
        except KeyboardInterrupt:
            pass
        return self.stop_listener
