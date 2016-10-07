# -*- coding: utf-8 -*-
import sys
import math
import numpy as np
import os
import random
import warnings


class Langevin:

    #Set of default parameters/ file locations
    kb=1
    mass=1
    D=2
    init_pos=D*random.random()
    init_vel=1
    T=1
    L=.5
    dt=.01
    N=200
    os.getcwd()
    Pot_file='./IOFiles/Pot_Example.txt'
    data= np.loadtxt(Pot_file)

    o_file="./IOFiles/output.txt"

    input_f='./IOFiles/input.txt'

    def main(self):
        
        self.parameters(self.input_f)#Calling the parameters function to apply the user specified values
           
        pos=self.wrap(self.init_pos,self.D)
        vel=self.init_vel
        index=0
        t=0
        p=0
        v=0
        f=open(self.o_file,"w")#Writing into the output file
        f.write('#index   time   position  velocity \n {0:d}  {1:4f}  {2:3f}  {3:4f}\n'.format(index, t, pos,vel))
        
        while(t<=(self.N*self.dt)):
            p=pos
            v=vel
            frc,dU=self.force(p,v,1)
            pos,vel=self.euler(p,v,frc)
            pos=self.wrap(pos,self.D)
            index+=1

            t=t+self.dt
            f.write('{0:d}  {1:4f}  {2:3f}  {3:4f}\n'.format(index, t, pos,vel))
        f.close()
        print("Final Position: ",pos,"Final velocity: ",vel,"Output file: ",self.o_file)

    def wrap(self,pos,PBC):
        pp=pos%PBC
        return (pp)
    
    def euler(self,p,v,frc):
       
        temp_p=p+(self.dt*v)
        v=v+(self.dt*frc/self.mass)
        return(temp_p,v)

    
    def force(self,p,v,switch):
        ff = np.interp(p, self.data[:,1],self.data[:,3]) #force from the input potential
        std_dev=math.sqrt(2*self.T*self.kb*self.L)
        eta=random.gauss(0,std_dev)
        if switch==0:#Turning langevin dynamics off
            force=ff
            
        else:
            force=-(self.L*v)+eta+ff
       
        return(force,ff)

    def parameters(self,in_file):
        if os.path.exists(in_file)!= True:
            print ("The input file path does not exist. Default values will be used")
            raise IOError
        f = open(in_file)
        
        for line in f:

            if "=" in line:
                if line.split("=")[0]=='D':
                    self.D=float(line.split("=")[1])
                elif line.split("=")[0]=='init_pos':
                    self.init_pos=float(line.split("=")[1])
                elif line.split("=")[0]=='init_vel':
                    self.init_vel=float(line.split("=")[1])
                elif line.split("=")[0]=='T':
                    self.T=float(line.split("=")[1])
                elif line.split("=")[0]=='L':
                    self.L=float(line.split("=")[1])
                elif line.split("=")[0]=='dt':
                    self.dt=float(line.split("=")[1])
                elif line.split("=")[0]=='N':
                    self.N=float(line.split("=")[1])
                elif line.split("=")[0]=='Pot_file':
                    self.Pot_file=line.split("=")[1].rstrip()

                    if os.path.exists(self.Pot_file)== False:
                        print("The Potential Energy file does not exist")
                        raise IOError
                elif line.split("=")[0]=='o_file':
                    self.o_file=line.split("=")[1].rstrip()
                    if os.path.exists(self.Pot_file)== True:
                        warnings.warn("A file named "+self.o_file +" already exists. Overwriting the file with output")



