import os

def getSampleTime(fileName):
    splitList = fileName.split("_")
    date = splitList[4]

    #starting time of day recording
    startTime = splitList[6]

    #minutes from startingtime
    minutesOffset = splitList[7]
    minutesOffset = int(minutesOffset[0] + minutesOffset[1] + minutesOffset[2] + minutesOffset[3])
    
    hours = int(startTime[0] + startTime[1])
    minutes = int(startTime[2] + startTime[3])
    seconds = int(startTime[4] + startTime[5])

    minutes = minutes + minutesOffset
    print(minutes)
    if minutes >= 60:
        offsetHours = int(minutes/60)
        minutes = minutes % 60        
        print(offsetHours)
        print(int(minutes/60))
        hours = hours + offsetHours
        if hours >= 24:
            offsetDate = int(hours/24)
            hours = hours % 24
            date = int(date) + offsetDate
    if hours < 10:
        hours = str("0") + str(hours)
    if minutes < 10:
        minutes = str("0") + str(minutes)

    newName = splitList[0] + "_" + splitList[1] + "_" + splitList[2] + "_" + splitList[3] + "_" + str(date) + "_" + splitList[5] + "_" + str(hours) + str(minutes) + str(seconds) + ".npy"
    return newName


rootfolder =  "/Volumes/Vogeltjes/resultsb73"
files = os.listdir(rootfolder)
for fileName in files:
    newFilename = getSampleTime(fileName)
    os.system("mv " + rootfolder + "/" + fileName + " " + rootfolder + "/" + newFilename)


