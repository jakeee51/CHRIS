# -*- coding: utf-8 -*-

import CHRIS

# Initiate SpeechHandler object
SH = CHRIS.SpeechHandler()
# Execute cmd_listen when you want take action
# Timeout after 2 seconds & listens for 8 seconds total
value = SH.cmd_listen()

if value == "java":
    print("install java")
elif value == "pull":
    print("pull V10")
else:
    print(value)
