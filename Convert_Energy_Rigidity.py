# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 03:34:22 2020
@author: Moshe Godfrey Mosotho

----------This code converts energy cutoffs to rigidity cutoffs and vice versa-------------

Source:-
H. Moraal
Space Research Centre, North-West University, Potchefstroom 2520, South Africa
Publication title : Cosmic-Ray Modulation Equations
Publication year : 2011
DOI 10.1007/s11214-011-9819-3
"""
#! \usr\home\python


from __future__ import division
import math



def Rig(Particle,T):
    if Particle=='Proton':
        A,Ze,E0=1.,1.,0.938
    elif Particle=='Electron':
        A,Ze,E0=2.,1.,0.00511
    elif Particle=='Helium':
        A,Ze,E0=1.,1.,0.93184475
    else:
        print ' '
        print ' '
        print ' '
        print ' Your selection is Invalid !!!  >>>>>>>>>>><<<<<<<<<<<<< '
        print ' '
        print ' '
    Rig=float(A/Ze)*(math.sqrt(float(T)*float(T) + 2.*float(T)*float(E0)))
    return Rig

 
def KE(Particle,P):
    if Particle=='Proton':
        A,Ze,E0=1.,1.,0.938
    elif Particle=='Electron':
        A,Ze,E0=2.,1.,0.00511
    elif Particle=='Helium':
        A,Ze,E0=1.,1.,0.93184475
    else:
        print ' '
        print ' '
        print ' '
        print ' Your selection is Invalid !!!  >>>>>>>>>>><<<<<<<<<<<<< '
        print ' '
        print ' '
    Energ=math.sqrt((float(Ze/A)**2.)*float(P)**2. + float(E0)**2.) - float(E0)
    return Energ

print ' '
print ' '
print " Cutoff - Select Calculation "
print "(1) Rigidity to Kinetic energy"
print "(2) Kinetic energy to Rigidity"
print "!----------------------------------------!"

print ' '
Input=raw_input("Choice: ")
if Input=="1":
    SD=str(raw_input("Particle e.g. Electron: "))
    Inputs=raw_input("Rigidity in GV (you can give several Rigidites seperated by ','): ")
    Inputs+=","
    print ' '
    print 'Results :'
    print 'Rigidity [GV] ===> Kinetic energy [GeV/n]'
    for Input in Inputs.split(","):
        if Input==[] or Input==''or Input==' ':
            pass
        else:
            PrinT=Rig(SD,Input)
            print Input,'  ===>  ',PrinT
    print ' '

print ' '
if Input=="2":
    SD=str(raw_input("Particle e.g. Electron: "))
    Inputs=raw_input("Kinetic energy, T in GeV (you can give several T's seperated by ','): ")
    Inputs+=","
    print ' '
    print 'Results :'
    print 'Kinetic energy [GeV/n] ===> Rigidity [GV]'
    for Input in Inputs.split(","):
        if Input==[] or Input==''or Input==' ':
            pass
        else:
            PrinT=KE(SD,Input)
            print Input,'  ===>  ',PrinT
    print ' '
