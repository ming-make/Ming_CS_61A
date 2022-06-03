from unittest import result


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    count = 1
    while count <= k:
          result = result * n
          n = n - 1
          count = count + 1
    return result



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    str_y = str(y)
    result = 0
    for i in str_y:
        result += int(i)
    return result



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    str_n = str(n)
    len_n = len(str_n)
    flag = True
    i = 0
    while i <= len_n-1:
        if str_n[i]=='8':
            if i+1 <= len_n-1:
            	if str_n[i+1] == '8':
                	return flag
        i = i + 1
    flag = False
    return flag
