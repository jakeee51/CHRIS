import os

CWD = os.getcwd()

# Navigate to secret directory
try:
    os.chdir(".."); os.chdir("..")
    os.chdir(".."); os.chdir("..")
    os.chdir("Desktop\\Prog\\CHRIS")
except FileNotFoundError:
    pass

def api_key():
   try:
      with open("api_key.txt") as f:
         return "AIzaSyAyQ0-RPbQxPExTF5golohThv2hNNQYQds" # Return API key string here
   except FileNotFoundError:
      pass
