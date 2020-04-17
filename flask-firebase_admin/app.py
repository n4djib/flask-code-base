### Building a Flask(Python) CRUD API with Cloud Firestore(Firebase) 
#    and Deploying on Cloud Run
# https://medium.com/google-cloud/building-a-flask-python-crud-api-with-cloud-firestore-firebase-and-deploying-on-cloud-run-29a10c502877

### Snapshot
# https://rakibul.net/fb-realtime-db-python
# https://stackoverflow.com/questions/56513181/firestore-listeners-for-python

# TODO: add snapshot + socketio(maybe) or just print in Console 





# Required Imports
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask App
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')

@app.route('/add', methods=['POST'])
def create():
    """ create() : e.g. json={'id': '1', 'title': 'Write a blog post'} """
    try:
        id = request.json['id']
        todo_ref.document(id).set(request.json)
        return jsonify({"success": True, "message": "added document id: "+str(id)}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/list', methods=['GET'])
def read():
    """ read() 
        todo : Return document that matches query ID
        all_todos : Return all documents """
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in todo_ref.stream()]
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/get', methods=['GET'])
def get():
    """ get() : e.g. json={'id': '1'} """
    try:
        id = request.json['id']
        todo = todo_ref.document(id).get()
        return jsonify(todo.to_dict()), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/update', methods=['POST', 'PUT'])
def update():
    """ update() : e.g. json={'id': '1', 'title': 'Write a blog post today'} """
    try:
        id = request.json['id']
        todo_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """ delete() : Delete a document from Firestore collection """
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        todo_ref.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=port)
