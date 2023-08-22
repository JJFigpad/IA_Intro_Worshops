"""
Created on Sun Aug 20 22:31:01 2023

@author: Juan Jose Figueroa Padilla, Fabian Eduardo Suarez
"""

class Agente_Aspiradora_simple:
    """
    Clase que representa a una aspiradora como agente reflexivo simple
    
    """
    
    def __init__(self, initial_state, environment):
        self.pos = initial_state
        self.env = environment
        self.dic = dict(environment)
        self.n = len(self.env)
    
    def accion(self):
        """
        

        Returns
        -------
        bool
            Retorna verdadero si ya limpio todos los cuartos que lo
            necesitaban.
        
        list
            Retorna la lista que representa el estado del ambiente al final
            de limpiar o moverse.

        """
        for i in range(self.n):
            if self.dic[i] == 0:
                break
            elif self.dic[i] == 1 and i == self.n-1:
                print("Done")
                return True
        print("Estado inicial =", self.env)
        if self.dic[self.pos] == 0: 
            self.dic[self.pos] = 1
            self.env[self.pos][1] = 1
            print("Limpiar cuarto", self.pos)
            print("Estado actual =", self.env)
        elif self.dic[self.pos] == 1:
            print("Ir al siguiente cuarto")
            self.pos += 1
            self.pos = self.pos%self.n
        return self.env

aspiradora1 = Agente_Aspiradora_simple(1, [[0,0],[1,0],[2,1]])
while aspiradora1.accion() != True:
    continue