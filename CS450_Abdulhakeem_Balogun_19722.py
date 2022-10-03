Question 1

# function make_buzzer
def make_buzzer(n):
    # defining another function 
    def function(m):
        # loop from 0 to m-1
        for i in range(m):
            # check if value of i is divisible by n
            if i % n == 0:
                # print message
                print('Buzz!')
            else:
                # else print value of i
                print(i)
    # return the function reference
    return function

# call to make_buzzer
i_hate_fives = make_buzzer(5)
# call the returned function from make_buzzer
i_hate_fives(10)



Question 2


def sum_n(n):

if n == 0 or n == 1:

return n

return n + sum_n(n-2)

print(sum_n(5))

print(sum_n(4))



Question 3

def cnt_primes(m):

if m == 0:

return 0

if is_prime(m):

return 1 + cnt_primes(m-1)

else:

return cnt_primes(m-1)



Question 4

(define (square x) (* x x))

(define (compose f g)
(lambda (x)
(f (g x))))

(define (repeated f n)
(if (= n 1)
f
(compose f (repeated f (- n 1)))))

(display ((repeated square 2) 5)) (newline)



Question 5

def operation(a, b, c):
if a == 0 or b == 0: # base case 1
return c
if a-1 == 0:# base case 2
return b+c

return b+operation(a-1, b, c) # for adding b a times, calling with one less a

print(operation (2, 4, 3)) # 11

print(operation (0, 3, 2)) # 2

print(operation (3, 0, 2)) # 2



def cal(n):

if n==0 or n==1: # base case

return n

return n*cal(n-2) # calling with 2 less n

print(cal(5)) # 15

print(cal(8)) # 0
