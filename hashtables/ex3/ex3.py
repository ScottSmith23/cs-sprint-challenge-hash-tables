def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    #get total count for all numbers in the lists
    for array in arrays:
        newlist = list(dict.fromkeys(array))
        for i in newlist:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
    #adds to result all numbers that have a count equal to number of lists
    result = [key for (key,value) in cache.items() if value == len(arrays)]


    return result


# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))

arrays = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]

print(intersection(arrays))