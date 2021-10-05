import unittest

def divide(x,y):
       
    return(x/y)

    class Divide(unittest.testCase):

         def test(self):

             self.assertEqual(divide(6,2),3)

if __name__== '__main__':
    unittest.main()

