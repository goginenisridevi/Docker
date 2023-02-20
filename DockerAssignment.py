import os
import socket
from collections import Counter

Counter = Counter()

def getMyIPAdress():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr

def getNumberOfWords(file):
    totalwordcount = 0
    with open(file, 'r') as file:
        for line in file:
            if (line != '\n'):
                if (file.name.endswith("IF.txt")):
                    Counter.update(line.replace("Â", "").split())
                totalwordcount = totalwordcount + len(line.replace("Â", "").split())
    return totalwordcount

TextFilesWordCounts = {}
path ="/home/data"
if os.path.exists(path + "/" +"result.txt"):
  os.remove(path + "/" +"result.txt")
outputString="************|| text file at location: /home/data ||************\n"
for eachFile in os.listdir(path):
    if eachFile.endswith(".txt"):
        outputString=outputString+eachFile+"\n"
        TextFilesWordCounts[eachFile] = getNumberOfWords(path + "/" + eachFile)
		
outputString=outputString+"\n"
outputString=outputString+"************|| b.Read the two text files and count total number of words in each text files ||************\n"
AllFilesWordCount = 0
AllFilesNames = ""
for eachkey in TextFilesWordCounts.keys():
    AllFilesNames = AllFilesNames + eachkey + ","
    AllFilesWordCount = AllFilesWordCount + TextFilesWordCounts.get(eachkey)
    outputString = outputString +"total number of words in [" + eachkey + "] is : " + str(TextFilesWordCounts.get(eachkey))+"\n"

outputString = outputString +"\n"
outputString = outputString +"************|| grand total (total number of words in both files) ||************\n"
outputString = outputString +"total number of words in both files [" + AllFilesNames[0:len(AllFilesNames) - 1] + "] is: " + str(AllFilesWordCount)+"\n"

outputString = outputString +"\n"
outputString = outputString +"************|| top 3 words with maximum number of counts in IF.txt ||************\n"
outputString = outputString +str(Counter.most_common(3))+"\n"

outputString = outputString +"\n"
outputString = outputString +"************|| IP address ||************\n"
outputString = outputString +"Your Computer IP Address is:" + getMyIPAdress()

resultsTextFile = open(path + "/" +"result.txt","w")
resultsTextFile.write(outputString)
resultsTextFile.close()
for eachline in open(path + "/" +"result.txt","r").readlines():
    print(eachline.replace("\n",""))