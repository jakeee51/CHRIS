# -*- coding: utf-8 -*-

import CHRIS, time

def main():
   SH = CHRIS.SpeechHandler()
   value = SH.cmd_listen_background()
   print("Started!")
   while True:
      value = SH.get_value(); time.sleep(1); print(value)
      if value == "trigger":
         # Hafeth, put function to handle connections to commands here
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
