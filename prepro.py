#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:11 2017

@author: barifuchs
"""

import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil





def prepro(basedir):
    #do something cool
    print('Data is in path '+basedir)
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*.nii.gz')):
        input=item
        output_path=item.strip('.nii.gz')
        output=output_path+('_brain')
        os.system("/usr/local/fsl/bin/bet %s %s -F"%(input, output))
        pdb.set_trace()
    
def main():
    #load in all global variables prepro needs, right now this is the path to the data
    basedir='Users/barifuchs/UNCworkshop_data/ds000030_R1.0.5'
    prepro(basedir) #call prepro to do cool things
    
main()
#runs main, which runs basedir (we defined basedir in main)
#main holds global variable (basedir)

print(os.system('echo $FSLDIR'))

#input='/Users/barifuchs/UNCworkshopdata/ds000030_R1.0.5/<subject number>/func/<nifiti_file>'

input=glob.glob('/Users/barifuchs/UNCworkshopdata/ds000030_R1.0.5/sub-*/func/sub-*.nii.gz')
print(input[0:10])
len(input)

#x=input[1]
#print('my path is '+x)
#y=x.split('/')
#print (y)
#whatcomp=y[2]
#sub=y[5]
#print sub

sub=input[1].split('/')[5]
print(sub)

subtask=input[1].split('/')[7].split('.')[0]
#subtask=subtask.strip('.nii.gz')
print(subtask)

output=subtask+'_brain'
print(output)

#os.system('bet' x output '-F') 
#print(x)
#print(output)
os.system('bet %s %s -F'%(x, output))

input=glob.glob('/Users/barifuchs/UNCworkshop_data/ds000030_R1.0.5/sub-*/func/sub-*.nii.gz')
print input