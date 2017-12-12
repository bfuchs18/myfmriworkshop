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
def main():
    #load in all global variables prepro needs, right now this is the path to the data
    basedir='Users/barifuchs/UNCworkshop_data/ds000030_R1.0.5'
    prepro(basedir) #call prepro to do cool things
    
main()
#runs main, which runs basedir (we defined basedir in main)
#main holds global variable (basedir)