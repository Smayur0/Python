masla_spices = ("cumin", "coriander", "turmeric", "cardamom", "cloves")
(first, second, third, fourth, fifth) = masla_spices

print(f"First spice: {first}, second spice: {second}, third spice: {third}, fourth spice: {fourth}, fifth spice: {fifth}")

ginger_ratio, cadramom_ratio = 2, 1

print(f"Ginger ratio: {ginger_ratio}, Cardamom ratio: {cadramom_ratio}")

ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio

print(f"Ginger ratio: {ginger_ratio}, Cardamom ratio: {cadramom_ratio}")

#membership testing
print("cumin" in masla_spices)
print("pepper" in masla_spices)