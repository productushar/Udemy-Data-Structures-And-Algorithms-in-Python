#Checking whether a string is a palindrome or not

def palindrome(s):
    if(s==s[::-1]):
        return True
    else:
        return False
