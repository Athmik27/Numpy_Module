# RANDOM NUMBERS
#( here we generate an random numbers)

import numpy as np

# random_number_generator=np.random.default_rng()
# print(random_number_generator.integers(1,7)) # this generate any random number from 1 to 7


# random_number_generator=np.random.default_rng()
# print(random_number_generator.integers(1,7,size=3)) # this generate any random number from 1 to 7 and size=3 means any 3 random number

# random_number_generator=np.random.default_rng()
# print(random_number_generator.integers(1,7,size=(3,2))) # this gives in 2D format

# for decimal values

# print(np.random.uniform()) # This generates a random decimal number between 0 and 1.

# print(np.random.uniform(-1,1)) # This generates a random decimal number between -1 and 1.

# print(np.random.uniform(-1,1,size=5))

# # using SHUFFLE METHOD

# random_number_generator=np.random.default_rng()
# array=np.array([1,22,3,4,5])
# random_number_generator.shuffle(array)
# print(array)

# we can also use  CHOICE() method

random_number_generator=np.random.default_rng()
fruits=np.array(["apple","mango","grapes"])
fruits=random_number_generator.choice(fruits,size=(3,2))
print(fruits)
