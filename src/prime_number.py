def is_prime(number):
    nums = [x for x in range(2, number+1)]
    prime = [x for x in nums if number%x == 0]
    if len(prime)>1:
        return False
    else:
        return True
    

num = input("Enter a number to test if it is prime: ")
num = int(num)
print(is_prime(num))