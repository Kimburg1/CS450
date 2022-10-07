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

def is_prime(n, i=2):
    if n <= i:
        return True
    elif n % i == 0:
        return False
    else:
       return is_prime(n, i + 1)

def cnt_primes(n):
    count=0
    i = 2
    while(i<=n):
         if is_prime(i):
           count+=1
         i+=1
    print("# of prime numbers = ",count)
cnt_primes(5)




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


QUESTION 6

def checking(n):
    if n<=0:
        print("Number should be positive integer ")
        return 
    else: 
      while (n>=1):
          a = n%10
          b = (n//10)%10
          if a >= b:
              output = True 
              n//=10
          else:
             output = False
             break 
    return output 
print(checking(5))
print(checking(11))
print(checking(127))
print(checking(1357))
print(checking(21))
result = checking(1372)
print(result)


QUESTION 7

def   cal(n):
    if n%2 == 0 and n <= 1:
      return 0
    elif n%2 == 1 and n <= 1:
      return 1

    elif n%2 == 0:
      return n*cal(n-2)
    return n*cal(n-2)

print(cal(5))

QUESTION 8

def incr(n):
    return n+1
def triple(n):
    return 3*n
def square(n):
  return n*n

def intscts(f,n):
    if n == 1:
       if f(n) == g(n):
         return True
       else:
         return False 
    g = lambda x: f(intscts(f, n-1)(x))

at3 = intscts(square,3)
at3(triple)


QUESTION 9

def  A(n): 
    if n <= 3:
      return n
    else:
      return A(n - 1) + 2 * A(n - 2) + 3 * A(n - 3)

print(A(1))
print(A(2))
print(A(3))
print(A(4))
print(A(5))

QUESTION 10

def bnc_bck_frth(n):
    k = 1
    assending = True 
    num_found = False 
    for i in range (1, n):
        #print(k)
        j = i
        while(j!=0):
          if i%10 ==7:
            num_found = True 
            break
          j //=10
        #print(num_found)
        if i%7 == 0 or num_found==True:
            num_found = False
            if assending == True: 
                assending = False 
            else:
                assending = True 
        if assending == True:
            k +=1
        else:
            k -=1
    return k
print(bnc_bck_frth (7))
print(bnc_bck_frth (8))
print(bnc_bck_frth (15))
print(bnc_bck_frth (21))
print(bnc_bck_frth (22))
print(bnc_bck_frth (30))
print(cal(8))
