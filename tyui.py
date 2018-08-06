def add_numbers(start,end):
    """
    write the body of this
    function, similar to the block
    of code we just saw. Hint:
    don’t forget to use return
    """
    total=0
    for number in range(start,end+1):
        total=total+number
    return total

answer = add_numbers(333,777)
print(answer)


    
