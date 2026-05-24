def factors(nums):
    for i in range(1,(int(nums**0.5)+1)):
        if nums%i == 0:
            yield i
    for i in range((int(nums**0.5)),0,-1):
        if nums**0.5 != i:
            if nums%i == 0:
                yield int(nums/i)
    
    