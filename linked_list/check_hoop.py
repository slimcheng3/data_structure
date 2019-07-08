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
n5.next = n3
# 检测链表是否有环

# 思路1：利用快慢指针,若有环两者必定相遇,时间复杂度O(1)
def check_hoop1(head):
    slow = head
    fast = head
    has_hoop = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_hoop = True
            return has_hoop
    return has_hoop

# 思路2:遍历链表，同时用一个集合存储结点，若下一结点在集合中则存在环，时间复杂度O(n),空间复杂度O(n)
def check_hoop2(head):
    set = {head}
    has_loop = False
    while head and head.next:
        if head.next in set:
            has_loop = True
            return has_loop
        set.add(head)
        head = head.next
    return has_loop

has_loop = check_hoop2(n1)
print("has_loop",has_loop)
