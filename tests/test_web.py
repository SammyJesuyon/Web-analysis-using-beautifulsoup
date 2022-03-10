import unittest
from src.web_analysis import WebAnalysis
from unittest import mock

class TestWebAnalysis(unittest.TestCase):

   def setUp(self):
      web_analysis = WebAnalysis()
      self.web_scrape_test = web_analysis.scrape_web
      self.clean_data_test = web_analysis.clean_data
      self.sorted_data_test = web_analysis.sort_data

   def test_web_scrape(self):
      url = 'https://python.org/'
      result = self.web_scrape_test(url)
      self.assertTrue(result)

   def test_web_scrape_dtype(self):
      url = 'https://python.org/'
      result = self.web_scrape_test(url)
      self.assertIsInstance(result, object)

   def test_clean_data(self):
      url = 'https://python.org/'
      test = self.web_scrape_test(url)
      result = self.clean_data_test(test)
      self.assertTrue(result)

   @mock.patch("builtins.print", return_value=None)
   def test_sorted_data(self, mocker):
      url = 'https://python.org/'
      data1 = self.web_scrape_test(url)
      data2 = self.clean_data_test(data1)
      result = self.sorted_data_test(data2)
      self.assertTrue(result)

   @mock.patch("builtins.print", return_value=None)
   def test_sorted_data_dtype(self, mocker):
      url = 'https://python.org/'
      data1 = self.web_scrape_test(url)
      data2 = self.clean_data_test(data1)
      result = self.sorted_data_test(data2)
      self.assertIsInstance(result, dict)
