def process(nums):
    max_num_index = 0
    min_num_index = 0
    length = len(nums)

    for i in range(1, length):
        # consuming O(n)
        if nums[max_num_index] < nums[i]:
            max_num_index = i
        if nums[min_num_index] > nums[i]:
            min_num_index = i
    # print(max_num_index)
    avg = int((nums[min_num_index] + nums[max_num_index]) / 2)
    new_list = []
    for i in nums:
        new_list.append(i - avg)

    right_sum = -1
    rotation_counter = 1
    print('new list = ', new_list)
    # print('right_list = ', new_list[max_num_index+rotation_counter:])
    while right_sum < 0:
        right_sum = sum(new_list[max_num_index+rotation_counter:])
        # print('right sum = ', right_sum)
        if right_sum >= 0:
            break
        new_list = rotate(new_list)
        rotation_counter += 1

    print('{} times rotation required'.format(rotation_counter - 1))
    for i in range(0, length):
        new_list[i] = new_list[i] + avg

    print('final list = ', new_list)
    print(cal_sum(new_list))

def brute_force(nums):
    ip_list = nums
    length = len(nums)
    s = cal_sum(nums)
    final_list = nums
    while length >= 1:

        new_list = rotate(ip_list)
        new_sum = cal_sum(new_list)
        if new_sum > s:
            final_list = new_list
            s = new_sum
        length -= 1
        ip_list = new_list
    print('final list = ', final_list)
    print('max sum = ', s)
    # print('max rotation', )

def rotate(nums):
    # print(nums)
    first, *rest, last = nums
    new_list = [last, first, *rest]
    # print(new_list, cal_sum(new_list))
    return new_list

def cal_sum(nums):
    sum = 0
    for i in range(0, len(nums)):
        sum += nums[i] * i
    return sum

nums = input("nums = ")
nums = list(map(int, nums.split()))
process(nums)
brute_force(nums)
