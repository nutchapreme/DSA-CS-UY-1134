def count_lowercase(s,low,high):
    if low == high:
        if ord('a')<=ord(s[low]):
            return 1
        else:
            return 0
    if ord('a')<=ord(s[low]):
        return 1+count_lowercase(s,low+1,high)
    return count_lowercase(s,low+1,high)

def is_number_of_lowercase_even(s, low, high):
    if low == high:
        return not ord('a')<=ord(s[low])
    else:
        if ord('a')<=ord(s[low]):
            return not is_number_of_lowercase_even(s, low+1, high) and True
        else:
            return is_number_of_lowercase_even(s, low+1, high)

    

    