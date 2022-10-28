import os 
import json
import unittest
from formatted.formatted import executeformatted
import pathlib as pl

dirname = os.path.dirname(__file__)

class TestFormatted(unittest.TestCase):

    def test_zoneExecution(self):
        executeformatted()
        
        path = pl.Path(os.path.join(dirname, '../formatted/formatted.duckdb'))
        #self.assertIs(os.path.exists(os.path.join(dirname, '../formatted/formatted.duckdb')), True, "Error creating formatted zone")
        
        self.assertEquals((str(path), path.is_file()), (str(path), True), msg="Error executing zone")

if __name__ == '__main__':
    unittest.main(verbosity=2)