import os

def getSampleTime(fileName):
    splitList = fileName.split("_")
    date = splitList[4]

    #starting time of day recording
    startTime = splitList[6]

    #minutes from startingtime
    minutesOffset = splitList[7]
    m = minutesOffset.index("m")
    minutesOffset = minutesOffset[0:m] + minutesOffset[m+1:]
    minutesOffset = int(minutesOffset[0:3])

    hours = int(startTime[0] + startTime[1])
    minutes = int(startTime[2] + startTime[3])
    seconds = int(startTime[4] + startTime[5])

    minutes = minutes + minutesOffset
    if minutes >= 60:
        offsetHours = int(minutes/60)
        minutes = minutes % 60        
        hours = hours + offsetHours
        if hours >= 24:
            offsetDate = int(hours/24)
            hours = hours % 24
            date = int(date) + offsetDate
    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)

    newName = splitList[0] + "_" + splitList[1] + "_" + splitList[2] + "_" + splitList[3] + "_" + str(date) + "_" + splitList[5] + "_" + str(hours) + str(minutes) + str(seconds) + ".npy"
    return newName


path = "/home/yorick/ManxShearwaterProject/results/b73"
files = os.listdir(path)
for fileName in files:
    newFilename = getSampleTime(fileName)
    os.system("mv " + path + "/" + fileName + " " + path + "/" + newFilename)
