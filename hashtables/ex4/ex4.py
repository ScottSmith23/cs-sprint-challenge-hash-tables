def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    for i in a:
        cache[i] = i
        #checks if i has a negative counterpart in the cache
        if i !=0 and -i in cache:
            result.append(abs(i))
   

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
