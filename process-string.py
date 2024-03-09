# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
str_input= input("Enter any words to double: ")
l1,l2 = list(str_input),list(str_input)

new_list = [None] * (len(l1)+ len(l2))
new_list[::2] = l1 #odd index
new_list[1::2] = l2 #even index
double_char = "".join(new_list) #join string together
print(double_char)
# # Application 2
# #  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.

user_range = input("Enter a range of letters (e.g., a-z): ")
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
start , end = user_range.split("-")
result_string = alphabet[alphabet.index(start) : alphabet.index(end) + 1]
print(result_string)

