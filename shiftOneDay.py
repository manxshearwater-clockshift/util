import os 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--directory", help="set the directory", type=str)
args = parser.parse_args()

def shift_one_day(filename):
    split_list = filename.split("_")
    date = split_list[4]
    date = str(int(date)-1)

    new_name = split_list[0] + "_" + split_list[1] + "_" + split_list[2] + "_" +split_list[3] + "_" + str(date) + "_" + split_list[5] + "_" + split_list[6]
    return new_name

if __name__ == "__main__":
    path = args.directory
    files = os.listdir(path)
    for filename in files:
        new_filename = shift_one_day(filename)
        os.system("mv " + path + "/" + filename + " " + path + "/" + new_filename)
