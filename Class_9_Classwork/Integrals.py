import numpy as np


def fnct(x):
    return x**4 - 2*x + 1


# a is the start point
# b is the endpoint
# n is the number of slices
# h = b-a / n
# right side: a + kh
# left side: a + kh - h
#            a + (k-1)h
# Ak = (1/2)h[f(a+(k-1)h + f(a+kh)]
# simplifies to -> Ak = h[(1/2)f(a) + (1/2)f(b) + sum(f(a+kh))
def trapezoid_int(a, b, n):
    h = (b-a) / n
    area = 0

    # Because we start at 1, to get the loop to run for all values,
    # the upper limit must be +1
    for k in range(1, n):
        area += fnct(a+(k*h))

    area += (1/2) * (fnct(a) + fnct(b))
    area *= h
    return area


# Fit three points with a polynomial curve to approximate the area under that curve
# Need three points for each "slice"
# Each point, x, gets these three points by: [a, a+h, a+2h], [a+2h, a+3h, a+4h], ...
# Area under these three points given by: (1/3)h[f(a)+4f(a+h)+f(a+2h) + f(a+2h)+4f(a+3h)+f(a+4h)...]
#                                       = (1/3)h[f(a+(n-2)h + 4f(a+(n-1)h+f(b)]
# Finally:                      I(a, b) = (1/3)h[f(a) + f(b) + 4sum[k=1->(n/2)](f(a+(2k-1)h) + 2sum[k=1->n-1](f(a+2kh))
def simpson_int(a, b, n):
    area = 0
    h = (b-a)/n
    area += fnct(a) + fnct(b)

    sum = 0
    for k in range(1, (n//2)+1):
        sum += fnct(a+((2*k)-1)*h)
    area += 4*sum

    sum = 0
    for k in range(1, (n//2)):
        sum += fnct(a+(2*k*h))
    area += 2*sum

    area *= (1/3)*h
    return area


def main():
    n = 10000
    print("The correct value of the integral is 4.4")
    print("Estimation with n=" + str(n))
    area1 = trapezoid_int(0, 2, n)
    print("Trapeziod Estimation: " + str(area1))
    area2 = simpson_int(0, 2, n)
    print("Simpson's Rule Estimation: " + str(area2))


main()
