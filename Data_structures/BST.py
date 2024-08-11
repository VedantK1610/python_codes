# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:41:26 2023

@author: VEDANT
"""

class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None 
    
    def add_child(self,data):
        if data==self.data:
            return 
        
        if data<self.data:
            if self.left:
                self.left.add_child(data) 
            else:
                self.left=BST(data) 
        else:
            if self.right:
                self.right.add_child(data) 
            else:
                self.right=BST(data) 
     
    def in_order(self):
        elements=[]
           #visit left 
        if self.left:
            elements+=self.left.in_order()
           
           #visit root 
        elements.append(self.data)
        
           #visit right
        if self.right:
            elements+=self.right.in_order()
        
        return elements 
    
    def find_min(self):
        if self.left is None:
            return self.data 
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data 
        return self.right.find_max()
    
    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left.delete(val)
            else:
                return None
        elif val>self.data:
            if self.right:
                self.right.delete(val) 
            else:
                return None
        else:
            if self.left is None and self.right is None:
                return None 
            if self.left is None:
                return self.right 
            if self.right is None:
                return self.left 
            min_val=self.right.find_min()
            self.data=min_val
            self.right.delete(min_val)
        return self    

def build_tree(elements):
    root=BST(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root    

if __name__=="__main__":
    nums=[17,4,1,20,9,23,18,34]   
    tree=build_tree(nums)
    print(tree.in_order())
    print(tree.find_min())
    print(tree.find_max())