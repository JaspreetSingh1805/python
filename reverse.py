# x = "Naveen Bhigan"
# a = x[::-1]
# print(a)
def reverse_str(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
input = "Hello"
print(reverse_str(input))
     