import numpy as np

array = np.random.randint(1,101,10)
print(array)

# loop through as many times as items in the array
for i in range(len(array)):
    for j in range(0, len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)