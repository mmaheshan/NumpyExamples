import numpy as np
from timeit import default_timer as timer


# Create a NumPy array 
array = np.array([1, 2, 3, 4, 5])
print("Created NumPy Array:", array)

multi_array = np.array([[1,2,3],[4,5,6]])

numbers = np.arange(1,50,0.3)
print (numbers)

try:
    numbers = list(range(1,20.5,1))
    print (numbers)
except TypeError as te:
    print("TypeError: Cant have floats") 

zeros = np.zeros((10,10), dtype='int')

print (zeros)

ones = np.ones((5,5,5))

print (ones)
    
empty = np.empty((4,4))
print(empty)

empty = np.empty

matrix = np.random.randint(1,10,(3,3))
print(matrix)

numbers = list(range(1,1000000))
start = timer()
[n + 1 for n in numbers]
end = timer()
elapsed_time = end - start
print(f"Elapsed time: {elapsed_time}")

numbers_np = np.array(numbers)
print(numbers_np.shape)

start = timer()
numbers_np + 1
end = timer()
elapsed_time = end - start
print(f"Elapsed time: {elapsed_time}")

arr = np.array([False, 2, 3], dtype=np.float64)

print(arr)

floats = np.array([1.5, 2.5, 3.5])
ints = np.array([1,1,1])

j = floats + ints
print(j)

mixed1 = np.array([1, 2, 'apples'])
print(mixed1)
mixed2 = np.array([1, 2, 'fruits'])

k = mixed1 + mixed2
print(k)