import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def countClass(fileName, className, rowIntervals, day):
    with open(fileName, 'r') as csvfile:
        classReader = csv.reader(csvfile, delimiter=',')
        next(classReader)
        occurrenceCounter = 0
        intervalCounter = rowIntervals
        occurrence = []

        for row in classReader:
            if len(row) > 0 and row[-1] != 'class':
                if int(row[2]) == day:
                    if int(row[-1]) == int(className):
                        occurrenceCounter += 1
                    if intervalCounter == 0:
                        occurrence.append(occurrenceCounter)
                        occurrenceCounter = 0
                        intervalCounter = rowIntervals
                    intervalCounter -= 1
        return occurrence

fileName = "npytocsv.csv"

unshiftedDays = [16,17,18,19,20,21]
shiftedDays = [22,23,24]
sumLists = []
minutes = 3600
className = 1
colors = ['r','g','b','y','black','magenta']
colors2 = ['grey', 'silver', 'tan']

#unshifted days
ax = plt.subplot(111)
for i in range(len(unshiftedDays)):
    occurrenceList = countClass(fileName, className, minutes, unshiftedDays[i])
    x = range(len(occurrenceList))
    line, = plt.plot(x, occurrenceList,colors[i],label=str(unshiftedDays[i]) + "-06" + "-15" + ("(b73)"))
    if i == 0:
        sumUnshifted = occurrenceList
    elif i > 0:
        sumUnshifted = [x + y for x, y in zip(occurrenceList, sumUnshifted)]
    
averageUnshifted = [x/len(days) for x in sumLists]

box = ax.get_position()
ax.set_position([box.x0,box.y0,box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1,0.5))
plt.show()


#shifted days
ax = plt.subplot(111)
for i in range(len(shiftedDays)):
    occurrenceList = countClass(fileName, className, minutes, shiftedDays[i])
    x = range(len(occurrenceList))
    plt.plot(x, occurrenceList,colors2[i],label=str(shiftedDays[i]) + "-06" + "-15" + ("(b73)"))
    if i == 0:
        sumShifted = occurrenceList
    elif i > 0:
        sumShifted = [x + y for x, y in zip(occurrenceList, sumShifted)]

box = ax.get_position()
ax.set_position([box.x0,box.y0,box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1,0.5))
plt.show()



# averages
ax = plt.subplot(111)
averageUnshifted = [x/len(unshiftedDays) for x in sumUnshifted]
x = range(len(averageUnshifted))
plt.plot(x, averageUnshifted, label="Average of days " + str(unshiftedDays[0]) + "-" + str(unshiftedDays[-1]))
box = ax.get_position()
ax.set_position([box.x0,box.y0,box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1,0.5))
plt.show()

ax = plt.subplot(111)
averageShifted = [x/len(shiftedDays) for x in sumShifted]
x = range(len(averageShifted))
plt.plot(x, averageShifted, label="Average of days " + str(shiftedDays[0]) + "-" + str(shiftedDays[-1]))
box = ax.get_position()
ax.set_position([box.x0,box.y0,box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1,0.5))
plt.show()

ax = plt.subplot(111)
x = range(len(averageUnshifted))
plt.plot(x, averageUnshifted,label="Average of days " + str(unshiftedDays[0]) + "-" + str(unshiftedDays[-1]))

x = range(len(averageShifted))
plt.plot(x, averageShifted, label="Average of days " + str(shiftedDays[0]) + "-" + str(shiftedDays[-1]))

box = ax.get_position()
ax.set_position([box.x0,box.y0,box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1,0.5))

plt.show()


