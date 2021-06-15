import numpy as np

array = np.random.randint(1,101,10)
print(array)

for i in range (len(array)):
    # Assume smallest is at current index
    IndexOfMin = i

    # Look through the rest of the array to see if there is anything smaller
    for j in range(i+1,len(array)):
        # If smaller update the position of the smaller element to the current one
        if array[IndexOfMin] > array[j]:
            IndexOfMin = j
    # Swap the current value with the smaller value found, swap is kinda redundant 
    # if i was actually the smallest value as basically swapping with itself 
    temp = array[i]
    array[i] = array[IndexOfMin]
    array[IndexOfMin] = temp

print(array)
