import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import sys
from konlpy.tag import Twitter

import re
from konlpy.tag import Okt
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

# 요 리스트들로 하이라이트를 주고싶다.
from termcolor import colored
import os
import requests
from my_util.my_logger import my_logger
import csv
import urllib.request
import codecs

def apply_regular_expression(text):
    hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')  # 한글 추출 규칙: 띄어 쓰기(1 개)를 포함한 한글
    result = hangul.sub('', text)  # 위에 설정한 "hangul"규칙을 "text"에 적용(.sub)시킴
    return result

#df = pd.read_csv("https://raw.githubusercontent.com/yoonkt200/FastCampusDataset/master/tripadviser_review.csv")

def highlight_start(line_test):
    print("hilight start!!!!!!!!!" , line_test)
    df = pd.read_csv("https://raw.githubusercontent.com/mojjijung/Vue/master/dev.csv")
    df.head()
    # dimension
    df.shape

    my_logger.info("df create !!" )

    #text 변수
    text =''

    okt = Okt()  # 명사 형태소 추출 함수
    nouns = okt.nouns(apply_regular_expression(df['text'][0]))
    #nouns
    #print(nouns)
    my_logger.info("nonus create !!" )
 
    url = "https://raw.githubusercontent.com/mojjijung/Vue/master/dev.csv"
    #req = requests.get(url)
    #url_content = req.content
    #csv_file = open('dev.csv','wb')

    response = urllib.request.urlopen(url)
    cr = csv.reader(codecs.iterdecode(response, 'utf-8'))

    # file_name = 'https://raw.githubusercontent.com/mojjijung/Vue/master/dev.csv'
    #f = open('dev.csv')     # 파일 열기
    #f = open(req)
    text =[]
    for line in cr:                # 한 줄씩 읽기   
        
        for i in nouns:           # 단어를 list에 넣어놨는데 그 list로 다시 for문 돌리기
            if i in line:         # list를 한줄 씩 읽어서 단어가 있는지 찾아낸다.
                #highlighted = line.replace(i, colored(i,'white','on_red'))
                line = line.replace(i, colored(i,'white','on_yellow'))
                

            if i is nouns[-1]:
                print(line)
                #text = text+line
                text.append(line)


    #f.close()                     # 파일 닫기
    #cr.close()
    #print("end 222222: " ,text)

    s = list(text)

    print("text list "  , s)
    my_logger.info("text create !!")
    return s
