#!/usr/bin/env python   
# -*- coding: utf-8 -*-


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# 求链表的中间结点
# 思路1：利用快慢结点，当快结点到达尾结点时,慢结点即为中间结点
def middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print(slow.val)
    return slow

middle(n1)
