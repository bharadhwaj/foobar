def solution(l):
    '''
    Problem Name: Find the Access Codes
    Author: Bharadhwaj C N (bharadhwaj10@gmail.com)
    Statement: https://github.com/bharadhwaj/foobar/tree/main/level-3/3-find-the-access-codes#readme
    '''
    division_count = [0] * len(l)
    count = 0

    for j in range(len(l)):
        for i in range(j):
            if l[j] % l[i] == 0:
                division_count[j] += 1
                count += division_count[i]

    return count

test_case_0 = [1, 1, 1]
answer_0 = 1

test_case_1 = [1, 2, 3, 4, 5, 6]
answer_1 = 3


try:
    assert solution(test_case_0) == answer_0
    assert solution(test_case_1) == answer_1
    print("SUCCESS!")
except AssertionError:
    print("Oops! Some error occurred!")