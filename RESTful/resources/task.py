from flask_restful import Resource, reqparse

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

class TaskListApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title', type=str, required=True,
            help='No task title provided', location='json')
        self.reqparse.add_argument(
            'description', type=str, default="", location='json')
        super(TaskListApi, self).__init__()

    def get(self):
        return tasks

    def post(self):
        args = self.reqparse.parse_args()
        return {"message": "posted...",
            "title": args['title']}

class TaskApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title', type = str, location = 'json')
        self.reqparse.add_argument(
            'description', type = str, location = 'json')
        self.reqparse.add_argument(
            'done', type = bool, location = 'json')
        super(TaskApi, self).__init__()

    def get(self, id):
        tsks = list(filter(lambda task: task['id'] == id, tasks))
        return tsks[0] if len(tsks) else None
        # return *list(filter(lambda task: task['id'] == id, tasks))


    def put(self, id):
        pass

    def delete(self, id):
        pass

