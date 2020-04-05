from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta_shopping



@app.route('/')
def home():
    return render_template('Shoppingmall_Home.html')

@app.route('/orders', methods=['POST'])
def order_post():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    add_receive = request.form['add_give']
    number_receive = request.form['number_give']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'add': add_receive,
        'number': number_receive}
    db.orders.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '주문이 접수되었습니다.'})

@app.route('/orders', methods=['GET'])
def order_get():
    orders = list(db.orders.find({}, {'_id': False}))

    return jsonify({'result':'success', 'orders': orders})


if __name__== '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
