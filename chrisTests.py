# -*- coding: utf-8 -*-

import CHRIS, time

# Initiate SpeechHandler object
SH = CHRIS.SpeechHandler(wait=25)
# Execute cmd_listen when you want take action
value = SH.cmd_listen_background()

print("Continue")
c = 0
while c < 30:
    c += 1; value = SH.get_value(); time.sleep(1)
    if value == "java":
        print("install java")
    elif value == "v10":
        print("Clone V10")
    elif value == None:
        print(None)
    else:
        print(value)
        
SH.stop_listener(wait_for_stop=False)
