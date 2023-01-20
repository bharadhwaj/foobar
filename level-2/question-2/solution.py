def solution(s):
    '''
    Problem Name: En Route Salute
    Author: Bharadhwaj C N (bharadhwaj10@gmail.com)
    Statement: https://github.com/bharadhwaj/foobar/tree/main/level-2/question-2#readme
    '''
    people_walking_to_right = 0
    salute_count = 0
    for tile in s:
        if tile == ">":
            people_walking_to_right += 1
        elif tile == "<":
            salute_count += people_walking_to_right * 2
        
    return salute_count


test_case_0 = "-->-><-><-->-"
answer_0 = 10

test_case_1 = ">----<"
answer_1 = 2

test_case_2 = "<<>>-<"
answer_2 = 4


try:
    assert solution(test_case_0) == answer_0
    assert solution(test_case_1) == answer_1
    assert solution(test_case_2) == answer_2
    print("SUCCESS!")
except AssertionError:
    print("Oops! Some error occurred!")