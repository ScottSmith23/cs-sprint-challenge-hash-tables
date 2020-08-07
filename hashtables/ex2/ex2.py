#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    #initialize array
    route = []
    cache = {}

    #map ticket source to key and destination to value
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    #set initial current to first location that has key "NONE"
    current = cache["NONE"]

    #set all locations in route by using destination as next key
    for i in range(length):
        route.append(current)
        current = cache[current]


    
    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_4 = Ticket("DCA", "PAN")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("PAN", "NONE")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4]

print(reconstruct_trip(tickets, 4))

