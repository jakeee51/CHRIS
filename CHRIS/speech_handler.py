# -*- coding: utf-8 -*-
'''
Author: David J. Morfe
Application Name: Speech Handler for C.H.R.I.S.
Functionality Purpose: Intake and process speech to recognize requested action
'''


import speech_recognition as sr
import time, re, os
from .keys import CWD, api_key


API_KEY = api_key()
os.chdir(CWD)


class SpeechHandler:
    '''This class instantiates the connector software to interface with other modules'''

    RECORD = sr.Recognizer() # Audio Record Variable
    MIC = sr.Microphone() # Microphone Variable
    API_KEY = API_KEY

    def __init__(self, wait: int=8):
        self.ret = self.file = None; self.wait = wait
        self.stop_listener = None
        self.expr_library = {
            "trigger": "(hey chris|hay kris|ay cris|chris|kris|oi chris)",
            "exit": "(exit|stop|quit)",
            "java": "(java|ava|lava|guava|kaaba)",
            "v10": "(v10|ten)",
            "v4": "(v4|four)",
            "ppm": "(ppm|hours|timesheet|worked)",
            "help": "(help|need|who|what|where|why|how)",
            "secure": "(secure|permission|permissions|group|groups)" }

    # Return value from callback
    def get_value(self) -> str:
        if self.ret != None:
            ret = self.ret
            self.ret = None
            return ret
        return None

    def get_cmd(self, captured_speech):
        for key,expr in self.expr_library.items():
            if re.search(fr"{expr}", captured_speech):
                return key

    # Call back function for background listener
    def callback(self, recognizer, audio):
        try:
            captured_speech = recognizer.recognize_google(
                audio, key=self.API_KEY, language="en-US").lower()
            print("raw:", captured_speech)
            self.ret = self.get_cmd(captured_speech)
            if self.file:
                with open(re.sub(r"\..+$", '', self.file) + ".txt", 'a') as f:
                    f.write(self.ret + '\n')
        except sr.UnknownValueError:
            print("UnknownValueError: Speech is unintelligible")
        except sr.RequestError:
            print("RequestError: Could not requests results from API")

    # Listen for specified length of time
    def cmd_listen(self, file: str=None) -> str:
        try:
            with self.MIC as source:self.RECORD.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(self.RECORD.energy_threshold))
            try:
                with self.MIC as source:
                    audio = self.RECORD.listen(source, timeout=2, phrase_time_limit=self.wait)
                # recognize speech using Google Speech Recognition API
                captured_speech = self.RECORD.recognize_google(audio, key=self.API_KEY, language="en-US").lower()
                self.ret = self.get_cmd(captured_speech)
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
    def cmd_listen_background(self, file: str=None):
        try:
            self.file = file
            with self.MIC as source:self.RECORD.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(self.RECORD.energy_threshold))
            self.stop_listener = self.RECORD.listen_in_background(
                self.MIC, self.callback, phrase_time_limit=2)
        except KeyboardInterrupt:
            pass
        return self.stop_listener
