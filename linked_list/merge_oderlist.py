#!/usr/bin/env python   
# -*- coding: utf-8 -*-

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

n1 = Node(1)
n2 = Node(6)
n3 = Node(9)
n1.next = n2
n2.next = n3

m1 = Node(3)
m2 = Node(7)
m1.next = m2

# 合并两个有序链表
# 思路：利用递归，两个链表l1,l2, 先对分别对第一结点比较，小的为头结点，关系：newhead = merge(l1.next,l2)或newhead = merge(l1,l2.next) 剩下的结点再比较
def merge(l1,l2):
    # 递归终止条件
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val <= l2.val:
        ret = l1
        ret.next = merge(l1.next, l2)
    else:
        ret = l2
        ret.next = merge(l1, l2.next)
    return ret

ret = merge(n1,m1)
while ret:
    print(ret.val)
    ret = ret.next
