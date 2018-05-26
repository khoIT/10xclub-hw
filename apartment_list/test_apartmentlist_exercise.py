import unittest
from 10xclub-hw.apartmentlist_exercise import group_randomizer

class TestGroupRandomizer(unittest.TestCase):
    def test_group_randomizer_should_work_with_list_of_6_elements(self):
        test_name_list = ['a','b','c','d','e','f']
        grouping = group_randomizer(test_name_list)
        self.assertEqual(len(grouping), 2)

if __name__ == '__main__':
    unittest.main()
