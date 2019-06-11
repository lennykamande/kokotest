import json
import unittest
from ... import create_app


class TestRentalApp(unittest.TestCase):
    """docstring for TestRentalApp"""

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.data = {
              "title": "Religion is all about faith",
              "description": "Novel",
              "days": 3,
              "books" : 2
        }
        self.data2 = {
              "title": "Songs of ice and fire",
              "description": "Fiction",
              "days": 6,
              "books" : 2
        }
        self.data3 = {
              "title": "A dance of dragons",
              "description": "Regular",
              "days": 6,
              "books" : 2
        }
        
    def post(self, path='/book', data={}):
        if not data:
            data = self.data

        resp = self.client.post(path='/api/v2/book', data=json.dumps(self.data), content_type='application/json')
        return resp

    def test_renting_a_novel_book(self):
        resp = self.post()
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.json['rental_id'], 1)
        self.assertTrue(resp.json['Total'], 15)
    
    def test_renting_a_fiction_book(self):
        response = self.client.post(path='/api/v2/book', data=json.dumps(self.data2), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json['rental_id'], 2)
        self.assertTrue(response.json['Total'], 48)

    def test_renting_a_regular_book(self):
        response = self.client.post(path='/api/v2/book', data=json.dumps(self.data3), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json['rental_id'], 3)
        self.assertTrue(response.json['Total'], 48)
        
    def test_getting_all_rentals(self):
        resp = self.client.get(path='/api/v2/book', content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_getting_a_single_rental(self):
        post = self.post()
        int_id = int(post.json['rental_id'])
        path = '/api/v2/book/1'
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_deleting_a_rental(self):
        post = self.client.post(path='/api/v2/book', data=json.dumps(self.data), content_type='application/json')
        int_id = int(post.json['rental_id'])
        path = '/api/v2/book/{}'.format(int_id)
        response = self.client.delete(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()