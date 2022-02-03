#!/usr/bin/python

import sys

def gene_file(file1,file2):
    """
    Reads the file (humchr.txt) 
    Writes to another file (gene_names.txt) a clean list of gene names.
    """
    with open(file1,'r') as file:
        with open(file2,'w')as myfile:
            count=0
            flag=False      
            for line in file:
            # print(line)
                if line.startswith('_____'):
                    flag=True
                    count+=1
                    continue
                elif line.startswith('-'):
                    flag=False
                elif flag and count==2:
                    myfile.writelines(line.split()[0]+'\n')
                
gene_file(sys.argv[1], sys.argv[2])