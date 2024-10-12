import pytest

from leetcode_python.problems.problem41 import Solution as Solution41
from leetcode_python.problems.problem442 import Solution as Solution442
from leetcode_python.problems.problem448 import Solution as Solution448
from leetcode_python.problems.problem287 import Solution as Solution287


@pytest.mark.parametrize('test_input,expected', [
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1),
])
def test_first_missing_positive(test_input: list[int], expected: int):
    solution = Solution41()
    assert solution.firstMissingPositive(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ([4,3,2,7,8,2,3,1], [2,3]),
    ([1,1,2], [1]),
    ([1], []),
])
def test_find_duplicates(test_input: list[int], expected: int):
    solution = Solution442()
    assert solution.findDuplicates(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ([4,3,2,7,8,2,3,1], [5,6]),
    ([1,1], [2]),
])
def test_find_disappeared_number(test_input: list[int], expected: int):
    solution = Solution448()
    assert solution.findDisappearedNumbers(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ([1,3,4,2,2], 2),
    ([3,1,3,4,2], 3),
    ([3,3,3,3,3], 3),
])
def test_find_one_duplicate(test_input: list[int], expected: int):
    solution = Solution287()
    assert solution.findDuplicate(test_input) == expected
