#!/usr/bin/python3

import sys
import re
import csv
def task2_mapper():

    country_vid_dic = {}
    for line in sys.stdin:

        data = list(csv.reader([line]))
        if len(data[0]) != 18:
            continue     
        try:
            float(data[0][8]) 
        except:
            continue
    
        print("{}\t{}\t{}".format(data[0][-1],data[0][0], data[0][8]))


if __name__ == "__main__":
    task2_mapper()
