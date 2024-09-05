# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("That's not a valid number!")
# else:
#     print(f"The result is {result}")
# finally:
#     print("Execution complete.")
# try:
#     file = open("Assignments/Notes/notes.txt", "r")
#     data = file.read()
#     print(data)
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Closing the file.")
#     file.close()  