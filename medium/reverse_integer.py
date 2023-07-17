# source: https://leetcode.com/problems/reverse-integer/?envType=featured-list&envId=top-interview-questions


def reverse(x):
    if x < 0:
        res = -1 * int(str(x)[1:][::-1])
    elif x == 0:
        res = 0
    else:
        res = int(str(x)[::-1])
    
    if res < -2**31 or res > 2**31 - 1:
        return 0
    else:
        return res


print(reverse(123))
print(reverse(-123))
print(reverse(1200))
print(reverse(-1200))