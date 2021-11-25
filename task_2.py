def is_palindrome(s):
    if s == s[::-1]:
        print("is palindrome")
    else:
        print("is not palindrome")


is_palindrome("поп")
