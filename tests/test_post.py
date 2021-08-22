import unittest
import json
from app import create_app, db

class PostTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.post = {'name': 'Test post 123'}
        """
        Bind to current context and create the tables
        """
        with self.app.app_context():
            db.create_all()

    def test_create_post(self):
        """
        Create a post (POST request)
        """
        res = self.client().post('/posts/', data=self.post)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Test post', str(res.data))

    def test_get_all_posts(self):
        """
        Get a post from all posts (GET request)
        """
        res = self.client().post('/posts/', data=self.post)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/posts/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Test post', str(res.data))

    def test_get_post_by_id(self):
        """
        Get a post by id (GET request)
        """
        rv = self.client().post('/posts/', data=self.post)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/posts/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Test post', str(result.data))

    def test_edit_post(self):
        """
        Edit a post (PUT request)
        """
        rv = self.client().post(
            '/posts/',
            data={'name': 'Test post 456'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/posts/1',
            data={
                "name": "Second test post 456"
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/posts/1')
        self.assertIn('Second test post', str(results.data))

    def test_delete_post(self):
        """
        Delete a post (DELETE request)
        """
        rv = self.client().post(
            '/posts/',
            data={'name': 'Test post 789'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/posts/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/posts/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """
        Teardown initialised variables and drop all tables
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == "__main__":
    unittest.main()