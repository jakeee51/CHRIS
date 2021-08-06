# -*- coding: utf-8 -*-

import CHRIS, time

# Initiate SpeechHandler object
SH = CHRIS.SpeechHandler()
# Execute cmd_listen when you want to take action
value = SH.cmd_listen_background()

print("Started")
c = 0
while c < 30:
    c += 1; value = SH.get_value(); time.sleep(1)
    if value == "java":
        print("Installing Java")
    elif value == "v10":
        print("Clone V10")
    elif value == "ppm":
        print("Opening PPM")
    elif value == "help":
        print("Helping you out")
    else:
        print(value)

SH.stop_listener(wait_for_stop=False)
