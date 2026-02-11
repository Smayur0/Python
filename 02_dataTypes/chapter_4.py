is_boiling = True
string_count = 4
total_actoins = string_count+is_boiling
print(f"Total actions is {total_actoins}") # 5 due to upCasting

miik_present = "jelkwsnd"  # 0 and None gives false, any other value gives true
print(f"is there milk? {bool(miik_present)}")

# logical operators
is_morning = True
is_Evening = False

# OR operator
what_is_time = is_morning or is_Evening
print(f"is it morning or evening? {what_is_time}")

# AND operator
what_is_time = is_morning and is_Evening
print(f"is it morning and evening? {what_is_time}")

# NOT operator
what_is_time = not is_Evening
print(f"NOT evening? {what_is_time}")