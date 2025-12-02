# Invalid IDS are IDS where a sequence of digits is repeated twice
# 55, 6464, 123123 are all invalid ids

val = 11,22

for i in range(val[0], val[1]+1):
    lis_i = [int(j) for j in str(i).split()]

    # compare digits if len >= 2
    # 12
    # compare every 2 digits if len >= 4
    # 1212
    # compare every 3 digits if len >= 6
    # 123123
    # compare every 4 digits if len >= 8
    # 12341234