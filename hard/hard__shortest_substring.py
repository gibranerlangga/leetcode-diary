def shortest_substring(char_list, string):
    elements = set(char_list)
    shortest_substring = None
    
    ## getting all potential options
    substrings = []
    
    for i in range(len(string)):
        for j in range(i, len(string)):
            temp_substr = string[i:j+1]
            ## check if temp_substr has all chars inside elements
            if set(temp_substr).issuperset(elements):
                substrings.append(temp_substr)
    
    ## evaluate all options to get the shortest one
    smallest_length = float('inf')

    for substring in substrings:
        if len(substring) < smallest_length:
            smallest_length = len(substring)
            shortest_substring = substring

    return shortest_substring


def better_shortest_substring(char_list, string):
    target_counts = {i: 1 for i in char_list}
    required_count = len(char_list)
    shortest_substring = None
    smallest_length = float('inf')

    left = right = 0
    window_counts = {}

    while right < len(string):
        char_right = string[right]
        window_counts[char_right] = window_counts.get(char_right, 0) + 1
        if char_right in target_counts and window_counts[char_right] <= target_counts[char_right]:
            required_count -= 1

        # when subtring containing all the elements are in place, do steps below
        while required_count == 0:
            if right - left + 1 < smallest_length:
                smallest_length = right - left + 1
                shortest_substring = string[left:right+1]
            
            if len(shortest_substring) == required_count:
                return shortest_substring

            char_left = string[left]
            window_counts[char_left] -= 1
            if char_left in target_counts and window_counts[char_left] < target_counts[char_left]:
                required_count += 1
            left += 1
        right += 1

    return shortest_substring

char_list = ['s', 'a', 'n', 'd']
string = "Amanda’s in the land of pandas and is dandy!"
## desired output: ndas

print(shortest_substring(char_list, string))
print(better_shortest_substring(char_list, string))