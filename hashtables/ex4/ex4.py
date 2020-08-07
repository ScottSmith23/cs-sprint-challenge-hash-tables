def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = dict.fromkeys(a)
    for i in a:
        #checks if i has a negative counterpart in the cache
        if -i in cache and i > 0:
            result.append(i)
   

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
