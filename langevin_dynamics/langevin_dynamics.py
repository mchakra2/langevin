# -*- coding: utf-8 -*-
import sys
import math
import numpy as np
import os
import random
class Langevin:
#def main():

    kb=1
    mass=1
    D=2
    init_pos=D*random.random()
    init_vel=4
    T=1
    L=.5
    dt=.01
    N=200
    Pot_file='../docs/Pot_Example.txt'
    '''
    init_pos=float(input("Initial Position"))
    
    init_vel=float(input("Initial Velocity"))
    T=float(input("Temperature"))
    L=float(input("Damping coefficient"))
    dt=float(input("Time step"))
    D=int(input("Integer domain for periodic boundary condition"))
    N=int(input("Number of timesteps the simulation should run"))
    input_file = raw_input("Path of the input file ")
    flag= os.path.exists(input_file)
    if flag == False:
        print ("Input file not found")
        raise IOError
    
    else:
    
        print (input_file + " exists")
    
    
    Pot_file = raw_input("Path of the potential file ")
    flag= os.path.exists(Pot_file)
    if flag == False:
        print ("Potential file not found")
        raise IOError
    
    else:
    
        print (Pot_file + " exists")
    '''
    data= np.loadtxt(Pot_file)
    #def __init__(self):
    #   pass
    #print (data[1])
    def main(self):
        pos=self.wrap(self.init_pos,self.D)
        vel=self.init_vel
        index=0
        t=0
        p=0
        v=0
        f=open("/home/maghesree/CHE477/test.txt","w")
        f.write('index   time   position  velocity \n {0:d}  {1:4f}  {2:3f}  {3:4f}\n'.format(index, t, pos,vel))
        
        while(t<=(self.N*self.dt)):
            p=pos
            v=vel
            pos,vel=self.euler(p,v)
            pos=self.wrap(pos,self.D)
            index+=1
            print(index)
            t=t+self.dt
            f.write('{0:d}  {1:4f}  {2:3f}  {3:4f}\n'.format(index, t, pos,vel))
        f.close()

    def wrap(self,pos,PBC):
        pp=pos%PBC
        if pp < 0:
            return(PBC-pp)
        return (pp)
    def euler(self,p,v):
        temp_p=p+(self.dt*v)
        min_diff=2
        for i in range(self.data.shape[0]):
            diff=abs(self.data[i][1]-p)
            if diff<min_diff:
                min_diff=diff
                nst_i=i
        std_dev=math.sqrt(2*self.T*self.kb*self.L)
        eta=std_dev*random.gauss(0,1)
        #print (eta,self.data[nst_i][3],-(self.L*v))
        force=-(self.L*v)+eta+self.data[nst_i][3]
        print(force,v)
        v=v+(self.dt*force/self.mass)
        p=temp_p
        return(p,v)
        
    
if __name__ == "__main__":
    f=Langevin()
    f.main()
 
