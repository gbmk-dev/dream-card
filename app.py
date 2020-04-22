from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)
db = client.dreamCard                    # 'dreamCard'라는 이름의 db를 만듭니다.


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


# 검색한 식당 이름이 포함된 List를 불러오는 API
@app.route('/county', methods=['GET'])
def dream_card_get():
    restaurant_find = list(db.county_files.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'info': restaurant_find})

    #restaurant_name_receive = request.args.get('restaurant_name_give')
    #print(restaurant_name_receive)
    #restaurant_find = list(db.county_files.find({'restaurant_name': restaurant_name_receive}, {'_id': 0}))
    #print(restaurant_find)
    #return jsonify({'result': 'success', 'info': restaurant_find})


@app.route('/county', methods=['POST'])
def dream_card_post():

    restaurant_name = request.form['restaurant_name_give']
    restaurant_type = request.form['restaurant_type_give']
    restaurant_phoneNumber = request.form['restaurant_phoneNumber_give']
    restaurant_address = request.form['restaurant_address_give']
    county_name = request.form['county_name_give']

    print(county_name, restaurant_name, restaurant_type, restaurant_phoneNumber, restaurant_address)

    query = {}
    if restaurant_name != '':
        query['restaurant_name'] = restaurant_name
    if county_name != '':
        query['county_name'] = county_name
    print(query)
    # restaurants = list(db.county_files.find({'county_name': '강북구'}, {'_id': 0}))
    restaurants_find = list(db.county_files.find(query, {'_id': 0}))
    print(restaurants_find)
    return jsonify({'result': 'post success', 'restaurants': restaurants_find})
    
    # restaurants = list(db.county_files.find({'restaurant_name':restaurant_name, 'county_name': county_name}, {'_id': 0}))
    # county = list(db.county_files.find({'county_name': county_name}, {'_id': 0}))
    # restaurants_only = list(db.county_files.find({'restaurant_name':restaurant_name}, {'_id': 0}))

    # return jsonify({'result': 'success', 'restaurants': restaurants, 'county': county, 'restaurants_only': restaurants_only})


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)