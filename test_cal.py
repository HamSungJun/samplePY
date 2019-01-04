import xmlrunner.unittest as unittest
import random
import cal as cal
import xmlrunner

def randNum():
    randAB = [(random.randint(0, 300)+random.random()),(random.randint(0, 300)+random.random())]

    return randAB

class TesterClass(unittest.TestCase):

    def setUp(self):
        print("\nsetUp()...")
    def tearDown(self):
        print("\n...tearDown")

    def test_add(self):

        for i in range(1 , 1000):
            
            randAB = randNum()
            result = cal.add(randAB[0], randAB[1])
            self.assertEqual(result , randAB[0]+randAB[1])

    def test_sub(self):

        for i in range(1, 1000):

            randAB = randNum()
            result = cal.sub(randAB[0], randAB[1])
            self.assertEqual(result, randAB[0]-randAB[1])

    def test_mul(self):

        for i in range(1 , 1000):

            randAB = randNum()
            result = cal.mul(randAB[0], randAB[1])
            self.assertEqual(result , randAB[0]*randAB[1])

    def test_div(self):

        for i in range(1 , 1000):

            randAB = randNum()
            if(i == 1):
                randAB[1] = 0
            
            with self.assertRaises(ZeroDivisionError):
                int(randAB[0]) / int(randAB[1])
            self.assertEqual(cal.div(randAB[0], randAB[1]), randAB[0] / randAB[1])

if __name__ == '__main__':
    unittest.main(
    testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
    # these make sure that some options that are not applicable
    # remain hidden from the help menu.
    failfast=False, buffer=False, catchbreak=False)

