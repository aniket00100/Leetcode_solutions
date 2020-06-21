# def happy_number(n):
#     arr = [int(i)*int(i) for i in str(n)]
#     sm = sum(arr)
#     sum_list = []
#     sum_list.append(sm)
#     while sm != 1:
#         arr = [int(i)*int(i) for i in str(sm)]
#         sm = sum(arr)
#         if sm == 1:
#             return True
#         if sm in sum_list:
#             return False
#         sum_list.append(sm)
#     if sm == 1:
#         return True
#     return False
#
#
# def calculate_sq_sum(arr):
#     pass
#######################################################################

def numSquareSum(n):
    squareSum = 0;
    while (n):
        squareSum += (n % 10) * (n % 10);
        n = int(n / 10);
    return squareSum;

def isHappynumber(n):

    slow = n;
    fast = n;
    while (True):

        slow = numSquareSum(slow);
        fast = numSquareSum(numSquareSum(fast));
        if (slow != fast):
            continue;
        else:
            break
    return (slow == 1);



n = input("n = ")
print(isHappynumber(n))