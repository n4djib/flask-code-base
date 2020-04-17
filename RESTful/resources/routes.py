from app import api
from .task import TaskListApi, TaskApi


api.add_resource(TaskListApi, 
    '/todo/api/v1.0/tasks', endpoint='tasks')
api.add_resource(TaskApi, 
    '/todo/api/v1.0/tasks/<int:id>', endpoint='task')











