# -*- coding: utf-8 -*-
'''
Author: David J. Morfe
Application Name: Speech Handler for C.H.R.I.S.
Functionality Purpose: Intake and process speech to recognize requested action
'''

##import speech_recognition as sr
import time
import re


##RECORD = sr.Recognizer() #Audio Record Variable
##MIC = sr.Microphone() #Microphone Variable


class SpeechHandler:
    '''This class instantiates the connector software to interface with other modules'''
    def __init__(self):
        self.lang = ()
        self.said = ""
        self.epat = ["(jump|trump|lump|hump|clump|dump|stump)", #English
                     "(duck|duct|truck|luck|yuck|stuck|muck|abduct)",
                     "(throw|row|mow|low|go|bow|boe|thorough|trough|bro)"]

    #Psuedo Switch Statement
    def switch(self, c):
        if c == 0: #English
            return ("en-US", self.epat)

    #Return the spoken language
    def lang_handler(self):
        langC = ""
        try:
            #print("A moment of silence, please...")
            with m as source: r.adjust_for_ambient_noise(source)
            #print("Set minimum energy threshold to {}".format(r.energy_threshold))
            while True:
                print("Speak the name of a language:  ")
                with m as source: audio = r.listen(source)
                try:
                    langCheck = r.recognize_google(audio, language="en-US")
                    if re.search(r"(english|ingles)", langCheck.lower()):
                        langC = 0
                except sr.UnknownValueError:
                    pass
                if langC != "":
                    return langC
        except KeyboardInterrupt:
            pass

    #Return the intended command
    def cmd_handler(self, file="log.txt"):
        self.lang = self.switch(self.lang_handler()) #Language determinants of type tuple: (str, list)
        print("Language: ", self.lang[0])
        try:
            #print("A moment of silence, please...")
            with m as source: r.adjust_for_ambient_noise(source)
            #print("Set minimum energy threshold to {}".format(r.energy_threshold))
            while True:
                with open(file, "a") as f:
                    print("Say a command!")
                    with m as source: audio = r.listen(source)
                    try:
                        # recognize speech using Google Speech Recognition
                        value = r.recognize_google(audio, language=self.lang[0])
                        print(f"You said {value}")
                        if re.search(fr"{self.lang[1][0]}", value.lower()):
                            f.write("JUMPED" + '\n')
                        elif re.search(fr"{self.lang[1][1]}", value.lower()):
                            f.write("DUCKED" + '\n')
                        elif re.search(fr"{self.lang[1][2]}", value.lower()):
                            f.write("THROWN" + '\n')
                        else:
                            pass
                    except sr.UnknownValueError:
                        pass
        except KeyboardInterrupt:
            pass

##SpeechHandler().cmd_handler()