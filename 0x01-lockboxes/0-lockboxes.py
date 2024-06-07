#!/usr/bin/python3
'''n number of locked boxes.'''


def canUnlockAll(boxes):
    '''A method to determines if all the boxes can be opened'''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxT = unseen_boxes.pop()
        if not boxT or boxT >= n or boxT < 0:
            continue
        if boxT not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxT])
            seen_boxes.add(boxT)
    return n == len(seen_boxes)
