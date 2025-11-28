marks = {"Chaitra": "77", "harish": 87, "zzz": 89}
print(marks["Chaitra"])
marks["harish"] = 22
print(marks)

print(marks.keys())


print(marks.values())

print(marks.items())

marks.pop("zzz")
print(marks)

marks.popitem()
print(marks)

marks.update ({"age": 22})
print(marks)

marks.clear()
print(marks)