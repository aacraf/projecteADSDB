import os
import unittest

from DataManagmentBackbone.explotation.processes.explotation import execute_explotation

dirname = os.path.dirname(__file__)

class TestTusted(unittest.TestCase):

    def test_zoneExecution(self):
        
        execute_explotation()
        
        self.assertIs(os.path.exists(os.path.join(dirname, '../DataManagmentBackbone/explotation/explotation.duckdb')), True, "Error creating explotation zone")
    
    def test_tablePivoting(self):
        pass
    
    def test_dataIntegration(self):
        pass
    
    def test_profilingGenerator(self):
        pass

    def test_databaseDescription(self):    
        pass 
if __name__ == '__main__':
    unittest.main()