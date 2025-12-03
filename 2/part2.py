# Invalid IDS are IDS where a sequence of digits is repeated twice
# 55, 6464, 123123 are all invalid ids

invalid_nums = []

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

            # if len of num is 10, we need to split by 1,2,3,4,5 - range 1 - len/2
            for i in range(1, int(str_num_len/2)+1):
                # check
                pass

print(sum(invalid_nums))