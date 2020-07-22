class Solution:
    """
    Division without using multiplication, division or mod operations:

    The idea behind this algorithm is very simple.
    Consider following inequality:
        
    (1)  A - x * B >= 0;

    A is dividend, B is divisor, x is quotient
    The goal here is to find the maximum value of x 
    where above condition is satisfied.
    
    Since every number can be represented as sum of numbers that are power of 2
    We can write down above inequality as follows:
    
    (2)  A - (2^i + 2^j + ... + 2^k) * B >= 0;
    
    So now our goal is reduced down to find those terms(2^i) individually.
    To find a term we should figure out some way perform 
    multiplication (2^i * B) without actual multiplication.
    
    It's clear that 2^p * B = 1 << p * B and B * 1 << p = B << p then
    we can claim following:
    
    (3)  2^p * B = B << p;
    
    So now, we can modify (2) like following:
    
    (4)  A - B << i - B << j - ... - B << k >= 0
    
    From above inequality we can come up with following algorithm:
        
        1.  A = A - B << 31
        2.  A = A - B << 30
        3.  A = A - B << 29
            ...
        31. A = A - B << 0
    
    """
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = dividend < 0 < divisor or dividend > 0 > divisor
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        for power in range(31, -1, -1):
            term = divisor << power
            if dividend >= term:
                dividend -= term
                quotient += 1 << power
        if is_negative:
            quotient = -quotient
        return min(max(quotient, -1 << 31), (1 << 31) - 1)
