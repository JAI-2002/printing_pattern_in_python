#printing pattern in python
#
# #
# # #
# # # #
# # # # #

# for i in range(4):
#     for j in range(4):
#         if j>=0 and j<=i:
#             print("# ",end="")
#     print()


#this one is much better and flexible as it takes input from the user and acts acordingly
n=int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print("#", end = "")
    print()
