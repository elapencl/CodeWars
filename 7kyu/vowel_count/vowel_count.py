def get_count(input_str):
    vowels = ['a','e','i','o','u']
    num_vowels = 0
    i = 0
    while i < len(input_str):
        for j in vowels:
            if input_str[i] == j:
                num_vowels = num_vowels + 1
        i = i + 1
    return num_vowels
