import json
import os

def readJsonFile(fileName):
    dictio = {}
    exists = False
    if os.path.isfile(fileName):
        with open(fileName, "r") as fileH:
            dictio = json.load(fileH)
            fileH.close()
            exists = True
    return dictio, exists

def writeJsonFile(fileName, dictionary):
    fileH = open(fileName, "w")
    dString = json.dumps(dictionary, sort_keys=True, indent=1)
    fileH.write("{}".format(dString))
    fileH.close()

