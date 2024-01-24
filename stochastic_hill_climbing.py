import random

def stochastic_hill_climbing(numbers:list):
    current_index =random.randint(0,len(numbers) -1)
    current_max = numbers[current_index]

    for i in range(100):
        current_index = random.randint(0,len(numbers) -1)
        max_ = numbers[current_index]
        if max_ > current_max:
            current_max = max_

    return current_max



max_num = stochastic_hill_climbing([12,7,8,4,100,3,2,5,9])
print(max_num)