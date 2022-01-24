import glob
import re
import mactag
import os

fileList = glob.glob("/Users/andrej/Documents/ARCHIVE_WORKING_COPYs/*")
allFoundTags = {'cukr'}

for aFile in fileList:
    tags = re.search('(.*)\[(.*)\](.*)', aFile, re.IGNORECASE)
    if tags:
        finalFileName = tags.group(1) + tags.group(3)
        tagList = tags.group(2).split()
        for aTag in tagList:
            allFoundTags.add(aTag)
        mactag.add(tagList, aFile)
        os.rename(aFile, finalFileName)
        print("+" + finalFileName + " : " + tagList.__str__())
    else:
        print("-" + aFile)

print("All found tags: " + allFoundTags.__str__())