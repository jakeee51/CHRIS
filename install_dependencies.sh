#!/bin/bash
echo "Installing dependencies..."
pip3 install -r requirments.txt
sudo su
chmod 777 /usr/local/share/zsh
chmod 777 /usr/local/share/zsh/site-functions
exit
brew install portaudio && pip3 install pyaudio && brew install flac
echo "Execute chrisTests.py from terminal then *allow* microphone permission"