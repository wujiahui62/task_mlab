from pymongo import MongoClient

class TaskList():

    db = None

    def __init__(self):
        self.client = MongoClient("mongodb://jiahui:password@ds141406.mlab.com:41406/task_db")
        self.db = self.client['task_db']

    def get_list(self, status=None):
        if status==None:
            where = {}
        else:
            where = {"status":status}
        items = self.db.todo.find(where,{
                            "_id":False,
                            "id":True,
                            "text":True,
                            "status":True,
                            })
        items = list(items)
        return items

    def get_task(self, id):
        items = self.db.todo.find({"id" : id}, {
                            "_id":False,
                            "id":True,
                            "text":True,
                            "status":True,
                            })
        items = list(items)
        if len(items) == 0:
            return None
        return items[0]
    
    def create_task(self, text, status):
        id = -1
        items = self.db.todo.find({},{
                            "_id":False,
                            "id":True,
                            })
        for item in items:
            if item["id"] > id:
                id = item["id"]
        self.db.todo.insert_one(
               { 
                    "id":id+1,
                    "text":text, 
                    "status":status
                })

    def update_text(self, id, text):
        self.db.todo.update_one({"id":id},{"$set":{"text":text}})

    def update_status(self, id, status):
        self.db.todo.update_one({"id":id},{"$set":{"status":status}})

    def delete_everything(self):
        self.db.todo.delete_many({})

    def delete_task(self, id):
        self.db.todo.delete_one({"id":id})
