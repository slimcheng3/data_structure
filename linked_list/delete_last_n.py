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

# 删除链表倒数第n个结点
# 思路：双结点法：第一个结点先走n步，第二个结点再开始走，当第一个结点到达尾结点时，第二个结点下一结点即为要删除的结点
def delete(head,n):
    prev = head
    back = head
    while n:
        prev = prev.next
        n-=1
    while prev.next:
        back = back.next
        prev = prev.next
    back.next = back.next.next
    while head:
        print(head.val)
        head = head.next

delete(n1,3)