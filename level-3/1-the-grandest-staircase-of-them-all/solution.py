def solution(n):
    '''
    Problem Name: The Grandest Staircase of them all
    Author: Bharadhwaj C N (bharadhwaj10@gmail.com)
    Statement: https://github.com/bharadhwaj/foobar/tree/main/level-3/1-the-grandest-staircase-of-them-all#readme
    '''
    possible_ways = [1] + ([0] * n)

    for bricks_used in range(1, n + 1):
        for bricks_left in range(n, bricks_used - 1, -1):
            possible_ways[bricks_left] += possible_ways[bricks_left - bricks_used]
    return possible_ways[-1] - 1


test_case_0 = 3
answer_0 = 1

test_case_1 = 4
answer_1 = 1

test_case_2 = 5
answer_2 = 2

test_case_3 = 200
answer_3 = 487067745


try:
    assert solution(test_case_0) == answer_0
    assert solution(test_case_1) == answer_1
    assert solution(test_case_2) == answer_2
    assert solution(test_case_3) == answer_3
    print("SUCCESS!")
except AssertionError:
    print("Oops! Some error occurred!")