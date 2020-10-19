from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS


app = Flask(__name__)
app.config['MONGO_URI']='mongodb+srv://userMaster:root@cluster0.achiw.mongodb.net/pythonreactdb'
mongo = PyMongo(app)

CORS(app)
#cone
db = mongo.db.users

#dasd
#Creat usuarios
@app.route('/users', methods=['POST'])
def createUser():
    id=db.insert({
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    })
    return jsonify(str(ObjectId(id)))


#Obtener ususarios
@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for doc in db.find():
        users.append({
          '_id': str(ObjectId(doc['_id'])) ,
           'name': doc['name'],
           'email': doc['email'],
           'password': doc['password']
        })
    return jsonify(users)


#Obtener un solo user por id
@app.route('/users/<id>', methods=['GET'])
def getUser(id):
    user = db.find_one({ '_id': ObjectId(id) })
    print(id)
    return jsonify({
          '_id': str(ObjectId(user['_id'])) ,
           'name': user['name'],
           'email': user['email'],
           'password': user['password']
        })

#borrar usr por id
@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    db.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'user deleted'})

#Actualizar 
@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    db.update_one({'_id': ObjectId(id)}, {'$set': {
        'name' : request.json['name'],
        'email' : request.json['email'],
        'password' : request.json['password']
    }})
    return jsonify({'msg': 'user updated'})

if __name__ == "__main__":
    app.run(debug=True)
