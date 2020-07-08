def ismountainArray(arr):

    len_arr = len(arr)

    i = 0

    while i+1 < len_arr and arr[i] < arr[i+1]:
        i += 1
        
    if i == 0 or i == len_arr-1:
        return False
    
    while i+1 < len_arr and arr[i] > arr[i+1]:
        i += 1

    return i == len_arr-1
        

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 3, 2, 1]
    print(ismountainArray(arr))
