from flask import Flask, jsonify
# CORS ( Cross Origin Resource Sharing ) 다른 도메인이나 로컬 환경에서 자바스크립트로 api 등을 호출하는 경우 브라우저에서 동일 출처 위반의 에러가 나타날때 해결하기 위함
from flask_cors import CORS

# set My log
from my_util.my_logger import my_logger

# import는 모듈을 가져오기 위함 
# from 모듈 import 이름   :  모듈내에서 필요한것만  가져오기 위함 


import os
# 현재 작업 폴더를 알아내기 위한 함수
os.getcwd()
# highlight 의 분석한 결과를 가져오자 
from src import highlight_function as hl


# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/', methods=['GET'])
def test_router():
    my_logger.info("hello this is root url!!!")
    return jsonify('This is Docker Test developments Server! ')


@app.route('/health_check', methods=['GET'])
def health_check():
    my_logger.info("health check route url!!")
    return jsonify('good')

@app.route('/review', methods=['GET'])
def review():

    line_test='soogeun.jung'
    my_logger.info("review start!!!!!!!!!!!!!!!!!!!!!!!!" )

    print("test highlight")
    line_test = hl.highlight_start(line_test)   
    text =  " ".join(map(str, line_test))
    my_logger.info("review end!!!!!!!!!!!!!!!!!!!!!!!!" +text ) 
    #return jsonify(line_test)
    return text


if __name__ == '__main__':
    # review()
    # 다른 파일 import 테스트 때문에 밑에 주석처리해놈 2021/07/16
    app.run(host='0.0.0.0',port=os.getenv('FLASK_RUN_PORT'),debug=os.getenv('FLASK_DEBUG'))