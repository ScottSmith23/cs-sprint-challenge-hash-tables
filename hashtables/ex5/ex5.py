# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    #creates a dict with queries as keys
    cache = dict.fromkeys(queries)
    result = []
    
    for path in files:
        #splits each path into an array so the destination (last item in array) can be read
        patharr = path.split("/")

        #checks if destination is in the cache and if true appends the path to result
        if patharr[-1] in cache:
            result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
