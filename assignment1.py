import os
import os.path
import csv
from datetime import datetime


#######################
#### Greg McCollum ####
#### Assignment 1 #####
#######################

#-navigating kernel to data folder
os.chdir("..")

#-initializing a list (to eventually be written to CSV) for file data, started with headers
data_inventory = [["absolute file path", "filename", "extension", "size (in bytes)", "last modified", "hash"]]

print("okay")

data_path = os.path.join("networked-services-labs","data")

for folder, subfolder, files in os.walk(data_path):
    #print(folder, subfolder, file)
    for file in files:
        file_data = []
        filepath = os.path.join(folder, file)
        #-add absolute path
        file_data.append(os.path.abspath(filepath))
        #-add filename
        file_data.append(os.path.basename(filepath))
        #-add extension
        file_data.append(os.path.splitext(filepath)[1])
        #-add filesize
        file_data.append(os.path.getsize(filepath))
        #-add modified time
        file_data.append(datetime.strftime(datetime.fromtimestamp(os.path.getmtime(filepath)),"%Y-%m-%d T%H:%m:%s"))
        #-add hash
        file_data.append("HASH DATA GOES HERE")

        #add file_data to inventory list
        data_inventory.append(file_data)

#-returning to directory I want to write this file to
os.chdir("Assignment1")

#-write inventory to CSV
with open("data_inventory.csv", "w") as f:
    writer = csv.writer(f,delimiter=",")
    writer.writerows(data_inventory)


