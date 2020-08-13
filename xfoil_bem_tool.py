"""
Authors: Andrew Vigne, George Loubimov

Script to quickly extract Re vs. AoA, Cl, and Cd
for any given airfoil geometry using XFoil.
Made for Blade Element Momentum virtual disks.

Created: 8/13/2020
"""

from subprocess import Popen, PIPE, STDOUT
import numpy as np
import itertools as itr
import csv

def xfoil_interact(foil, re, alfa_strt, alfa_end, alfa_step):   
    def get_cmd(foil, re, alfa_strt, alfa_end, alfa_step):
        
        if foil is not None:
            load_cmd = 'LOAD ' + foil
        else:
            load_cmd = 'NACA 0012'
        cmd = '''    
        {}
        
        OPER
        VISC {}
        ITER
        1000
        PACC
        OUTPUT/{}_SAVE
        
        ASEQ
        {}
        {}
        {}
        
        '''.format(load_cmd, re, re, alfa_strt, alfa_end, alfa_step)
        
        return cmd
    
    p = Popen(['C:\\XFoil\\xfoil.exe'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
    stdout = p.communicate(input=get_cmd(foil=foil, re=re, alfa_strt=alfa_strt, 
                                         alfa_end=alfa_end, 
                                         alfa_step=alfa_step).encode())[0]
    print(stdout)
    print('=====================================================')
    
    return None

######################## PARAMETERS ########################

re_strt = 200000
re_end = 270000
re_step = 10000
re_num = int((re_end-re_strt)/re_step) + 1


alfa_strt = 0
alfa_end = 10
alfa_step = 5
alfa_num = int((alfa_end-alfa_strt)/alfa_step) + 1

foil = None # None or file name 'example.dat'

tbl = np.zeros([int(re_num*alfa_num), 4]) # main output in csv

############################################################

i = 0
for re in range(re_strt , re_end+re_step, re_step):
    xfoil_interact(foil, re, alfa_strt, alfa_end, alfa_step)
    i = i + 1
    tbl_end = alfa_num*i
    
    if i == 1:
        tbl_strt = 0
    else:
        tbl_strt = alfa_num*i-alfa_num
        
    aa_list = []
    cl_list = []
    cd_list = []
    
    tbl[tbl_strt:tbl_end,0] = re  # stores set of Reynolds
    
    with open('output/{}_save'.format(re),'r') as infile:
        for x in itr.islice(infile, 12, None): # ignores first 13 lines
            x = x.split()
            aa_list.append(float(x[0]))
            cl_list.append(float(x[1]))
            cd_list.append(float(x[2]))
            
    tbl[tbl_strt:tbl_end,1] = aa_list
    tbl[tbl_strt:tbl_end,2] = cl_list
    tbl[tbl_strt:tbl_end,3] = cd_list
    
outfile = open('output/outfile.csv', 'w+', newline = '')
with outfile:
    write = csv.writer(outfile)
    write.writerows(tbl)

