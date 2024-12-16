def sortedlist(names,heights):
    return[ name for height, name in sorted(zip(heights,names), reverse=True)]
names = ["arya","rekha","Derin","manav"]
heights = [180,172,163,178]
output = sortedlist(names,heights)
print(output)