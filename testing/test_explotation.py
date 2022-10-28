import os 
import json
import unittest

from explotation.processes.explotation import execute_explotation
from explotation.processes.tablepivoting import execute_tablepivoting
from explotation.processes.dataintegration import execute_dataIntegration
from explotation.processes.explotation_infodb import describeExplotationDB



dirname = os.path.dirname(__file__)

class TestTusted(unittest.TestCase):

    def test_zoneExecution(self):
        
        execute_explotation()
        
        self.assertIs(os.path.exists(os.path.join(dirname, '../explotation/explotation.duckdb')), True, "Error creating explotation zone")
    
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