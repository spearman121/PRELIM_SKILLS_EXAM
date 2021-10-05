import unittest

def add(x,y):
       
    return(x+y)

    class Add(unittest.testCase):

         def test(self):

             self.assertEqual(add(6,2),8)

if __name__== '__main__':
    unittest.main()