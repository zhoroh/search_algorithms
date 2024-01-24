def hill_climbing(numbers:list):
    current_max = numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i] > current_max:
            current_max = numbers[i]

    return current_max


max_ = hill_climbing([102,7,8,4,100,3,2,5,9])
print(max_)