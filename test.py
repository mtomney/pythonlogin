from app import app
import unittest

#Test that Flask was properly setup
class FlaskTestCase(unittest.TestCase):
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

#Test that the login page properly loads
	def test_login_load(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertTrue(b'Please enter login information' in response.data)

#Test that login is permitted given correct credentials
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post('/login', data=dict(username="user", password="secret"), follow_redirects=True)
		self.assertIn(b'You have been logged in', response.data)
#Test that login is denied given incorrect credentials
	def test_incorrect_login(self):
		tester = app.test_client(self)
		response = tester.post('/login', data=dict(username="wrong", password="wrong"), follow_redirects=True)
		self.assertIn(b'Error: Invalid username or password, please try again.', response.data)
#Test that the user logout function is properly working
	def test_logout(self):
		tester = app.test_client(self)
		tester.post('/login', data=dict(username="user", password="secret"), follow_redirects=True)
		response = tester.get('/logout', follow_redirects=True)
		self.assertIn(b'You have been logged out', response.data)
if __name__ == '__main__':
	unittest.main()