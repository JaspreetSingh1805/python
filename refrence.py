    
    # (Mutable function)
# def modify_list(lst):
#     lst.append(8)
#     print("inside function: ",lst)
# my_list = [1,2,3]
# modify_list(my_list)
# print("outside function: ",my_list)

    # (Immutable)
def modify_number(num):
    num += 5
    print("Inside function",num)
my_number = 10
modify_number(my_number)
print("Outside function",my_number)
    