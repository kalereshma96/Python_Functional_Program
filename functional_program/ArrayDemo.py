# # #
# # # #to print list
# # #
# # # T = [[10,20,56,85],[56,20,43,10],[5,2,1],[8,5,75,6]]
# # # for i in T:
# # #     for c in i:
# # # #         print(c, end=" ")
# # # #     print()
# # #
# # # n = int(input())
# # # a = []
# # # for i in range(n):
# # #     a.append([int(j) for j in input().split()])
# #
# # elements = []
# #
# # # Append empty lists in first two indexes.
# # elements.append([])
# # elements.append([])
# #
# # # Add elements to empty lists.
# # elements[0].append(1)
# # elements[0].append(2)
# #
# # elements[1].append(3)
# # elements[1].append(4)
# #
# # # Display top-left element.
# # print(elements[0][0])
# #
# # # Display entire list.
# # print(elements)
# #
# # # Loop over rows.
# # for row in elements:
# #     # Loop over columns.
# #     for column in row:
# #         print(column, end="")
# #     print(end="\n")
# def switch_demo(argument):
#     switcher = {
#         1: "January",
#         2: "February",
#         3: "March",
#         4: "April",
#         5: "May",
#         6: "June",
#         7: "July",
#         8: "August",
#         9: "September",
#         10: "October",
#         11: "November",
#         12: "December"
#     }
#     return switcher.get(argument, "Invalid month")
num=int(input("enter no"))
decimal = 0
i = 1
while num != 0:
    remd = num % 2
    decimal = decimal + remd * i
    num = num // 10
    i = i * 2
print("decimal no is:", decimal)
