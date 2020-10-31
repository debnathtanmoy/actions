import unittest
from api import app
from flask import json

# pylint: disable-all
class Test(unittest.TestCase):
    def test_get_product(self):
        response = app.test_client().get(
        '/getproduct')

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)

        expected = [
        {
            "id": "1",
            "name": "mx33"
        },
        {
            "id": "2",
            "name": "mx34"
        },
        {
            "id": "3",
            "name": "mx35"
        },
         {"id" : "007",
            "name" : "bond"}
        ]
        self.assertEqual(data, expected)

    def test_add_product(self):
        response = app.test_client().post(
        '/addproducts',
        
        data=json.dumps({'id': '007', 'name':'bond'}),
        content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 201)

        expected = [
        {
            "id": "1",
            "name": "mx33"
        },
        {
            "id": "2",
            "name": "mx34"
        },
        {
            "id": "3",
            "name": "mx35"
        },
            {"id" : "007",
            "name" : "bond"}
    ]
        self.assertEqual(data, expected)


if __name__ == '__main__':
    unittest.main()
