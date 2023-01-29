from decimal import Decimal
import math


def abs_error(p, pa):
    return abs(Decimal(p) - Decimal(pa))


def rel_error(top, pa):
    return abs(Decimal(top) / abs(Decimal(pa)))


def exponent(str):
    count = 10
    res = 0

    for i in str:
        if i == '1':
            res += pow(2, count)

        count -= 1

    return res


def f(x):
    return x ** 3 + 4 * (x ** 2) - 10


def mantissa(str):
    count = 1
    res = float(0)

    for s in str:
        if s == '1':
            res += float(pow(0.5, count))
        count += 1

    return res


def bisection_method(left: float, right: float):
    tolerance: float = 10 ** -4
    max_iter = 100
    i = 0

    p = 1

    while abs(right - left) > tolerance and i < max_iter:
        i = i + 1
        p = (left + right) / 2

        if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
            right = p
        else:
            left = p

    return i


def f_derivative(x):
    return (3 * x * x) + (8 * x)


def newton_raphson(initial_approximation, tolerance, sequence):
    # remember this is an iteration based approach...
    iteration_counter = 0
    
    f = eval(sequence)
    # finds f'
    f_prime = f_derivative(initial_approximation)

    approximation: float = f / f_prime
    while abs(approximation) >= tolerance:
        # finds f
        f = eval(sequence)
        # finds f'
        f_prime = f_derivative(initial_approximation)
        # division operation
        approximation = f / f_prime
        # subtraction property
        initial_approximation -= approximation
        iteration_counter += 1

    return iteration_counter


def main():
    val = '010000000111111010111001000000000000000000000000000000'
    sign = val[0:0]
    exp = val[1:12]
    mant = val[12:]

    c = exponent(exp)
    ff = mantissa(mant)

    # problem 1
    calc = pow(2, c - 1023) * (1 + ff)
    print(f'{calc}')

    # problem 2
    norm = calc / 1000
    num2 = str(norm)
    print(f'\n{num2[0:5]}',  end='\n\n')

    # problem 3
    num3 = "{0:.3f}".format(norm)
    print(num3, end='\n\n')

    # problem 4
    ab_err = abs(Decimal(norm*1000) - Decimal(num3)*Decimal(1000))
    print(f'{ab_err/1000}')
    print(f'{Decimal(ab_err)/abs(Decimal(norm*1000)):.31f}', end='\n\n')

    # problem 5
    err_room = 4
    # (n+1)^3 > 10^4
    n = pow(10, (err_room / 3)) - 1
    print(math.ceil(n), end='\n\n')

    # problem 6
    left = -4
    right = 7
    # a
    bisect = bisection_method(left, right)
    print(bisect, end='\n\n')
    #b
    newt = newton_raphson(-4, 10**-4, 'x ** 3 + 4 * (x ** 2) - 10')
    print(newt, end='\n')


if __name__ == "__main__":
    main()
