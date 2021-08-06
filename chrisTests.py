# -*- coding: utf-8 -*-

import CHRIS, time
import chrisFunctions as cf

# Initiate SpeechHandler object
SH = CHRIS.SpeechHandler()
# Execute cmd_listen when you want take action
value = SH.cmd_listen_background()

print("Continue")
c = 0
while c < 30:
    c += 1; value = SH.get_value(); time.sleep(1)
    if value == "java":
    try:
        cf.installJava(11)
    except:
        print("error")    elif value == "v10":
        print("Clone V10")
    elif value == "ppm":
        print("OIIIII")
        cf.openPage("https://ppmi.optum.com")
    elif value == None:
        print(None)
    else:
        print(value)

SH.stop_listener(wait_for_stop=False)


# -*- coding: utf-8 -*-

import CHRIS, time
import chrisFunctions as cf

# Initiate SpeechHandler object
SH = CHRIS.SpeechHandler(wait=5)
# Execute cmd_listen when you want take action
value = SH.cmd_listen()

print("Continue")
c = 0
while c < 30:
    c += 1; value = SH.get_value(); time.sleep(1)
    if value == "java":
        print("yeah yeah yeah yeah")
        try:
            cf.installJava(11)
        except:
            print("error")
    elif value == "v10":
        print("Clone V10")
    elif value == "ppm":
        print("OIIIII")
        cf.openPage("https://ppmi.optum.com")
    elif value == None:
        print(None)
    else:
        print(value)
    break

# SH.stop_listener(wait_for_stop=False)
