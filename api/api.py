import flask
from flask import jsonify
# from flask import abort
from flask import request

# flake8: noqa
app = flask.Flask(__name__)
app.config["DEBUG"] = True


prod_list = [{"name":"mx33",
               "id": "1"},
            {"name":"mx34",
               "id": "2"},
            {"name":"mx35",
               "id": "3"}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Assist to Purchase</h1><p>This site is a prototype API for helping consumers get the best products.</p>"

@app.route('/getproduct',methods=['GET'])
def getproduct():
    return jsonify(prod_list)

@app.route('/addproducts',methods=['POST'])
def addproduct():
    new_prod = {
        "id":request.json["id"],
        "name":request.json["name"]
    }
    prod_list.append(new_prod)
    return jsonify(prod_list),201

# @app.route('/deleteprod/<int:task_id>', methods=['DELETE'])
# def delete_task(task_id):
#     if request.method == 'DELETE':
#         prod_list.pop(task_id)
#         return jsonify({'result': True}),204

# @app.route('/update/<int:task_id>', methods=['PUT'])
# def update_task(task_id):
#     if  request.method == 'PUT':
#         prod_list['id'] = request.json['id']
#         prod_list['name'] = request.json['name']
#         return jsonify({'task': 'updated'})


if __name__ == '__main__':
    app.run()