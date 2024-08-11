# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 10:40:59 2023

@author: VEDANT
"""

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None 
        
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
      
    def print_tree(self):
        spaces=' '* self.get_level()*2
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
        
    def get_level(self):
        p=self.parent 
        level=0
        while p:
            level+=1 
            p=p.parent 
        return level 
    
def build_tree():
    root=TreeNode("Electronics")
    
    laptop=TreeNode("laptop")
    laptop.add_child(TreeNode("idealpad"))
    
    mobile=TreeNode("mobile")
    mobile.add_child(TreeNode("tab"))
    mobile.add_child(TreeNode("heymob"))
    
    home=TreeNode("home")
    home.add_child(TreeNode("fridge"))
    home.add_child(TreeNode("tv"))
    
    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(home)
    
    mac=TreeNode("mac")
    mac.add_child(TreeNode("8 GB"))
    mac.add_child(TreeNode("16 GB"))
    laptop.add_child(mac)
    
    
    return root
if __name__=="__main__":
    root=build_tree()
    root.print_tree()    
    pass