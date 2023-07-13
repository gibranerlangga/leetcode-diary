# source: https://leetcode.com/problems/roman-to-integer/?envType=featured-list&envId=top-interview-questions
# Given a roman numeral, convert it to an integer.

def romanToInt(s):
    # build roman dictionary
    roman_dict = {  'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
    
    # initialize result
    result = 0

    # iterate through string
    for i in range(len(s)):
        # if the current roman numeral is less than the next, subtract
        if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
            result -= roman_dict[s[i]]
        # else add
        else:
            result += roman_dict[s[i]]

    return result


roman = "III"
roman1 = "IV"
roman2 = "IX"
roman3 = "LVIII"
roman4 = "MCMXCIV"

print(romanToInt(roman1))
print(romanToInt(roman2))
print(romanToInt(roman3))
print(romanToInt(roman4))