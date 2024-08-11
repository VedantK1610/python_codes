# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 11:15:21 2023

@author: VEDANT
"""

class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.dic={}
        for start,end in self.edges:
            if start in self.dic:
                self.dic[start].append(end)
            else:
                self.dic[start]=[end]
        print(self.dic) 
     
    def get_paths(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.dic:
            return []
        
        paths=[]
        for node in self.dic[start]:
            if node not in path:
                new_path=self.get_paths(node, end ,path)
                for p in new_path:
                    paths.append(p)
        return paths        
                
 
if __name__=="__main__":
    routes=[
        ("mumbai","paris"),
        ("mumbai","dubai"),
        ("paris","dubai"),
        ("paris","new york"),
        ("dubai","new york"),
        ("new york","toronto")
        
        ]
    route_graph=Graph(routes)
    print(route_graph.get_paths("mumbai", "new york"))