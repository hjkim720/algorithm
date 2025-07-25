while True:
    n = int(input())
    if n == -1:
        break
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i != n:
                divisors.append(i)
            if i != 1 and i != n // i and n // i != n:
                divisors.append(n // i)
    divisors.sort()
    if sum(divisors) == n:
        print(f"{n} =", " + ".join(map(str, divisors)))
    else:
        print(f"{n} is NOT perfect.")
