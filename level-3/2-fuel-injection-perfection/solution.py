def solution(n):
    '''
    Problem Name: Fuel Injection Perfection
    Author: Bharadhwaj C N (bharadhwaj10@gmail.com)
    Statement: https://github.com/bharadhwaj/foobar/tree/main/level-3/2-fuel-injection-perfection#readme
    '''
    n = int(n)
    count = 0

    while n > 1:
        count += 1
        if n % 2 == 0:
            n //= 2
        elif n == 3 or n % 4 == 1:
            n = (n - 1) // 2
            count += 1
        else:
            n = (n + 1) // 2
            count += 1

    return count


# Recursive (Didn't work, assuming because of recursion count limit)
# def solution(n):
#     n = int(n)
#     if n <= 3:
#         return n - 1
#       
#     if n % 2 == 0:
#         return solution(n//2) + 1
#
#     if n % 4 == 1:
#         return solution((n-1)//2) + 2
#
#     return solution((n+1)//2) + 2


test_case_0 = '15'
answer_0 = 5

test_case_1 = '4'
answer_1 = 2


try:
    assert solution(test_case_0) == answer_0
    assert solution(test_case_1) == answer_1
    print("SUCCESS!")
except AssertionError:
    print("Oops! Some error occurred!")