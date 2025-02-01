def balancedOrNot(ex, maxReplace):
    pointers = {'<': '>'}
    pairs = []  

    for i in ex:
        if i in pointers.keys():
            pairs.append(i)
        elif i in pointers.values():
            if pairs and pointers[pairs[-1]] == i:
                pairs.pop() 
            else:
                return 0

    unbalanced_count = len(pairs)

    if unbalanced_count <= maxReplace:
        return 1  # balanced
    else:
        return 0  # unbalanced


print(balancedOrNot("<><>", 1))  
print(balancedOrNot("<<<><>", 1))  
print(balancedOrNot("<<>>", 1))   
print(balancedOrNot("<<<>", 2)) 
print(balancedOrNot("><", 0))