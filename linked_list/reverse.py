#!/usr/bin/env python   
# -*- coding: utf-8 -*-

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3

# 单链表反转

# 思路1：先用数组存储链表的值，再反向取数组值建立新链表，空间复杂度O(n)，时间复杂度O(n)
def reverse_linkedlist1(head):
    if head == None or head.next == None:  #边界条件判断
        return head
    attr = []
    while head:
        attr.append(head.val)
        head = head.next
    newhead = Node(0)
    tmp = newhead
    for i in attr[::-1]:
        tmp.next = Node(i)
        tmp = tmp.next
    return newhead.next

# 思路2: 从链表头部开始遍历链表，逐个改变链表节点指向，空间复杂度O(1),时间复杂度O(n)
def reverse_linkedlist2(head):
    if head == None or head.next == None:
        return head
    cur = head
    newhead = None
    while cur:
        temp = cur.next
        cur.next = newhead  # 改变当前节点指向
        newhead = cur       # 新链表地址
        cur = temp
    return newhead

# 思路3：递归实现，
def reverse_linkedlist3(head):
    # 递归终止条件
    if head == None or head.next == None:
        return head
    newhead = reverse_linkedlist3(head.next)
    head.next.next = head
    head.next = None
    return newhead


newhead = reverse_linkedlist3(n1)
print(n3.val)
print(newhead.val)


