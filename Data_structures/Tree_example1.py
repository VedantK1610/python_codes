# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:06:14 2023

@author: VEDANT
"""

class TreeNode:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.children=[]
        self.parent=None 
     
    def add_child(self,child):
        child.parent=self 
        self.children.append(child)
        
    def print_tree(self,argument):
        if argument=='name':
            value=self.name
        if argument=='designation':
            value=self.designation
        if argument=='both':
            value=self.name + '(' + self.designation + ')'
        
        level=self.get_level()
        spaces=' '*level *2
        
        print(spaces + value)
        if self.children:
            for child in self.children:
                child.print_tree(argument)
                
    def get_level(self):
         level=0 
         p=self.parent
         while p:
             level+=1 
             p=p.parent 
         return level    
        
def built_tree():
    ceo=TreeNode("Vedant", "CEO")
    
    cto=TreeNode("Chinmay", "CTO")
    
    infra_head=TreeNode("Vishwa", "Infrastructure head")
    infra_head.add_child(TreeNode("Dhaval","Cloud manager"))
    infra_head.add_child(TreeNode("Abhijit","App manager"))
    
    cto.add_child(infra_head)
    ceo.add_child(cto)
    
    return ceo
    
if __name__=="__main__":
    root=built_tree()
    root.print_tree("name")
    pass