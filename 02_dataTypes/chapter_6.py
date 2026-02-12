# -----------------------------------------
# STRINGS IN PYTHON - DETAILED CONCEPT NOTES
# -----------------------------------------

"""
1️⃣ What is a String?

A string is:
- A sequence of characters
- Enclosed in single (' ') or double (" ") quotes
- Immutable (cannot change after creation)
- Ordered (has fixed position of characters)

In Python:
Everything is an object.
String is an object of class 'str'.
"""

chai_type = "Ginger Chai"      # String object
customer_name = "Priya"        # Another string object

# f-string (formatted string literal)
# Allows embedding variables using {}
print(f"Customer {customer_name} ordered {chai_type}")


# -----------------------------------------
# INDEXING & SLICING
# -----------------------------------------

"""
Indexing:
Each character has a position (index).
Index starts from 0.

Example:
"Garam chai and masala chai"

G → index 0
a → index 1
r → index 2
...

Negative Indexing:
-1 → last character
-2 → second last
"""

chai_description = "Garam chai and masala chai"

# Accessing first 10 characters
print(f"First 10 characters are: {chai_description[:10]}")

"""
Slicing Syntax:
string[start : end : step]

Important:
- Start index is INCLUDED
- End index is EXCLUDED
- Step tells how many jumps
"""

# From index 10 till end
print(f"Characters from index 10 onward: {chai_description[10:]}")

# Last 4 characters using negative slicing
print(f"Last 4 characters: {chai_description[-4:]}")

# Reverse the string using step = -1
print(f"Reversed string is: {chai_description[::-1]}")

"""
Why reverse works?
[start : end : step]

If step = -1:
Python moves backward.
This creates a reversed copy of the string.
"""

# -----------------------------------------
# IMMUTABILITY CONCEPT
# -----------------------------------------

"""
Strings are immutable.

This means:
Once created, you cannot change a character directly.

Example (this would give error):
chai_type[0] = "M"

Instead, Python creates a NEW string object
whenever you modify a string.
"""


# -----------------------------------------
# ENCODING & DECODING
# -----------------------------------------

"""
Computers store data as bytes (binary).

Encoding:
Converting string (text) → bytes

Decoding:
Converting bytes → string

UTF-8 is the most common encoding format.
It supports all Unicode characters.
"""

label = "Chai Spécial"

# Encoding string into bytes
encode_label = label.encode("utf-8")

print(f"Original label is: {label}")
print(f"Encoded label is: {encode_label}")

"""
Encoded output looks like:
b'Chai Sp\xc3\xa9cial'

The 'b' prefix means it is a bytes object.
Special characters (like é) are stored in multi-byte form.
"""

# Decoding bytes back to string
decode_label = encode_label.decode("utf-8")

print(f"Decoded label is: {decode_label}")


# -----------------------------------------
# 🧠 IMPORTANT CONCEPT SUMMARY
# -----------------------------------------

"""
1️⃣ String is an immutable sequence.
2️⃣ Supports indexing and slicing.
3️⃣ Slicing creates a NEW string.
4️⃣ Negative indexing accesses from end.
5️⃣ step parameter controls jump size.
6️⃣ Encoding converts string → bytes.
7️⃣ Decoding converts bytes → string.
8️⃣ Python strings use Unicode internally.
"""
