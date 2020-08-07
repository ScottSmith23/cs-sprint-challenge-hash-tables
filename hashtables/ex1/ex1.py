def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i in range(length):
        #get difference of limit and weigth
        diff = limit - weights[i]
        #check if diff is in cache
        if diff in cache:
            #compare which index is higher then return
            if cache[diff] > i:
                return (cache[diff],i)

            else: 
                return (i, cache[diff])
        #stores the weights list index as it's value in cache
        else:
            cache[weights[i]] = i
        


    return None


print(get_indices_of_item_weights([ 4, 6, 10, 15, 16 ],5,21))
