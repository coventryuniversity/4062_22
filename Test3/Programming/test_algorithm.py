import unittest

import fixme

class testScraper(unittest.TestCase):
    """
    Unit-tests for the bubblesort
    """

    def test_nosort(self):
        """
        Test if a list that doesn't need sorting is correct
        """

        #Setup the Data
        data = [1,2,3,4,5,6]      # Input
        expected = [1,2,3,4,5,6]  # Expected Value

        #Sort the Thing
        out = fixme.bubblesort(data)

        #Test that the expected == output
        self.assertEqual(expected, out)


    def test_revrse(self):
        """
        Does the sort fully revese the list
        """
        #Setup the Data
        data = [6,5,4,3,2,1]      # Input
        expected = [1,2,3,4,5,6]  # Expected Value

        #Sort the Thing
        out = fixme.bubblesort(data)

        #Test that the expected == output
        self.assertEqual(expected, out)


    
    def test_partial(self):
        """
        Test that reversing a list works
        """

        #Setup the Data
        data = [1,3,2,4,6,5]      # Input
        expected = [1,2,3,4,5,6]  # Expected Value

        #Sort the Thing
        out = fixme.bubblesort(data)

        #Test that the expected == output
        self.assertEqual(expected, out)

        
