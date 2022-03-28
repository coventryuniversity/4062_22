import unittest

import fixme

class testAlgorithm(unittest.TestCase):
    """
    Unit-tests for the Algorithm
    """

    def testFirst(self):
        """
        The output of the First Iteration should be 1
        """

        output = fixme.fib(1)
        self.assertEqual(output, 1)
        
    def testSecond(self):
        """
        The output of the Second Iteration should be 1
        """
        
        output = fixme.fib(2)
        self.assertEqual(output, 1)
        
    def testSequence(self):
        """
        Given the 4-10 elements are they correct
        """

        answers = [5, 8, 13, 21, 34, 55]

        for x in range(5):
            target = x+5
            
            out = fixme.fib(target)
            print(f"Testing {target},  Result{out}")
            self.assertEqual(out, answers[x])


    def testLinear(self):
        """
        Compare our linear and recusrive outputs
        """

        out = fixme.fib(20)
        linout = fixme.linearFib(20)
        self.assertEqual(out, 6765)
        self.assertEqual(out, linout)
