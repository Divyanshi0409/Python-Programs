def is_palindrome(str):
    if str==str[::-1]:
        return True
    else:
        return False

str= input("Enter a string: ")
palindrome = is_palindrome(str)
if palindrome==True:
    print("The string is palindrome")
else:
    print("The string is not palindrome")