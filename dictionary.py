from collections import Counter
import matplotlib.pyplot as plt

friuts = [
    'banana',
    'apple', 'apple',
    'orange', 'orange', 'orange',
    'cherry', 'cherry', 'cherry', 'cherry'
    ]

fruit_counter = Counter(friuts)

print(fruit_counter.most_common(3))

print(fruit_counter.keys())
print(fruit_counter.values())

plt.bar(fruit_counter.keys(), fruit_counter.values())

plt.show()