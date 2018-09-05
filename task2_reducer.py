#!/usr/bin/python3

import sys

def read_map_output(file):
    for line in file:
        
        
        yield line.strip('\n').split('\t')


def task2_reducer():


    tmp = read_map_output(sys.stdin)
    
    country_vid_dic = {}
    current = ""
    for country, videoid, views in tmp:     
        if current != country:
            if current != "":
                for vid in country_vid_dic:
                    if len(country_vid_dic[vid]) > 1:
                        sorted_integers = sorted(country_vid_dic[vid])
                        result = 100*(sorted_integers[1] - sorted_integers[0])/sorted_integers[0]
                        if result > 1000:
                            print("{}\t{}\t{}".format(current, vid,result))   

            current = country
            country_vid_dic = {}


        if videoid not in country_vid_dic:
            country_vid_dic[videoid] = []
        country_vid_dic[videoid].append(float(views))


    if current != "":
        for vid in country_vid_dic:
            if len(country_vid_dic[vid]) > 1:
                sorted_integers = sorted(country_vid_dic[vid])
                result = 100*(sorted_integers[1] - sorted_integers[0])/sorted_integers[0]
                if result > 1000:
                    print("{}\t{}\t{}".format(current, vid,result))   



if __name__ == "__main__":
    task2_reducer()
