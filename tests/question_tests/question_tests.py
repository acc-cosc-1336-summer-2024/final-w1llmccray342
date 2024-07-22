#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions

from src.question_c.question_c import grab_lowest_nums, grab_highest_nums, grab_avg_nums, grab_total_nums

class Test_Config(unittest.TestCase):

    def test_question_c_grab_lowest_nums(self):
        nums_to_test = [1, 2, 3, 4, 5]
        self.assertEqual(1, grab_lowest_nums(nums_to_test))

    def test_question_c_grab_highest_nums(self):
        nums_to_test = [1, 2, 3, 4, 5]
        self.assertEqual(5, grab_highest_nums(nums_to_test))


