import unittest

from test_UI import myWidget

from practice import Calc

#
# def main_calc_test(self,Calc):
#     try:
#        pass
#     pass
class TestingPr(unittest.TestCase):
    def setUp(self):
        self.widget = myWidget()


    def test_ui(self):
        self.widget = myWidget()
        self.test_value = ['0.5' , '0.6']
        self.result_test = [None, [0.6 ]]
        self.n = len(self.test_value)
        for i in range (self.n):

            self.assertEqual(self.widget.ui(self.test_value), self.result_test)


    # def tearDown(self):
    #     self.widget.dispose()


if __name__ == '__main__':
    unittest.main()