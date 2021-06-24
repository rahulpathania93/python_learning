'''
string = charcters  array
jhow to write = using single quotes, double and triple quotes
NOTE: triples quote is a comment
'''


string_var = 'apple fall from tree'

# #understanding array property of string

# 1. Indexing: as a string is array, all the charcters are indexed
print("the value indexed at position is ",string_var[7])

# 2. Slicing: we can slice the charcters according to our need
print("the value of slicing is also array that can be used further", string_var[0:5])

# 3. Iteration: we can iterate over a string
# 3.a iterating over a complete string
for var in string_var:
    if var in ('a','e','i','o','u'):
        print("vowel found",var)

# 3.b iterating over a slice
for var in string_var[0:5]:
    if var in ('a','e','i','o','u'):
        print("vowel found",var)
