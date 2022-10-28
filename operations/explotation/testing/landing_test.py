import os 
import json
import unittest
from landing.landing import Wrapper, executeLanding


class TestLanding(unittest.TestCase):

    def test_wrapperCreation(self):
        
        test = Wrapper()
        datasources = test.getDataSources()
        
        self.assertEqual(type(datasources), 'list', "Error")

if __name__ == '__main__':
    unittest.main()