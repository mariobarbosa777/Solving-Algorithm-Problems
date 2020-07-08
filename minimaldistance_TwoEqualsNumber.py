def Min_Distance_two_equals_numbers(arr):
    
    from collections import defaultdict
    
    min_distance_so_far = -1

    memory = defaultdict(list)  #To append the index in a list  

    for i in range(len(arr)):
        if arr[i] in memory.keys():
            for index in memory[arr[i]]:
                distance = i-index
                if min_distance_so_far == -1: 
                    min_distance_so_far=len(arr)
                if distance <  min_distance_so_far:
                    min_distance_so_far = distance
        memory[arr[i]].append(i)

    return min_distance_so_far 


if __name__ == "__main__":

    arr = [7, 0, 2, 4, 5, 6, 7]

    print(Min_Distance_two_equals_numbers(arr))
