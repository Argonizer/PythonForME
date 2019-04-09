def prime(num):

    count = 0                     
    for i in range(1,num):    #[1,2,3,4,5,6,7,8,.......,num-1]
        if num % i == 0:
            count+=1

    if count == 1:
       return num

for i in range(100):       #"Banana"
    if(prime(i)):
        print(i)
