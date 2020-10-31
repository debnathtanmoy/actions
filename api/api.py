from flask import Flask, jsonify
from flask import abort
from flask import request

# flake8: noqa
app = Flask(__name__)

products = [
    {
        'id': 1,
        'title': u'mx33',
        'description': u'effective for small ICUS'
    },
    {
        'id': 2,
        'title': u'mx53',
        'description': u'effective for medium sized ICUS'
    }
]

@app.route('/getprod', methods=['GET'])
def get_prod():
    return jsonify({'products': products})

@app.route('/getprodid/<int:task_id>', methods=['GET'])
def get_prod_by_id(task_id):
    # task = [task for task in products if task['id'] == task_id]
    # if len(task) == 0:
    #     abort(404)
    # return jsonify({'task': task[0]})
    for task in products:
        if task['id'] == task_id:
            # if len(task) == 0:
            #     abort(404)
            tasks = [task]
            return jsonify({'task': tasks[0]}),200
            


@app.route('/addprod',methods=['POST'])
def addproduct():
    new_prod = {
        "id":request.json["id"],
        "title":request.json["title"],
        'description':request.json["description"]
    }
    products.append(new_prod)
    return jsonify(products),201

@app.route('/deleteprod/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # task = [task for task in products if task['id'] == task_id]
    # if len(task) == 0:
    #     abort(404)
    # products.remove(task[0])
    # return jsonify({'result': "Deleted"}),200
    for task in products:
        if task['id'] == task_id:
            # if len(task) == 0:
            #     abort(404)
            tasks = [task]
            products.remove(tasks[0])
            return jsonify({'result': "Deleted"}),200
            

if __name__ == '__main__':
    app.run(debug=True)