#!/usr/bin/python3

import sys

def read_map_output(file):

    for line in file:
        
        
        yield line.strip('\n').split('\t')


def second_reducer():

    
    tmp = read_map_output(sys.stdin)
    # if len(tmp) == 3:
    country_vid_dic = {}
    current = ""

    for country, videoid, views in tmp:  
        if current != country:
            if current != "":
                for key, value in sorted(country_vid_dic.iteritems(), reverse=True,key=lambda (k,v): (v,k)):
                    print("{}; {}, {}%".format(current,key,format(value, '.1f')))

            current = country
            country_vid_dic = {}

        country_vid_dic[videoid] = float(views)

    if current != "":
        for key, value in sorted(country_vid_dic.iteritems(), reverse=True,key=lambda (k,v): (v,k)):
                    print("{}; {}, {}%".format(current,key,format(value, '.1f')))

if __name__ == "__main__":
    second_reducer()
