import requests
import json
import argparse
import git
import os
import webbrowser
import jdk

def cloneRepo(githubRepoUrl,repoName):
    git.Repo.clone_from(githubRepoUrl,repoName)
#https://github.optum.com/pes/NDBProviderSearchV10-war.git

def openPage(pageUrl):
    webbrowser.open(pageUrl)

def installJava(versionNum):
    jdk.install(str(versionNum))
    print("installed Java " + str(versionNum)+ " into $HOME/.jdk")

def connect_cmds(SH):
    value = SH.cmd_listen();
    if value == "java":
        print("INSTALLING JAVA")
        try:
            installJava(11)
        except:
            print("error")
    elif value == "ppm":
        print("NAVIGATING TO PPM")
        openPage("https://ppmi.optum.com")
    elif value == "secure":
        print("NAVIGATING TO SECURE")
        openPage("https://secure.uhc.com")
    elif value == "v10":
        print("CLONING THE V10 API")
        cloneRepo("https://github.optum.com/pes/NDBProviderSearchV10-war.git","V10")
    elif value == "v4":
        print("CLONING THE V4 API")
        cloneRepo("https://github.optum.com/pes/NDBPhysnFaclSearchV4-war.git","V4")
