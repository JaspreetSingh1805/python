def count_vowel(s):
    count = 0
    vowels = "aieouAIOUE"
    for char in s:
        if char in vowels:
           count += 1
    return count
string = "Hello"
# print(count_vowel(string))

# str="hello"
# str2=""
# for i in  str:
#     str2=i+str2
# print(str2)
# str = "beba"
# str2 = ""
# for i in str:
#     str2 = i + str2
# print(str2)
# str = "Naveen"
# str2 = ""
# for i in str:
#     str2 = i+str2
# print(str2)