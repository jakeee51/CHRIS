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
def pullRepo(repoName,branchName):
    g = git.Git(repoName)
    g.pull('origin',branchName)

def openPage(pageUrl):
    webbrowser.open(pageUrl)

def installJava(versionNum):
    jdk.install(str(versionNum))
    print("installed Jave " + str(versionNum)+ " into $HOME/.jdk")
