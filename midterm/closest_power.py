def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    e = 0
    smallest_err = abs(base**e - num)
    e += 1
    while True:
        err = abs(base**e - num)
        #print('{0}**{1}-{2} = {3}'.format(base, e, num, err))

        if err >= smallest_err:
            break
        else:
            smallest_err = err
            e += 1
    return e-1

print(closest_power(16, 136))