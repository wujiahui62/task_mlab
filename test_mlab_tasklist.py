import unittest

from mlab_tasklist import TaskList

class TaskList_Test(unittest.TestCase):

    def setUp(self):
        self.tasklist = TaskList()
        self.tasklist.delete_everything()
        for i in range(0,8):
             self.tasklist.create_task("Do something", i%2)

    def tearDown(self):
        #self.tasklist.close()
        pass

    def test_000_do_nothing(self):
        tasklist = self.tasklist
        assert tasklist != None

    def test_001_get_task_list(self):
        tasklist = self.tasklist
        tasks = tasklist.get_list()
        assert len(tasks) > 0
        assert type(tasks) is list
        assert type(tasks[0]) is dict
        task = tasks[0]
        assert "id" in task
        assert "text" in task
        assert "status" in task
        for status in [0,1]:
            tasks = tasklist.get_list(status=status)
            assert len(tasks) > 0
            for task in tasks:
                assert task["status"] == status

    def test_002_get_task(self):
        tasklist = self.tasklist
        tasks = tasklist.get_list()
        assert len(tasks) > 3
        example_task = tasks[3]
        task = tasklist.get_task(example_task["id"])
        for entry in ["id","text","status"]:
            assert task[entry] == example_task[entry]
        task = tasklist.get_task(12390814)
        assert task == None

    def xtest_003_create_task(self):
        tasklist = self.tasklist
        text = "This is a new item"
        status = 1
        tasklist.create_task(text, status)
        for task in tasklist.get_list():
            if task["text"] == text and task["status"] == status:
                assert type(task["id"]) is int 
                return
        assert False, "created task was not found"

    def test_004_update_text(self):
        tasklist = self.tasklist
        tasks = tasklist.get_list()
        assert len(tasks) > 0
        id = tasks[0]["id"]
        tasklist.update_text(id,"Do something else")
        tasks = tasklist.get_list()
        for task in tasks:
            if task["id"] == id:
                assert task["text"] == "Do something else"
        
    def test_005_update_status(self):
        tasklist = self.tasklist
        tasks = tasklist.get_list()
        assert len(tasks) > 0
        id = tasks[0]["id"]
        for status in [0,1]:
            tasklist.update_status(id,status)
            tasks = tasklist.get_list()
            for task in tasks:
                if task["id"] == id:
                    assert task["status"] == status

    def test_006_delete(self):
        tasklist = self.tasklist
        tasks = tasklist.get_list()
        assert len(tasks) > 2
        id = tasks[1]["id"]
        tasklist.delete_task(id)
        tasks = tasklist.get_list()
        for task in tasks:
            if task["id"] == id:
                assert False, "Task was not deleted"

if __name__ == "__main__":
    unittest.main(verbosity=2)

