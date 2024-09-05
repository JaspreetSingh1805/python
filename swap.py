# method 1 
# l = [12,65,25,24,28]
# t = l[0]
# l[0] = l[len(l)-1]
# l[len(l)-1] =  t
# print(l)

# Second method 

# def swapList(newList):
#     size = len(newList)
    
#     # swapping 
#     temp = newList[0]
#     newList[0] = newList[size - 1]
#     newList[size - 1] = temp
#     return newList

# newList = [12,35,9,56,24]
# print(swapList(newList))\
    
    
# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

# Examples:  

# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# # Output : [19, 65, 23, 90]

# l = [23,65,19,90]
# t = l[0]
# l[0]= l[len(l)-2]
# l[len(l)-2] = t
# print(l)


# def swapList(newList):
#     size = len(newList)
#     # swapping 
#     temp = newList[0]
#     newList[0] = newList[size - 2]
#     newList[size - 2] = temp
    
#     newList = [23,65,19,90]
#     print(swapList(newList))

#   Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]   

# l =  [1,2,3,4,5]
# t = l[1]
# l[1] =  l[len(l)-1]
# l[len(l)-1] = t
# print(l)

# . Find the Length of a List Using Naive Method
# Initializing list
# test_list = [1, 4, 5, 7, 8]
# counter = 0
# for i in test_list:
#     counter+=1
# print("Length of list using naive method is : " , counter)


#4 Find the Length of a List Using length_hint() Method
# from operator import length_hint

# test_list = [1, 4, 5, 7, 8]
# list_len = len(test_list)

# list_len_hint = length_hint(test_list)

# print("Length of list using len() is : " ,list_len)

# print("Length of list using length_hint() is : ", list_len_hint)


# 5. Find the Length of a List Using sum() Function



# test_list = [1, 4, 5, 7, 8,5,5,5,5,5,88,5,5,5,58]
 
# print("The list is : " + str(test_list))
 
# list_len = sum(1 for i in test_list)
 
 
# print("Length of list using len() is : " + str(list_len))

# list = [2,5,5,8,5,8,5,5,5,5]
# list_len = sum(1 for i in list)
# print(list)
# print(list_len)

# number  = [1,2,3,4,5,6,7,8]
# double = [x*3 for x in number]
# print(double)

# number =  [12,2,6,2,8,9,10]
# square = [x**2 for x in number]
# print(square)

# list = [char for char in [1,2,3]]
# print(list)

# list = [x for x in range(2,101) if x%2==0]
# print(list)

# list = [x for x in range(0,101) if x%2!=0 ]
# print(list)

# matrix = [[j for j in range(4)] for i in range(4)]
# print(matrix)

# Using list comprehension to iterate through loop 
# list = [char for char in  'geeks for geeks']
# print(list)

z = [f"20 X {i} = {20 * i}" for i in range(1,11)]
print("\n".join(z))


