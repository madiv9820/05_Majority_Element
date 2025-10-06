import unittest
from timeout_decorator import timeout
from Solution import Solution

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = (
            ([3,2,3], 3),
            ([2,2,1,1,1,2,2], 2)
        )
        self.__solution = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_0(self):
        nums, expectedResult = self.__testcases[0]
        actualResult = self.__solution.majorityElement(nums = nums)
        self.assertEqual(actualResult, expectedResult)

    @timeout(0.5)
    def test_case_1(self):
        nums, expectedResult = self.__testcases[1]
        actualResult = self.__solution.majorityElement(nums = nums)
        self.assertEqual(actualResult, expectedResult)

if __name__ == '__main__': unittest.main()