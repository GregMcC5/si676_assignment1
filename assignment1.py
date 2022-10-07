import os
import os.path
import csv
from datetime import datetime
import hashlib


#######################
#### Greg McCollum ####
#### Assignment 1 #####
#######################

def get_checksum(filePath, checksum_type):
    '''This is a helper function to create a checksum. 

    This function is by Dr. Jesse Johnston, and not Gregory McCollum

    In this example we will focus on MD5, which can be used to check data integrity.

    The filePath value argument be a string representing a valid path.
    The checksum_type argument should be a valid type of checksum.
    
    The function returns the string of characters for an MD5 or SHA256 checksum.
    The is function only allows you to create MD5 or SHA 256 and will result in an error for other types.'''
    checksum_type = checksum_type.lower().replace(" ","")

    with open(filePath, 'rb') as f:
        bytes = f.read()
        if checksum_type == 'md5':
            hash_string = hashlib.md5(bytes).hexdigest()
        elif checksum_type == 'sha256':
            hash_string = hashlib.sha256(bytes).hexdigest()
        else:
            Raise('{} is not a hash function supported by this program. You must ask for MD5.')
    return hash_string

#-navigating kernel to data folder
os.chdir("..")

#-initializing a list (to eventually be written to CSV) for file data, started with headers
data_inventory = list()

headers = ["absolute file path", "filename", "extension", "size (in bytes)", "last modified", "md5_checksum", "sha256_checksum"]

data_path = os.path.join("networked-services-labs","data")

for folder, subfolder, files in os.walk(data_path):
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
        file_data.append(datetime.strftime(datetime.fromtimestamp(os.path.getmtime(filepath)),"%Y-%m-%d T %H:%M:%S"))
        #-add md5_checksum
        file_data.append(get_checksum(filepath, "md5"))
        #-add sha256_checksum
        file_data.append(get_checksum(filepath, "sha256"))

        #add file_data to inventory list
        data_inventory.append(file_data)

#-returning to directory I want to write this file to
os.chdir("Assignment1")

#-write inventory to CSV
with open("data_inventory.csv", "w") as f:
    writer = csv.writer(f,delimiter=",")
    writer.writerow(headers)
    print("Wrote Headers")
    for row in data_inventory:
        writer.writerow(row)
print("done")



