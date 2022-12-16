

import argparse
import os
import argparse
import webvtt
import pprint
from datetime import datetime, timedelta


def split_vtt(vtt_file, split_time):
    ret_list=[]
    text_buff=""
    time_buff=0
    buff_start=""
    buff_end=""
    i=0
    for caption in webvtt.read(vtt_file):
        time_start= datetime.strptime(caption.start, "%H:%M:%S.%f")
        time_end= datetime.strptime(caption.end, "%H:%M:%S.%f")
        diff=time_end-time_start
        if text_buff=="":
            buff_start=caption.start
        time_buff=time_buff+diff.total_seconds()
        text_buff=text_buff+caption.text
        #buff_start=""
        buff_end=caption.end
        if time_buff >= split_time :
            ret_list.append({
                            "start":buff_start,
                            "end":buff_end,
                            "text":text_buff,
                            "sec":time_buff,
                            })
            time_buff=0
            text_buff=""
    return ret_list
    
    
    

parser = argparse.ArgumentParser()
parser.add_argument('file', help='the file to be processed')
parser.add_argument('split', help='seconds to split')

args = parser.parse_args()

if os.path.exists(args.file):
    print('The file exists')
    sub_list=split_vtt("metalova_dvojacat_buh_neni.mp3.vtt", 25)
    print("Celkem scen/obrazku", len(sub_list))
    for i in sub_list:
        print(i["start"],i["end"],i["sec"])
        #print("Summarize following text to one line.")
        print("Condense following text to one line, focus on nouns and adjectives and description of scenery.")
        print(i["text"])
        print("----------------")
  

#pprint.pprint(split_vtt("jirout.mkv.vtt",30))
            
#import deepl

#auth_key = "f63c02c5-f056-..."  # Replace with your key
#translator = deepl.Translator(auth_key)
#result = translator.translate_text("Hello, world!", target_lang="FR")
#print(result.text)  # "Bonjour, le monde !"
