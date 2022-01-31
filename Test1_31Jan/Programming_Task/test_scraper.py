import unittest

import webscraper

TESTURL = "https://github.coventry.ac.uk/pages/4061CEM-2021OCTJAN/Data/coding/unittest_data.json"

class testScraper(unittest.TestCase):
    """
    Unit-tests for the web-scraper
    """

    def setUp(self):
        """
        Create the class for the scraper.

        This will get called for each individual test
        """
        self.scraper = webscraper.Scraper(TESTURL)

    def test0Total(self):
        self.assertEqual(6, webscraper.total([1,2,3]),msg="Incorrect value given by the 'total' function")

    def test1Mean(self):
        self.assertEqual(2, webscraper.mean([1,2,3]),msg="Incorrect value given by the 'mean' function")

        
    def testFetch(self):
        """ 
        Does the GetURL code work properly.
        """

        data = self.scraper.getData().json()

        #Is the data returned as a dictionary.
        self.assertIsInstance(data, dict, msg="Data returned is not in dictionary format")

    def testData(self):
        """
        Test if the data being returned is as expected
        """

        data = self.scraper.getData()

        jsondata=data.json()
        
        # So we expect that the data has a checksum
        checksum = jsondata.get("checksum", None)
        self.assertTrue(checksum, msg="No Checksum in returned data")

        # And is the checksum data as expected
        self.assertEqual(checksum, [0,5], msg="Checksum data is incorrect")


        # Next we check the data element
        userdata = jsondata.get("data")

        #It has a length of 2
        self.assertEqual(len(userdata), 2, msg="Incorrect number of data items returned")

    def testUserData(self):
        """
        Test the data for a specific user (0)
        """

        data = self.scraper.getData().json()

        # Then get a relevant user
        userdata = data.get("data")
        firstUser = userdata.get("0",None)

        # name should be "User 1"
        self.assertEqual(firstUser["name"], "User 1", msg="Username is incorrect")

        # Text "BAAAA"
        self.assertEqual(firstUser["text"], "BAAAAA", msg="Text is incorrect")

        # Total 15
        self.assertEqual(firstUser["total"], 15, msg="Total Returned is incorrect")

        # Values [1,2,3,4,5]
        self.assertEqual(firstUser["values"], [1,2,3,4,5], msg="Values are Incorrect")


    def testProcess(self):
        """
        Test the processing of the data.
        """

        # We need to get the data first
        data = self.scraper.getData().json()

        # The test the processing of it.
        output = self.scraper.parseData(data)
        
        self._checkProcess(output)
    
    def testRun(self):
        """
        Test the run function
        """

        output = self.scraper.run()

        self._checkProcess(output)

    def _checkProcess(self, theData):
        """
        Helper function to check the processed data

        As both the run / process functions do the same thing, we can have 
        one function that tests the output.  Means that it is consistent
        between the two sets of tests.

        @param theData:  Dictionary of processed data
        """

        #So We should have a message of BB
        self.assertEqual(theData["message"], "BB", msg="Processing of message is incorrect")

        #For the first user we should have a sum of 15 and Average of 3
        firstUser = theData["data"]["0"]
        self.assertEqual(firstUser["sum"], 15, msg="User 1 Sum incorrect")

        #Check the Average is correct, we use almost equal as its a floating
        #point number  
        self.assertAlmostEqual(firstUser["average"], 3, msg="User 1 Average incorrect")

        #For the second user we should have a sum of 25, and average of 5
        secondUser = theData["data"]["1"]

        self.assertEqual(secondUser["sum"], 25, msg="User 1 Sum incorrect")

        #Check the Average is correct, we use almost equal as its a floating
        #point number  
        self.assertAlmostEqual(secondUser["average"], 5 , msg="User 2 Average incorrect")


        #WE also need to check the running total and average
        self.assertEqual(theData["running_average"], 20, msg="Running Average is incorrect")
        self.assertEqual(theData["running_sum"], 40, msg="Running total is incorrect")
