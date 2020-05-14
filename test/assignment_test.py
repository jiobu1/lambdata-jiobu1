#assignment_test.py

import unittest
from pandas import DataFrame

from my_lambdata.assignment import add_state_names 
# add __init__.py
# python -m my_lambdata/assignment.py (to run)

#OBJECTIVE:test the add_state_names() finction from teh my_lambdata package

class TestAssignment(unittest.TestCase):
    
    def test_add_state_names(self):
        df = DataFrame({'abbrev': ["CA", "CO", "CT", "DC", "TX"]})
        self.assertEqual(list(df.columns), ['abbrev'])

        result = add_state_names(df)
        self.assertEqual(list(result.columns), ['abbrev', 'name'])

        #after we invoke the function:
        #expect taht it has one more column and the same number of rows, after we invoke the function
        #expect that certain column names exist before and certain col names after

        breakpoint()
        #df.columns
        #self.assertEqual("foo".upper(), "FOO")

if __name__ == "__main__":
    unittest.main()
