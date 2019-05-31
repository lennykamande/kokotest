import json
import unittest
from ... import create_app


class TestRentalApp(unittest.TestCase):
    """docstring for TestRentalApp"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.data = {
              "title": "Religion is all about faith",
              "description": "UPDATED: Some serious and useful content here",
              "days":"3"
        }
        
    def post(self, path='/book', data={}):
        if not data:
            data = self.data

        resp = self.client.post(path='/api/v1/book', data=json.dumps(self.data), content_type='application/json')
        return resp

    def test_renting_a_book(self):
        resp = self.post()
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.json['book_id'])
        self.assertEqual(resp.json['total'], '9')

    def test_getting_all_rentals(self):
        resp = self.client.get(path='/api/v1/book', content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json['total'], '9')

    def test_getting_a_single_rental(self):
        post = self.post()
        int_id = int(post.json['book_id'])
        path = '/api/v1/book/1'
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
unittest.main()