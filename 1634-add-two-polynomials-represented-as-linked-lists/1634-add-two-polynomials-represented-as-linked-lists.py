# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def remove_zeros(self, poly):
        start = None
        while poly is not None:
            if poly.coefficient != 0:
                start = poly
                break
            else:
                poly = poly.next
        if start is None:
            return None
        res = start

        while start.next is not None:
            if start.next.coefficient != 0:
                start, start.next = start.next, start.next.next
            else:
                start.next = start.next.next

        return res

    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        if poly1 is None:
            return poly2
        if poly2 is None:
            return poly1
        if poly1.power < poly2.power:
            poly1, poly2 = poly2, poly1
        res = poly1

        while (poly1 and poly2):
            if poly1.power == poly2.power:
                poly1.coefficient = poly1.coefficient + poly2.coefficient
                poly2 = poly2.next
            elif poly1.power > poly2.power:
                if poly1.next is None:
                    poly1.next = poly2
                    return self.remove_zeros(res)
                else:
                    if poly1.next.power >= poly2.power:
                        poly1 = poly1.next
                    else:
                        temp = poly1.next
                        poly1.next = poly2
                        poly2 = temp
                        poly1 = poly1.next
        return self.remove_zeros(res)
        




        
        