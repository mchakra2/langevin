# -*- coding: utf-8 -*-
import sys
import math
import numpy as np
import os
import random

kb=1
mass=1
D=2
init_pos=D*random.random()
init_vel=4
T=1
L=.5
dt=.01
N=200
os.getcwd()
Pot_file='./docs/Pot_Example.txt'
data= np.loadtxt(Pot_file)
'''
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
    os.getcwd()
    Pot_file='./docs/Pot_Example.txt'
    data= np.loadtxt(Pot_file)



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
        p=self.warp(p)
        temp_p=p+(self.dt*v)
        temp_p=langevin_dynamics.wrap(temp_p)
        ff = np.interp(p, data[:,1],data[:,3]) #force from the input potential
        std_dev=math.sqrt(2*self.T*self.kb*self.L)
        eta=random.gauss(0,std_dev)
        if switch==0:#Turning langevin dynamics off
            force=ff
        else:
            force=-(self.L*v)+eta+ff

            #print(force,v)
            v=v+(dt*force/mass)
    
        return(temp_p,v)
       
    
    
    
if __name__ == "__main__":
    #f=Langevin()
    main()
 
'''

def wrap(pos,PBC):
    pp=pos%PBC
    if pp < 0:
        return(PBC-pp)
    return (pp)
'''
def tab_match(pos):
    a=np.interp(pos, data[:,1],data[:,3])
    return(a)
'''

def euler(p,v,switch):
    if type(switch)!=int:
        print("Switch has to be an integer")
        raise TypeError
    temp_p=p+(dt*v)
    #temp_p=wrap(temp_p)
    ff = np.interp(p, data[:,1],data[:,3]) #force from the input potential
    std_dev=math.sqrt(2*T*kb*L)
    eta=random.gauss(0,std_dev)
    if switch==0:#Turning langevin dynamics off
        force=ff
    else:
        force=-(L*v)+eta+ff
        print("In Langevin")

    #print(force,v)
    v=v+(dt*force/mass)
    return(ff,force)
    #return(temp_p,v)

