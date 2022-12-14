
# SI676 - Assignment 1, Data Inventory Repository

Gregory McCollum - gregmcc@umich.edu - University of Michigan, Ann Arbor, Michigan

An assignment developing an inventory of the "data" folder from this [repository](https://github.com/morskyjezek/networked-services-labs).

Due Date: October 12, 2022

Data Gathered: October 7th, 2022

*Repository last updated on October 7th, 2022*

## Provenance

The files in this repository was created by Gregory McCollum, a student in the University of Michigan School of Information Master of Science in Information program's SI676 course.

The files documented by my scripts are from Dr. Jesse Johntson, the course instructor. Additionally the get_checksum() function in assignment1.py was developed by Dr. Jesse Johntson
## Repository Files

This repository contains the following files:

- **assignment1.py** - a Python script that uses the os.walk() function to loop through the materials in the 'data' directory and extracting metadata from them.
- **data_inventory.csv** - a CSV document containing the file metadata extracted by assignment1.py


## Data Inventory Fields

The **data_inventory.csv** file contains the following field:

- *absolute file path* - str - indicating each file's location on my local drive
- *filename* - str - indicating the file's name
- *extension* - the dot extension code used at the end of the filename
- *size* - int - indicating the file's size in bytes
- *last modified* - YYYY-MM-DD HH-MM-S - a timestamp of when the file was last modified
- *md5_checksum* - str - a checksum for that file developed by MD5 checksum algorithm
- *sha256_checksum* - str- a checksum for that file developed by SHA256 checksum algorithm
