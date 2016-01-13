#
import os

#rootFolder = "/Volumes/Vogeltjes/Parts_one_hour"
#destFolder = "/Volumes/Vogeltjes/outputWaves"

rootFolder = "/Volumes/Vogeltjes/outputWaves"

counter = 0

# get folderNames
#folders = os.listdir(rootFolder)
folders = os.system("ls")


for folder in folders:

#    os.system("mkdir" + " /Volumes/Vogeltjes/outputWaves" + "/" + folder)
    dates = os.listdir(rootFolder + "/" + folder)
    
    for date in dates:
        fileNames = os.listdir(rootFolder + "/" + folder + "/" + date)
#        os.system("mkdir" + " /Volumes/Vogeltjes/outputWaves" + "/" + folder + "/" + date)

        for filename in fileNames:
            #mpg321 -w output.wav input.mp3
            print("converting:" + folder + "/" +filename + "\n \n")

            newFileName = filename.split(".")
            newFileName = newFileName[0] + ".wav"

            #move files
            os.system("mv " + rootFolder + "/" + folder + "/" + date + "/" + filename + " " + rootFolder + "/" + folder + "/" + date + "/" + newFileName)
            print(rootFolder + "/" + folder + "/" + date + "/" + newFileName)

            #convertFiles
 #           os.system("mpg321 -w" +
#                      #output
#                      "/Volumes/Vogeltjes/outputWaves" + "/" + folder + "/" +
#                      date + "/" + filename + ".wav " +
                      #input
#                      rootFolder + "/" + folder + "/" + date + "/" + filename)
