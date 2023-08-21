#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 22:31:01 2023

@author: jjfigpad
"""

class Agente_Aspiradora_simple:
    
    def __init__(self, initial_state, environment):
        self.pos = initial_state
        self.env = environment
        self.dic = dict(environment)
    
    def accion(self):
        print("Initial state =", self.env)
        while(True):
            if self.dic[0] == self.dic[1] == 1:
                break
            if self.dic[self.pos] == 0: 
                self.dic[self.pos] = 1
                self.env[self.pos][1] = 1
                print("Clean room", self.pos)
                print("Actual state =", self.env)
                if self.dic[(self.pos+1)%2] == 1:
                    break
            self.pos += 1
            self.pos = self.pos%2
            print("Move to room", self.pos)
            print("Actual state =", self.env)
        return self.env

aspiradora1 = Agente_Aspiradora_simple(0, [[0,0],[1,0]])
aspiradora2 = Agente_Aspiradora_simple(0, [[0,1],[1,0]])
aspiradora3 = Agente_Aspiradora_simple(0, [[0,0],[1,1]])
aspiradora4 = Agente_Aspiradora_simple(0, [[0,1],[1,1]])
print(aspiradora1.accion())
print(aspiradora2.accion())
print(aspiradora3.accion())
print(aspiradora4.accion())