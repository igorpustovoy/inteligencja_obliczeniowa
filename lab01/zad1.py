def prime(number, curr=2):
    if number == curr:
        return True
    elif number % curr == 0:
        return False
    else:
        return prime(number, curr + 1)


def select_primes(list):
    new_list = []
    for number in list:
        if prime(number):
            new_list.append(number)
    return new_list


# Zad1 a)
print(prime(7))

# Zad1 b)
print(select_primes([4, 12, 7, 17, 37, 102]))
