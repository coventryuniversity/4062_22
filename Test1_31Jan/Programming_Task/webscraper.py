"""
Simple program that will scrape a website and do some calculations
"""

import logging

import requests


def total(values):
    acc=0
    for v in range(values):
        acc+=v
    return acc

def mean(values):
    return len(values)/total(values)

class Scraper:
    def __init__(self, URL):
        """
        Create a new scraper object

        @param URL:  Web address to get data from
        """

        self.URL = URL
        self.log = logging.getLogger(__name__)
        self.log.debug("Scraper for %s created", self.URL)


    def getData(self):
        """
        This function will use the requests library and return a request object

        @returns: request object
        """
        self.log.debug("Fetching data")
        
        r = requests.get(self.URL)
        self.log.debug(r.json())
        return r
        
    def parseData(self, theData):
        """
        Function to process JSON formatted data

        @param theData:  Data to process
        @returns: A Summary of the data 
        """
        self.log.debug("Processing data")

        #Get the list of users
        userdict = theData["data"]
        checksum = theData["checksum"]
        self.log.debug("Checksum is %s", checksum)
        processed = []
        message = ""
        
        userList = theData["data"]

        runningSum = 0
        #runningAverage = 0  #To Break it

        idx = 0 #Keep track of where we are in the checksum
        for item in userList.values():
            #Calculate the average value
            self.log.debug("--> User is %s", item["name"])
            theSum = total(item["values"])
            theAvg = mean(item["values"])
            self.log.debug("\t Sum %d", theSum)
            self.log.debug("\t Avg %f", theAvg)
            #Get the Secret Flag
            checkIdx = checksum[idx]   
            message += item["text"][checkIdx]

            item["sum"] = theSum
            item["average"] = theAvg

            runningSum += theSum
            #Make sure we increment the message
            idx += 1
            

        #And our Running totals
        theData["running_sum"] = runningSum
        theData["running_average"] = runningSum / idx
        
        theData["message"] = message
        self.log.debug("Message is %s",message)
        return theData



    def run(self):
        """
        Run the program
        """
        self.log.debug("Running")

        #Fetch the data
        data = self.getData()

        #Process it
        output = self.parseData(data.json())

        return output


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    #webscraper =
    #Scraper("https://github.coventry.ac.uk/pages/4061CEM-2021OCTJAN/Data/coding/testdata.json")
    webscraper = Scraper("https://github.coventry.ac.uk/pages/4061CEM-2021OCTJAN/Data/coding/testdata.json")
    output = webscraper.run()

    #Print the ouutput
    print("{0}".format("-"*40))
    print("Message is {0}".format(output["message"]))

    #import pprint
    #pprint.pprint(output)
