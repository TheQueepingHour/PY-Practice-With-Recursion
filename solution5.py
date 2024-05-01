# Write code for algorithm 5 below
def palindrome(string):
    return string == string[::-1]

print(palindrome("hannah"))
print(palindrome("racecar"))
print(palindrome("chicago"))
print(palindrome("Hollywood"))