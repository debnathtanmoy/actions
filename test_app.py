import unittest
import app

class Test(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(app.hello_world(),'hello world')
        

if __name__ == '__main__' :
    unittest.main()