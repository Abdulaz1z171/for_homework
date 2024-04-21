#  Tub sonlarni topuvchi funksiya


def find_prime_numbers(*args:int):
    prime_numbers = []
    for i in args:
        if 7 or 11 in args:
            prime_numbers.append(7)
            prime_numbers.append(11)
            if i%2 > 0:
                if i%3 > 0:
                    if i%4 > 0:
                        if i%5 > 0:      
                            if i%11 > 0:
                                prime_numbers.append(i)
            
        else:
            continue
    
    print(tuple(set(prime_numbers)))



