def brute_force(A,k):
    n = len(A)
    solutions = []
    for i in range(n+1): 
        for j in range(i+1,n+1):
            subarr=A[i:j]
            if sum(subarr)==k:
                solutions.append(subarr)


    return solutions


def cumulative_sum(A,k):
    n = len(A)
    solutions = []
    for i in range(n+1):
        sum_so_far = 0
        for j in range(i,n):
            sum_so_far += A[j]
            if sum_so_far == k:
                solutions.append(A[i:j+1])
    

    return solutions

from collections import defaultdict  

def hashmap(A,k): #Time complexity : O(n^2) , Space complexity : O(n)
    n = len(A)

    memory = defaultdict(list) #Allows append values when a key value does not exist still
    sum_so_far = 0

    memory[sum_so_far].append(-1)
    solutions = []

    for i in range(n):
        sum_so_far += A[i]

        if (sum_so_far-k) in memory.keys():
            indexList = memory[sum_so_far-k]
            for indexStart in indexList:
                 solutions.append(A[indexStart+1:i+1])

        memory[sum_so_far].append(i)

   
    return solutions


if __name__ == "__main__":

    A = [3, 4, -7, 1, 3, 3, 1]
    k = 7

    print(brute_force(A,k))
    print(cumulative_sum(A,k))
    print(hashmap(A,k))


