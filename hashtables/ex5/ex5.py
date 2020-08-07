# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    lasts = []
    result = []
    for path in files:
        final = path.split("/")
        lasts.append(final[-1])
    for i in lasts:
        if i in queries:
            result.append(i)


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
