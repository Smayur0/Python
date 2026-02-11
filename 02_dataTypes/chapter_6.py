chai_type = "Ginger Chai"
customer_name = "Priya"

print(f"Customer {customer_name} ordered {chai_type}")


# -------------------------------
# Indexing and Slicing in Python
# -------------------------------

# string[start : end]


"""
Indexing:
In Python, each character in a string has a position (index).
Index always starts from 0.

Example:
String:  "Garam chai and masala chai"
Index:    0 1 2 3 4 5 6 ...

We can access a single character using indexing.
Example: string[0] → first character

Negative indexing:
-1 means last character
-2 means second last character
"""

chai_Description = "Garam chai and masala chai"

# Slicing:
# Slicing is used to extract a portion (substring) of a string.
# Syntax: string[start : end]
# It includes start index but excludes end index.

print(f"First 10 characters are: {chai_Description[:10]}")  
# means from index 0 to 9

print(f"Characters from index 10 onward: {chai_Description[10:]}")  
# means from index 10 till end

print(f"Last 4 characters: {chai_Description[-4:]}")  
# negative slicing (from end)

print(f"Reversed string is: {chai_Description[::-1]}")  
# negative slicing (reverse the string)

#Encoding and Decoding

# Encoding is the process of converting a string into bytes.
# Decoding is the process of converting bytes back into a string.

label = "Chai Spécial"
encode_label = label.encode("utf-8")  

# encoding the string to bytes
print(f"Original label is: {label}")
print(f"Encoded label is: {encode_label}")

# Decodeing the bytes back to string
decode_label = encode_label.decode("utf-8")  
print(f"Decoded label is: {decode_label}")