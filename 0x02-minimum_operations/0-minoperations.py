#!/usr/bin/python3
'''The minimum operations steps.
Print 'H', end=''
initialized the first copy and paste then print 'H', end=''
do it all over again
'''


def minOperations(n):
    if not isinstance(n, int):
        return 0
    num_ops = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            num_ops += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            num_ops += 2
        elif clipboard > 0:
            done += clipboard
            num_ops += 1
    return num_ops
