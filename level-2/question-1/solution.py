def decimal_to_base(num, base):
    num = int(num)
    if num == 0:
        return "0"

    digits = []
    while num:
        digits.insert(0, str(num % base))
        num //= base

    return "".join(digits)


def subtraction_in_base(num1, num2, base):
    if base == 10:
        return str(int(num1) - int(num2))

    return decimal_to_base(str(int(num1, base) - int(num2, base)), base)

def solution(n, b):
    '''
    Problem Name: Hey, I Already Did That!
    Author: Bharadhwaj C N (bharadhwaj10@gmail.com)
    Statement: https://github.com/bharadhwaj/foobar/tree/main/level-2/question-1#readme
    '''
    minions_ids = []
    k = len(n)
    while n not in minions_ids:
        minions_ids.append(n)
        x = "".join(sorted(str(n), reverse=True))
        y = "".join(sorted(str(n)))
        z = subtraction_in_base(x, y, b).zfill(k)
        n = z

    return len(minions_ids) - minions_ids.index(n)    


test_case_1 = {"n": "1211", "b": 10}
answer_1 = 1

test_case_2 = {"n": "210022", "b": 3}
answer_2 = 3


try:
    assert solution(**test_case_1) == answer_1
    assert solution(**test_case_2) == answer_2
    print("SUCCESS!")
except AssertionError:
    print("Oops! Some error occurred!")