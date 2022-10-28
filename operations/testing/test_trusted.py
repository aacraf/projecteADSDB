import os 
import json
import unittest


from trusted.combine_versions import execute_combine_versions
from trusted.data_quality.missing import executeMissingData
from trusted.data_quality.outliers import execute_outliers
from trusted.data_quality.profiling import execute_profiling
from trusted.trusted_infodb import describeTrustedDB


dirname = os.path.dirname(__file__)

class TestTusted(unittest.TestCase):

    def test_zoneExecution(self):
        
        execute_combine_versions()
        
        self.assertIs(os.path.exists(os.path.join(dirname, '../trusted/trusted.duckdb')), True, "Error creating trusted zone")
    
    def test_missingDataMethod(self):
        pass
    
    def test_outlierRemovalMethod(self):
        pass
    
    def test_profilingGenerator(self):
        pass
    
    def test_databaseDescription(self):    
        pass
    

if __name__ == '__main__':
    unittest.main()