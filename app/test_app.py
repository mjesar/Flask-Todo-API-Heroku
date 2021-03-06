import unittest
import sys, json

from app import app
class TestMain(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"]=True
        self.app=app.test_client()


    def tearDown(self):
        pass

    def test_index_get(self):
        response=self.app.get("/todo/api/v1.0/tasks")
        self.assertEqual(response.status_code,200)

    def test_one_get(self):
        response = self.app.get("/todo/api/v1.0/tasks/4")
        self.assertEqual(response.status_code, 200)
    
    def test_post(self):
        response = self.app.post("/todo/api/v1.0/tasks", data=json.dumps(dict({'title':'checking day', 'description' : 'xyzsdljhljfd', 'complete':'false'})), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        response = self.app.put("/todo/api/v1.0/text/14", data=json.dumps(dict({'title':'hadsgfjshf ', 'description' : 'xyz'})), content_type='application/json')
        self.assertEqual(response.status_code, 200) 

    def test_put1(self):
        response = self.app.put("/todo/api/v1.0/tasks/9" )
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.app.delete("/todo/api/v1.0/tasks/11")
        self.assertEqual(response.status_code, 200)
   

if __name__ == "__main__":
    unittest.main()                
            