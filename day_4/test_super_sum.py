
"""test suite for super_sum."""

from unittest import TestCase
from super_sum import super_sum 

class SuperSumTestCase(TestCase):
	"""test case for super sum"""


	def test_empty_input(self):
		"""test empty input"""
		self.assertEqual(super_sum(),0)

	def test_sum_of_intergers (self):
		"""Test sum of integers."""

		self.assertEqual(super_sum(1,2,3),6 )
		self.assertEqual(super_sum(-1,1),0)
		self.assertNotEqual(super_sum(10,20,30),100 )


	def test_string_input_returns (self):
		"""
		Test sum of items in a single list"""

		self.assertEqual(super_sum('string', 1,4) ,0)


	def test_sum_of_items_in_list(self):
		"""Test sum of items in a single list."""

		self.assertEqual(super_sum([1,2,3]),6)