# Problem Title: Rabbit Recurrence

'''A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms.
In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring.
A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior.
As a result, if F represents the number of rabbit pairs alive after the -th month, then we obtain the Fibonacci sequence having terms F that are defined by the recurrence relation Fn=Fn−1+Fn−2(with F1=F2=1to initiate the sequence).'''

# definig the function to calculate the number of rabbit pairs
## The function takes two parameters: n (the month) and k (the number of offspring produced by each pair of rabbits)
def fibb(n,k): 
    if n==1 or n==2:
        return 1
    else:
        return fibb(n-1,k) + k * fibb(n-2,k)

# Example usage   
print(fibb(35, 2))   






