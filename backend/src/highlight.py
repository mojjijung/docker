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
def apply_regular_expression(text):
    hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')  # 한글 추출 규칙: 띄어 쓰기(1 개)를 포함한 한글
    result = hangul.sub('', text)  # 위에 설정한 "hangul"규칙을 "text"에 적용(.sub)시킴
    return result

#df = pd.read_csv("https://raw.githubusercontent.com/yoonkt200/FastCampusDataset/master/tripadviser_review.csv")
df = pd.read_csv("dev.csv")

df.head()

# dimension
df.shape
#print(df.shape)

# information
# df.info()

# text 변수 확인

#df['text'][0]
#print(df['text'][0])

#apply_regular_expression(df['text'][0])
#print(apply_regular_expression(df['text'][0]))


okt = Okt()  # 명사 형태소 추출 함수
nouns = okt.nouns(apply_regular_expression(df['text'][0]))
#nouns
print(nouns)
# 요 리스트들로 하이라이트를 주고싶다.
from termcolor import colored

file_name = 'dev.csv'
f = open(file_name)      # 파일 열기
for line in f:                # 한 줄씩 읽기   
    
    for i in nouns:           # 단어를 list에 넣어놨는데 그 list로 다시 for문 돌리기
        if i in line:         # list를 한줄 씩 읽어서 단어가 있는지 찾아낸다.
            #highlighted = line.replace(i, colored(i,'white','on_red'))
            line = line.replace(i, colored(i,'white','on_yellow'))
        if i is nouns[-1]:
            print(line)


f.close()                     # 파일 닫기

# 말뭉치 생성
#corpus = "".join(df['text'].tolist())
#corpus
# print(corpus)

# 정규 표현식 적용
#apply_regular_expression(corpus)

# 전체 말뭉치(corpus)에서 명사 형태소 추출
#nouns = okt.nouns(apply_regular_expression(corpus))
# print(nouns)


# 빈도 탐색
#counter = Counter(nouns)

# counter.most_common(10)
# # print(counter.most_common(10))

# # 한글자로 된 부분 제거
# available_counter = Counter({x: counter[x] for x in counter if len(x) > 1})
# available_counter.most_common(10)

# # 사용하지 않을 언어들 추가하기
# stopwords = pd.read_csv("https://raw.githubusercontent.com/yoonkt200/"
#                         + "FastCampusDataset/master/korean_stopwords.txt").values.tolist()

# jeju_hotel_stopwords = ['제주', '제주도', '호텔', '리뷰', '숙소', '여행', '트립']
# for word in jeju_hotel_stopwords:
#     stopwords.append(word)


# def text_cleaning(text):
#     hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')  # 정규 표현식 처리
#     result = hangul.sub('', text)
#     okt = Okt()  # 형태소 추출
#     nouns = okt.nouns(result)
#     nouns = [x for x in nouns if len(x) > 1]  # 한글자 키워드 제거
#     nouns = [x for x in nouns if x not in stopwords]  # 불용어 제거
#     return nouns


# vect = CountVectorizer(tokenizer = lambda x: text_cleaning(x))

# # 각 단어의 리뷰별 등장 횟수
# bow_vect = vect.fit_transform(df['text'].tolist())

# # 단어 리스트
# word_list = vect.get_feature_names()

# # 각 단어가 전체 리뷰중에 등장한 총 횟수
# count_list = bow_vect.toarray().sum(axis=0)

# # "단어" - "총 등장 횟수" Matching
# word_count_dict = dict(zip(word_list, count_list))
# word_count_dict
# # print(word_count_dict)

# # 빈도 탐색
# counter = Counter(word_count_dict)
# counter.most_common(10)
# print(counter.most_common(10))





