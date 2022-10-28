import os 
import json
import unittest
from landing.landing import Wrapper, executeLanding

dirname = os.path.dirname(__file__)

class TestLanding(unittest.TestCase):

    def test_wrapperLoading(self):
        
        # test = Wrapper()
        # self.datasources = test.getDataSources()
        # self.assertIs(type(self.datasources), list, "not working")
        
        pass
        
    def test_deletingWrapper(self):
        # test = Wrapper()
        # test.clean()
        # test.delete()
        
        # wrapper_file = (os.path.exists(os.path.join(dirname, '../landing/wrapper.json')))
        
        # self.assertIs(wrapper_file, False, "Error deliting Wrapper")
        pass
        
    def test_movingToPersistent(self):        
        pass
    
    
    def reading_newDatasource(self):
        pass


if __name__ == '__main__':
    unittest.main()