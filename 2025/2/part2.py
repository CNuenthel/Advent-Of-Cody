from collections import Counter
# Invalid IDS are IDS where a sequence of digits is repeated twice
# I pulled all my input and verified the largest length of a range value was 10
# 55, 6464, 123123 are all invalid ids

"""
# Takeaways
Following completion 
A better way to complete this is to follow this line of thought.

1. Find the length of the string
2. Iterate over all substring lengths
3. Verify string can be divided by substring
4. Take a substring slice and concat by num of substrings for given substring length
5. If new string from substring slice is equal to original string, we have an invalid num

def is_repeated(s: str) -> bool:
    n = len(s)
    for L in range(1, n // 2 + 1):
        if n % L == 0:
            block = s[:L]
            if block * (n // L) == s:
                return True
    return False
"""

invalid_nums = []

def pop_chars(str_chars: str, sl: int) -> tuple:
    """
    :return: slice chars, remaining chars
    """
    return str_chars[:sl], str_chars[sl:]

with open("input.txt", "r") as f:
    data = f.read().split(",")

for d_range in data:
    str_range_0, str_range_1 = d_range.split("-")
    int_range_0, int_range_1 = int(str_range_0), int(str_range_1)

    for num in range(int_range_0, int_range_1+1):
        str_num = str(num)

        if len(str_num) == 2:
            if str_num[0] == str_num[1]:
                invalid_nums.append(num)
        else:
            str_num_len = len(str_num)
            list_str_num = [char for char in str_num]

            # All nums are the same, but pass single digit values
            if len(set([char for char in str_num])) == 1 and str_num_len != 1:
                invalid_nums.append(num)
                continue

            # Repeated 2-slices
            if len(str_num) % 2 == 0:
                str_num_copy = str_num
                slices = []
                while str_num_copy:
                    if len(str_num_copy) >= 2:
                        slice_chars, str_num_copy = pop_chars(str_num_copy, 2)
                        slices.append(slice_chars)
                    else:
                        break
                slice_counter = Counter(slices)
                if max(slice_counter.values()) >= len(str_num)/2:
                    invalid_nums.append(num)
                    continue

            # Repeated 3-slices
            if len(str_num) % 3 == 0:
                str_num_copy = str_num
                slices = []
                while str_num_copy:
                    if len(str_num_copy) >= 3:
                        slice_chars, str_num_copy = pop_chars(str_num_copy, 3)
                        slices.append(slice_chars)
                    else:
                        break
                slice_counter = Counter(slices)

                if len(str_num) == 6:
                    if max(slice_counter.values()) >= 2:
                        invalid_nums.append(num)
                        continue
                elif len(str_num) == 9:
                    if max(slice_counter.values()) >= 3:
                        invalid_nums.append(num)
                        continue

            # repeated 4-slices
            if len(str_num) % 4 == 0:
                str_num_copy = str_num
                slices = []
                while str_num_copy:
                    if len(str_num_copy) >= 4:
                        slice_chars, str_num_copy = pop_chars(str_num_copy, 4)
                        slices.append(slice_chars)
                    else:
                        break
                slice_counter = Counter(slices)
                if max(slice_counter.values()) >= 2:
                    invalid_nums.append(num)
                    continue

            # repeated 5-slices
            if len(str_num) % 5 == 0:
                str_num_copy = str_num
                slices = []
                while str_num_copy:
                    if len(str_num_copy) >= 5:
                        slice_chars, str_num_copy = pop_chars(str_num_copy, 5)
                        slices.append(slice_chars)
                    else:
                        break
                slice_counter = Counter(slices)
                if max(slice_counter.values()) >= 2:
                    invalid_nums.append(num)
                    continue

print(invalid_nums)
print(sum(invalid_nums))