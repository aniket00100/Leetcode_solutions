# def answer_function(n, ar):
#     ar.sort()
#     print(ar)
#     temp = ar[0]
#     pair_count = 0
#     i = 1
#     while i < n:
#         if ar[i] == temp:
#             pair_count += 1
#             i += 2
#             if i >= n:
#                 break
#             else:
#                 temp = ar[i-1]
#         elif i < n:
#             temp = ar[i]
#             i += 1
#         else:
#             i += 1
#     return pair_count
#
#
# n = int(input('n = '))
# ar = list(map(int, input("ar = ").split()))
# print(answer_function(n, ar))

#######################################################################################################
                                        # Version 2 #
#######################################################################################################
# def answer(n, ar):
#     pair_count = 0
#     ar_set = set()
#     ar_set.add(ar[0])
#     for num in ar[1:]:
#         if num in ar_set:
#             ar_set.remove(num)
#             pair_count += 1
#         else:
#             ar_set.add(num)
#     return pair_count
#
# n = int(input('n = '))
# ar = list(map(int, input("ar = ").split()))
# print(answer(n, ar))

#######################################################################################################
                                        # Version 3 #
#######################################################################################################
def answer(n, ar):
    new_dict = dict()
    for i in ar:
        if new_dict.get(i) != None:
            new_dict.update({i: new_dict.get(i) + 1})
        else:
            new_dict.update({i: 1})
    pair_count = 0
    for i in new_dict.values():
        pair_count += i//2

    return pair_count

n = int(input('n = '))
ar = list(map(int, input("ar = ").split()))
print(answer(n, ar))