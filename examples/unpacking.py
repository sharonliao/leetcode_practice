snack_claories = {
    'chips': 140,
    'popcorn': 80,
    'nuts': 180
}
items = tuple(snack_claories.items())
print(items)
# (('chips', 140), ('popcorn', 80), ('nuts', 180))

item = ('499999','2')
docID, tf = item

snacks = list(snack_claories.items())
for index, (name, calories) in enumerate(snacks):
    print(f"# {index}: {name} has {calories} calories")





