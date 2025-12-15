words = ["banana", "mango", "apple", "cat", "dog", "lion"]

filtered_words = []

for x in words:
    if len(x)>3:
        filtered_words.append(x.upper())
slicing = filtered_words[:3]
slicing.sort
print(slicing)        