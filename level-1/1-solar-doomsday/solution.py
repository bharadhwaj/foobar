import math

def solution(area):
    '''
    Problem Name: Solar Doomsday
    Author: Bharadhwaj C N (bharadhwaj10@gmail.com)
    Statement: https://github.com/bharadhwaj/foobar/tree/main/level-1/1-solar-doomsday#readme
    '''
    panel_sizes = []
    while area > 0:
        max_square_side = int(math.sqrt(area))
        max_square_area = max_square_side ** 2
        panel_sizes.append(max_square_area)
        area -= max_square_area

    return panel_sizes


test_case_1 = 12
answer_1 = [9, 1, 1, 1]

test_case_2 = 15324
answer_2 = [15129, 169, 25, 1]


try:
    assert solution(test_case_1) == answer_1
    assert solution(test_case_2) == answer_2
    print("SUCCESS!")
except AssertionError:
    print("Oops! Some error occurred!")