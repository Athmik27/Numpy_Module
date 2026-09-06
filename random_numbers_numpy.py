# RANDOM NUMBERS
#( here we generate an random numbers)

import numpy as np

random_number_generator=np.random.default_rng()
print(random_number_generator.integers(1,7)) # this generate any random number from 1 to 7

random_number_generator=np.random.default_rng() # default_rng() creates a random number generator object.

print(random_number_generator.integers(1,7)) # this generate any random number from 1 to 7

print(random_number_generator.random()) # it generates the random float point number from 0 to 1 ( as the size is not been mentioned)

# np.random.uniform(low, high, size) this gives an random float number from 1 to 10.
print(random_number_generator.uniform(1,10))


random_number_generator=np.random.default_rng()
print(random_number_generator.integers(1,7,size=3)) # this generate any random number from 1 to 7 and size=3 means any 3 random number

random_number_generator=np.random.default_rng()
print(random_number_generator.choice([10, 20, 30])) # this randomly choose any 1 value from the list.

random_number_generator=np.random.default_rng()
print(random_number_generator.integers(1,7,size=3)) # this generate any random number from 1 to 7 and size=3 means any 3 random number

random_number_generator=np.random.default_rng()
print(random_number_generator.integers(1,7,size=(3,2))) # this gives in 2D format

# for decimal values
# for decimal we can also use random()

print(np.random.uniform()) # This generates a random decimal number between 0 and 1.
print(np.random.uniform(-1,1)) # This generates a random decimal number between -1 and 1.
print(np.random.uniform(-1,1,size=5))

# using SHUFFLE METHOD

random_number_generator=np.random.default_rng()
array=np.array([1,22,3,4,5])

random_number_generator.shuffle(array) # randomly changes the order of the elements inside the original array.
print(array)

# we can also use  CHOICE() method

random_number_generator=np.random.default_rng()
fruits=np.array(["apple","mango","grapes"])
fruits=random_number_generator.choice(fruits,size=(3,2)) # choice() to randomly select elements from an array.
print(fruits)

# permutation() randomly rearranges an array.
# Permutations generate ALL possible arrangements

rng = np.random.default_rng() # rng=random_number_generator
array = np.array([1, 2, 3, 4, 5])
new_array = rng.permutation(array)
print("Original:", array)
print("New:", new_array)

# normal() — Generate Random Numbers from a Normal Distribution.
rng.normal(loc=0.0, scale=1.0, size=None)

# | Parameter | Meaning                       |
# | --------- | ----------------------------- |
# | `loc`     | Mean (center)                 |
# | `scale`   | Standard deviation (spread)   |
# | `size`    | Number/shape of random values |

# poisson() — Counting Events
# The Poisson distribution is used when we want to find how many times an event happens during a fixed period or area.

customers = rng.poisson(lam=5, size=10)
print(customers)

# lam	Average number of events 
# # lam=lambda.
# size	Number/shape of random results

# exponential() — Waiting Time Between Events

waiting_time = rng.exponential(scale=5, size=10)
print(waiting_time)

# rng.exponential(scale=1.0, size=None)
# Parameter	Meaning
# scale	Average waiting time
# size	Number/shape of random values

# seed() seed gives the random generator a starting point,and also we get the same sequence of random numbers.
import numpy as np
np.random.seed(42) # here when you run the code multiple times your result will be the same.
print(np.random.randint(1, 10))