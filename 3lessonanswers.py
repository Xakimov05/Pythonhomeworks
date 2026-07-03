numbers = [345, 43, 55, 43, 45, 23]
element = 2
print(numbers.count(element))

numbers = [10, 20, 30, 40, 50]
print(sum(numbers))

numbers = [10, 818, 232, 120, 555]
print(max(numbers))

numbers = [44, 81, 22, 100, 45]
print(min(numbers))

numbers = [123, 222, 333, 444, 343, 23]
element = 6
print(element in numbers)

numbers = [10, 20, 30]
print(numbers[0] if numbers else None)

numbers = [1, 2, 3, 4, 5]
print(numbers[:3])

numbers = [10, 29, 31, 43, 55]
print(numbers[::-1])

numbers = [54, 22, 4, 10, 3]
print(sorted(numbers))

numbers = [1, 2, 2, 3, 4, 4]
print(list(set(numbers)))

numbers = [1, 2, 4]
numbers.insert(2, 3)
print(numbers)

numbers = [100, 220, 3, 24]
element = 3
print(numbers.index(element))

numbers = []
print(len(numbers) == 0)

numbers = [112, 23, 33, 44, 57, 60]
count = sum(1 for n in numbers if n % 2 == 0)
print(count)

numbers = [11, 22, 333, 44, 55, 66]
count = sum(1 for n in numbers if n % 2 != 0)
print(count)

list1 = [11, 22]
list2 = [33, 44]
print(list1 + list2)

numbers = [11, 22, 30, 40, 55]
sublist = [30, 40]

found = False
for i in range(len(numbers) - len(sublist) + 1):
    if numbers[i:i+len(sublist)] == sublist:
        found = True
        break

print(found)

numbers = [11, 42, 233, 342]
old = 42
new = 342

if old in numbers:
    index = numbers.index(old)
    numbers[index] = new

print(numbers)

numbers = [4, 8, 2, 10, 5]
unique = sorted(set(numbers))
print(unique[-2])

numbers = [4, 8, 2, 10, 5]
unique = sorted(set(numbers))
print(unique[1])

numbers = [1, 2, 3, 4, 5, 6]
even = [n for n in numbers if n % 2 == 0]
print(even)

numbers = [1, 2, 3, 4, 5, 6]
odd = [n for n in numbers if n % 2 != 0]
print(odd)

numbers = [1, 2, 3, 4]
print(len(numbers))

numbers = [1, 2, 3]
copy = numbers.copy()
print(copy)

numbers = [11, 20, 13, 14, 50]

if len(numbers) % 2 == 1:
    print(numbers[len(numbers)//2])
else:
    mid = len(numbers)//2
    print(numbers[mid-1:mid+1])

numbers = [1, 5, 3, 8, 2]
sublist = numbers[1:4]
print(max(sublist))

numbers = [1, 5, 3, 8, 2]
sublist = numbers[1:4]
print(min(sublist))

numbers = [10, 20, 30]

index = 1

if 0 <= index < len(numbers):
    numbers.pop(index)

print(numbers)

numbers = [1, 2, 3, 4]
print(numbers == sorted(numbers))

numbers = [11, 20, 30]
times = 2

result = []
for n in numbers:
    result.extend([n] * times)

print(result)

list1 = [50, 11]
list2 = [40, 20]
print(sorted(list1 + list2))

numbers = [1, 2, 3, 2, 4, 2]
element = 2

indices = [i for i, n in enumerate(numbers) if n == element]
print(indices)

numbers = [1, 2, 3, 4, 5]
rotated = [numbers[-1]] + numbers[:-1]
print(rotated)

numbers = list(range(10, 21))
print(numbers)

numbers = [-2, 33, -11, 57, 40]
total = sum(n for n in numbers if n > 0)
print(total)

numbers = [-22, 33, -12, 0, 44]
total = sum(n for n in numbers if n < 0)
print(total)

numbers = [1, 2, 3, 2, 1]
print(numbers == numbers[::-1])

numbers = [1, 2, 3, 4, 5, 6]
size = 2

nested = [numbers[i:i+size] for i in range(0, len(numbers), size)]
print(nested)

numbers = [11, 22, 22, 30, 11, 44]

unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)

numbers = (13, 13, 33, 22, 13, 22)
element = 13
print(numbers.count(element))

numbers = (44, 28, 42, 13, 35)
print(max(numbers))

numbers = (44, 28, 22, 130, 25)
print(min(numbers))

numbers = (11, 22, 33, 14)
element = 22
print(element in numbers)

numbers = (10, 20, 30)
print(numbers[0] if numbers else None)

numbers = (10, 20, 30)
print(numbers[-1] if numbers else None)

numbers = (11, 22, 30, 40)
print(len(numbers))

numbers = (1, 2, 3, 4, 5)
print(numbers[:3])

tuple1 = (11, 12)
tuple2 = (33, 40)
print(tuple1 + tuple2)

numbers = ()
print(len(numbers) == 0)

numbers = (1, 2, 3, 2, 4, 2)
element = 2

indices = [i for i, n in enumerate(numbers) if n == element]
print(indices)

numbers = (44, 38, 24, 12, 25)
unique = sorted(set(numbers))
print(unique[-2])

numbers = (44, 28, 22, 103, 325)
unique = sorted(set(numbers))
print(unique[1])

single = (6,)
print(single)

numbers = [12, 23, 33, 44]
result = tuple(numbers)
print(result)

numbers = (1, 2, 3, 4)
print(numbers == tuple(sorted(numbers)))

numbers = (1, 5, 3, 8, 2)
subtuple = numbers[1:4]
print(max(subtuple))

numbers = (1, 5, 3, 8, 2)
subtuple = numbers[1:4]
print(min(subtuple))

numbers = (1, 2, 3, 2, 4)
element = 2

temp = list(numbers)

if element in temp:
    temp.remove(element)

result = tuple(temp)
print(result)

numbers = (1, 2, 3, 4, 5, 6)
size = 2

nested = tuple(
    tuple(numbers[i:i+size])
    for i in range(0, len(numbers), size)
)

print(nested)

numbers = (1, 2, 3)
times = 2

result = ()

for n in numbers:
    result += (n,) * times

print(result)

numbers = tuple(range(1, 11))
print(numbers)

numbers = (1, 2, 3, 4, 5)
print(numbers[::-1])

numbers = (1, 2, 3, 2, 1)
print(numbers == numbers[::-1])

numbers = (11, 22, 22, 3, 11, 44)

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(tuple(unique))

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)

