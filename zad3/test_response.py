import unittest

from response import check_parameters_count
from response import MyCustomException
from response import checkurl
from response import getResonse

class TestParametersCount(unittest.TestCase):
    def test_count_no_params(self):
       with self.assertRaises(MyCustomException) as ctx:
           check_parameters_count([1])
       self.assertEqual("No parameters! Please provide URL", str(ctx.exception))

    def test_count_to_many_params(self):
       with self.assertRaises(MyCustomException) as ctx:
           check_parameters_count([3,"param",64,98])
       self.assertEqual("To many parameters!", str(ctx.exception))

    def test_count_exact_2_params(self):
        check_parameters_count([3,"param"])
      
class TestUrl(unittest.TestCase):
    def test_invalid_url(self):
        with self.assertRaises(MyCustomException) as ctx:
            checkurl("dupa")
        self.assertEqual("URL is not valid", str(ctx.exception))
    def test_valid_url(self):
        checkurl("http://google.com")
    










