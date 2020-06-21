def move_zeros(nums):
    length = len(nums)

    for a in range(0, length):
        if nums[a] == 0:
            break

    if a == length - 1:
        return nums

    if nums[0] == 0:
        c = 0
        start = 0
    else:
        c = 1
        start = 1
    for i in range(start, length):
        if nums[i] != 0:
            # if i == length - 1 and c == start:
            #     break
            nums[c] = nums[i]
            if c != i:
                nums[i] = 0
            c += 1
    return nums

def brute_force(nums):
    length = len(nums)
    new_lst = [0]*length
    c = 0
    for i in range(0, length):
        if nums[i] != 0:
            new_lst[c] = nums[i]
            c += 1
    return new_lst

nums = list(map(int, input("nums = ").split()))

print(brute_force(nums))

