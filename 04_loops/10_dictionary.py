# -----------------------------------------
# Coupon Discount Processing
# -----------------------------------------

users = [
    {"id": 1, "total": 200, "coupon": "DISCOUNT10"},
    {"id": 2, "total": 150, "coupon": "DISCOUNT20"},
    {"id": 3, "total": 200, "coupon": "DISCOUNT30"},
]
# list of dicts → typical JSON-like structure (API-style data)


discounts = {
    "DISCOUNT10": (0.10, 0),
    "DISCOUNT20": (0.20, 0),
    "DISCOUNT30": (0, 30)
}
# dictionary mapping coupon → (percentage_discount, fixed_discount)
# tuple used because:
# - fixed structure
# - immutable
# - lightweight


for user in users:

    # dict.get(key, default)
    # avoids KeyError if coupon not found
    # returns (0,0) fallback if coupon invalid
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    # tuple unpacking into two variables

    # discount calculation:
    # percentage part + fixed part
    discount = user["total"] * percent + fixed

    print(f"User {user['id']} paid {user['total']} got a discount of {discount}")


"""
Execution Flow (per user):

1. Access coupon → O(1) dictionary lookup (hash table)
2. Unpack tuple → constant time
3. Compute discount → arithmetic operation
4. Print result

Overall complexity: O(n) where n = number of users
Space complexity: O(1) extra
"""


# -----------------------------------------
# Design Insight
# -----------------------------------------

"""
✔ Data-driven design:
   Instead of if/elif chains for coupons,
   behavior is controlled via mapping table.

✔ Scalable:
   Adding new coupon requires only updating `discounts` dict.

✔ Safe access:
   .get() prevents runtime crash on unknown coupon.

Production improvement:
- Consider using Decimal for financial calculations (avoid float precision issues).
- Consider storing coupon structure as dict or dataclass if logic grows.
"""
