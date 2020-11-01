import unittest
from api import app
from flask import json

# flake8: noqa
class Test(unittest.TestCase):
    
    def test_get_prod(self):
        response = app.test_client().get(
        '/getprod')

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)


    def test_get_prod_by_id(self):
        response = app.test_client().get(
        '/getprodid/1')

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)

        expected = {
        "task": {
            "description": "effective for small ICUS",
            "id": 1,
            "title": "mx33"
        }
        }
        self.assertEqual(data, expected)

    def test_add_product(self):
        response = app.test_client().post(
        '/addprod',
        
        data=json.dumps({ "id":"3","title": "mx66","description":"godd for large size ICUS"}),
        content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 201)

        expected = [
    {
        "description": "effective for small ICUS",
        "id": 1,
        "title": "mx33"
    },
    {
        "description": "effective for medium sized ICUS",
        "id": 2,
        "title": "mx53"
    },
    {
        "description": "godd for large size ICUS",
        "id": "3",
        "title": "mx66"
    }
]
        self.assertEqual(data, expected)
    
    def test_delete_product(self):
        response = app.test_client().delete(
        '/deleteprod/2')
        
        # data=json.dumps({ "id":"3","title": "mx66","description":"godd for large size ICUS"}),
        # content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)

        expected = {
        "result": "Deleted"
        }
        self.assertEqual(data, expected)
    
    def test_update_product(self):
        response = app.test_client().put(
        '/updateprod/1',
        
        data=json.dumps({ "id":"3","title": "mx66","description":"godd for large size ICUS"}),
        content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)

        expected = {
        'task': "updated"
        }
        self.assertEqual(data, expected)


if __name__ == '__main__':
    unittest.main()
