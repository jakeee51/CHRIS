# -*- coding: utf-8 -*-

import CHRIS, time
import chrisFunctions as cf

def main():
   SH = CHRIS.SpeechHandler(3)
   value = SH.cmd_listen_background()
   robot = """
              .andAHHAbnn.
           .aAHHHAAUUAAHHHAn.
          dHP^~"        "~^THb.
    .   .AHF                YHA.   .
    |  .AHHb.              .dHHA.  |
    |  HHAUAAHAbn      adAHAAUAHA  |
    I  HF~"_____        ____ ]HHH  I
   HHI HAPK""~^YUHb  dAHHHHHHHHHH IHH
   HHI HHHD> .andHH  HHUUP^~YHHHH IHH
   YUI ]HHP     "~Y  P~"     THH[ IUP
    "  `HK                   ]HH'  "
        THAn.  .d.aAAn.b.  .dHHP
        ]HHHHAAUP" ~~ "YUAAHHHH[
        `HHP^~"  .annn.  "~^YHH'
         YHb    ~" "" "~    dHF
          "YAb..abdHHbndbndAP"
           THHAAb.  .adAHHF
            "UHHHHHHHHHHU"
              ]HHUUHHHHHH[
            .adHHb "HHHHHbn.
     ..andAAHHHHHHb.AHHHHHHHAAbnn..
.ndAAHHHHHHUUHHHHHHHHHHUP^~"~^YUHHHAAbn.
  "~^YUHHP"   "~^YUHHUP"        "^YUP^"
       ""         "~~"
       """

   print(robot)
   print("Started!")


   while True:
      value = SH.get_value(); time.sleep(1); print(value)
      if value == "trigger":
         # Hafeth, put function to handle connections to commands here
         SH.stop_listener(wait_for_stop=False)
         value2 = SH.cmd_listen();
         SH.cmd_listen_background()
         if value2 == "java":
              # Hafeth, put function to handle connections to commands here
            try:
                cf.installJava(11)
            except:
                print("error")

         elif value2 == "ppm":
             cf.openPage("https://ppmi.optum.com")



         print("Say a command!")

      elif value == "exit":
         SH.stop_listener(wait_for_stop=False)
         print("Exiting..."); break
      else:
         value = None
         continue

if __name__ == "__main__":
   print("Starting...")
   main()
