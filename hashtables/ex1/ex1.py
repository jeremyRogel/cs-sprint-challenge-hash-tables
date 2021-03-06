def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    data = {}
    for i in range(len(weights)):
        data[weights[i]] = i
    for i in range(len(weights)):
        dif = limit-weights[i]
        if dif in data:
            return(max(i, data[dif]), min(i, data[dif]))
            
    return None
