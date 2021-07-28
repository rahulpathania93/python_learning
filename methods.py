# Create a variable named carname and assign the value Volvo to it.
carname = "volvo"
print(carname)
# Remove the illegal characters in the variable name:
# 2my-first_name = "John"
first_name = "john"

#1.Format():-)  
# Using a string and .format() method print the number: 1 only.
print("{}".format(1))

# Now using a string and .format() method and three curly brackets, 
# print the numbers: 1, 2, 3 each separated with a comma.

numbers = "{},{},{}".format(1,2,3)
print(numbers)


# Fill in the values for months, weeks and days accordingly.
str1 = "one year has {} months, {} weeks and {} days.".format(12,52,365)
print(str1)

# Fill inside .format()'s parenthesis so that it matches the correct values.
rahul = 70
adi = 93
deepi = 80
str2 = "scores were as following: rahul:{}, adi{}, deepi{}"
print(str2.format(70,93,80))

#2.join():-)
# Join the list's elements with: "+++".
lst = ["india", "usa", "new jersey"]
joined= "+++".join(lst)
print(joined)


# Join the tuple's elements so that you get a proper email address.
address = ("mr.rahul","gamil.com")
email = "@".join(address)
print(email)

# Join each element in the list with a space character: " "
lst =['everything','has','beauty','but','no','one','can','see','that']
joined = " ".join(lst)
print(joined)



# Using .join() method join the keys in the dictionary with a comma: ",".
economic_growth= {"india" : 7.0, "combodia" : 7,"russia": 7.9,"pakistan":4.7}
str = ",".join(economic_growth)
print(str)


# Python join method with new line character
# "\n" is a character that creates a new line. (Similar to when you press enter key in your text editor.)
# Using "\n" character and .join() method, join the sentences in the list so that it looks like a proper poem.
poem_lst=["Not enjoyment, and not sorrow,", "Is our destined end or way;", " But to act, that each tomorrow", "Find us farther than today."]
poem_str="\n".join(poem_lst)
print(poem_str)
