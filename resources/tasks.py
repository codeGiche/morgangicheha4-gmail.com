from main import Resource, api, fields

# namespace
ns_tasks = api.namespace("tasks", description="All tasks regarding tasks")


task_list = [
    {"id": 1, "title": "learn flask-restx", "description": "learn the basices"},
    {"id": 2, "title": "learn vue js", "description": "learn the basices"},
    {"id": 3, "title": "learn docker", "description": "learn the basices"},
]
# models
task_model = api.model(
    "Task", {"title": fields.String(), "description": fields.String()}
)


@ns_tasks.route("")
class TasksList(Resource):
    def get(self):
        """ use this ednpoint to get a list of tasks """
        return task_list, 200

    @api.expect(task_model)
    def post(self):
        """ use this ednpoint to add new tasks """

        data = api.payload
        data["id"] = len(task_list) + 1
        task_list.append(data)

        return data, 201


@ns_tasks.route("/<int:id>")
class Task(Resource):
    def get(self, id):
        """retrieve a task by it's id"""
        return next(filter(lambda x: x["id"] == id, task_list)), 200


    @api.expect(task_model )
    def put(self, id):
        """edit a task by it's id"""
        data = api.payload
        task = next(filter(lambda x: x["id"] == id, task_list), None)
        if task:
            if u'title' in data:
                task["title"]= data["title"]

            if u'description' in data:
                task["description"]= data["description"]
                return task,201 #Created

        else:
            return {"message": "task not found"},404 
        

    def delete(self, id):
        """use this endpoint to delete a task"""
        # query  tasl_list for that id
        # print(next( filter(( lambda x:x["id"]==id ), task_list) )) #this function queries for the object to be deleted and finds the first one
        to_delete = next(filter((lambda x: x["id"] == id), task_list), None)
        if to_delete:
            task_list.remove(to_delete)
            return {"message": "Task deleted"}, 201
        else:
            return {"message": "Task not found"}, 404

