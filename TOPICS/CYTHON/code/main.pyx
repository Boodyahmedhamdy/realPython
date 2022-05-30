
def find_primes_vanilla(amount: int):
    primes = []
    found = 0

    number = 2

    while found < amount:
        for x in range(2, number):
            if number % x == 0:
                break

        # if break isn't happend
        else:
            primes.append(number)
            found += 1
        number += 1
    return primes


def find_primes_cython(int amount):
    cdef int number, x, found
    cdef int primes[100000]

    # take the minimum of amount and max size of the array
    amount = min(amount, 100000)

    found = 0
    number = 2

    while found < amount:
        for x in primes[:found]:
            if number % x == 0:
                break

        else:
            primes[found] = number
            found += 1

        number += 1

    return_list = [p for p in primes[:found]]
    return return_list