set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print(result)

set1 = {11, 20, 33}
set2 = {20, 14}
result = set1.difference(set2)
print(result)

set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))

numbers = {1, 2, 3, 4}
element = 3
print(element in numbers)

numbers = {12, 22, 13, 43}
print(len(numbers))

numbers = [1, 2, 2, 3, 4, 4]
result = set(numbers)
print(result)

numbers = {12, 42, 33, 44}
element = 42

if element in numbers:
    numbers.remove(element)

print(numbers)

numbers = {13, 22, 13}
numbers.clear()
print(numbers)

numbers = set()
print(len(numbers) == 0)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.symmetric_difference(set2)
print(result)

numbers = {1, 2, 3}
numbers.add(4)
print(numbers)

numbers = {1, 2, 3}

element = numbers.pop()

print("Removed:", element)
print(numbers)

numbers = {34, 28, 22, 11, 15}
print(max(numbers))

numbers = {4, 8, 2, 10, 5}
print(min(numbers))

numbers = {12, 21, 33, 24, 55, 66}
even = {n for n in numbers if n % 2 == 0}
print(even)

numbers = {31, 22, 33, 44, 52, 63}
odd = {n for n in numbers if n % 2 != 0}
print(odd)

numbers = set(range(1, 11))
print(numbers)

list1 = [1, 2, 3]
list2 = [3, 4, 5]

result = set(list1 + list2)

print(result)

set1 = {11, 22}
set2 = {33, 44}

print(set1.isdisjoint(set2))

numbers = [1, 2, 2, 3, 4, 4]

result = list(set(numbers))

print(result)

numbers = [11, 22, 22, 32, 44, 41]

count = len(set(numbers))

print(count)

import random

numbers = set()

while len(numbers) < 5:
    numbers.add(random.randint(1, 20))

print(numbers)

student = {"name": "Nursaid", "age": 21}
print(student.get("name", None))

student = {"name": "Nursaid", "age": 21}
print("age" in student)

student = {"name": "Nursaid", "age": 21, "city": "Namangan"}
print(len(student))

student = {"name": "Nursaid", "age": 21}
print(list(student.keys()))

student = {"name": "Nursaid", "age": 21}
print(list(student.values()))

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

result = dict1 | dict2
print(result)

student = {"name": "Nursaid", "age": 21}
key = "age"

student.pop(key, None)

print(student)

student = {"name": "Nursaid", "age": 21}

student.clear()

print(student)

student = {}

print(len(student) == 0)

student = {"name": "Nursaid", "age": 21}
key = "age"

if key in student:
    print((key, student[key]))
else:
    print(None)

student = {"name": "Nursaid", "age": 21}

student["age"] = 21

print(student)

data = {"a": 1, "b": 2, "c": 1, "d": 3}

value = 1

count = list(data.values()).count(value)

print(count)

data = {"a": 1, "b": 2, "c": 3}

result = {value: key for key, value in data.items()}

print(result)

data = {"a": 1, "b": 2, "c": 1, "d": 3}

value = 1

keys = [key for key, val in data.items() if val == value]

print(keys)

keys = ["a", "b", "c"]
values = [1, 2, 3]

result = dict(zip(keys, values))

print(result)

data = {
    "student": {"name": "Nursaid"},
    "age": 21
}

result = any(isinstance(value, dict) for value in data.values())

print(result)

data = {
    "student": {
        "name": "Nursaid",
        "age": 21
    }
}

print(data["student"]["name"])

from collections import defaultdict

data = defaultdict(lambda: "Not Found")

data["name"] = "Nursaid"

print(data["name"])
print(data["age"])

data = {"a": 1, "b": 2, "c": 1, "d": 3}

count = len(set(data.values()))

print(count)

data = {"c": 3, "a": 1, "b": 2}

result = dict(sorted(data.items()))

print(result)

data = {"a": 3, "b": 1, "c": 2}

result = dict(sorted(data.items(), key=lambda item: item[1]))

print(result)

ata = {"a": 10, "b": 5, "c": 20, "d": 3}

result = {k: v for k, v in data.items() if v > 5}

print(result)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

common = set(dict1.keys()) & set(dict2.keys())

print(len(common) > 0)

pairs = (("a", 1), ("b", 2), ("c", 3))

result = dict(pairs)

print(result)

data = {"a": 1, "b": 2, "c": 3}

first = next(iter(data.items()))

print(first)
