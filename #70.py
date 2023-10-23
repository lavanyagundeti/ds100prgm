#70


data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 28},
]


sorted_data = sorted(data, key=lambda x: x["age"])


for entry in sorted_data:
    print(entry)
