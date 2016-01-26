import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="set the directory",
                    type=str)
args = parser.parse_args()

def get_sample_time(file_name):
    split_list = file_name.split("_")
    date = split_list[4]

    #starting time of day recording
    start_time = split_list[6]

    #minutes from startingtime
    minutes_offset = split_list[7]
    m = minutes_offset.index("m")
    minutes_offset = minutes_offset[0:m] + minutes_offset[m+1:]
    minutes_offset = int(minutes_offset[0:m])


    hours = int(start_time[0] + start_time[1])
    minutes = int(start_time[2] + start_time[3])
    seconds = int(start_time[4] + start_time[5])

    minutes = minutes + minutes_offset
    if minutes >= 60:
        offset_hours = int(minutes/60)
        minutes = minutes % 60        
        hours = hours + offset_hours
        if hours >= 24:
            offset_date = int(hours/24)
            hours = hours % 24
            date = int(date) + offset_date
    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)

    newName = split_list[0] + "_" + split_list[1] + "_" + split_list[2] + "_" + split_list[3] + "_" + str(date) + "_" + split_list[5] + "_" + str(hours) + str(minutes) + str(seconds) + ".npy"
    return newName

if __name__ == "__main__":
	path = args.directory
	files = os.listdir(path)
	for file_name in files:
	    new_file_name = get_sample_time(file_name)
	    os.system("ren " + path + "\\" + file_name + " " + new_file_name)

