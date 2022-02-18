# #!/usr/bin/env python

import pdbfuntions as pdb

# curr_filename = 'Current PDB: None'
# def display():
#     """
#     Desplay function

#     """
#     # global curr_filename
#     curr_filename = 'Current PDB: None'

#     print('*' * 100),
#     print('*', 'PDB FILE ANALYZER',' '*78,'*')
#     print('*' * 100)
#     print('*', 'select an option from below:',' '*68 +'*') 
#     print('*', ' '*96, '*')
#     print('{:7s} {:2s} {:30s} {:>4s} {:51s} {:s}'.format('*' , '1)','Open a pdb file','(O)',' ', '*' ))
#     print('{:7s} {:2s} {:30s} {:>4s} {:51s} {:s}'.format('*' , '2)','Information' ,'(I)',' ', '*' ))
#     print('{:7s} {:2s} {:30s} {:>4s} {:51s} {:s}'.format('*' , '3)','Show histogram of amino acids' ,'(H)',' ', '*' ))
#     print('{:7s} {:2s} {:30s} {:>4s} {:51s} {:s}'.format('*' , '4)','Diplay secondary structure' ,'(S)',' ', '*' ))
#     # print('{:7s} {:2s} {:30s} {:>4s} {:51s} {:s}'.format('*' , '5)','Export PDB file' ,'(X)',' ', '*' ))
#     print('{:7s} {:2s} {:30s} {:>4s} {:51s} {:s}'.format('*' , '5)','Exit' ,'(Q)',' ', '*' ))
#     print('{:7s} {:>90s} {:s}'.format('*',curr_filename,'*' ))
#     print('*' *100)
#     opts=input(':' )
#     return opts
              
"""
program
"""

# filename = ' None'
options= "'1','2','3','4','5','6','o','i','h','s','q'"

for opt in options:
    global filename
    opt=pdb.display().lower()
    # if opt==None:
    #     print('No option Selected')
    #     break
                
    # else:   # opt=pdb.display().lower()
    if opt in "'q','5'":
        exit_status=pdb.Exit(opt)
        if exit_status==True:
            break
        
    elif opt in "'1','o'":
        opened=input("Enter a Valid PATH for a PDB File: ")
        valid=pdb.validpdb(opened)
        # print(valid)

        if valid==2:
                pathname=opened.split('/')[-1]
                
                filename = pathname
                print(filename)
                
                print(f'The File {pathname} has been successfully loaded')
                with open(opened) as fh:
                    f=fh.readlines()
                    pass
                # pdb.display().lower
                # display().lower()

        else:print("File not a PDB File ")
        # if curr_filename =='None'
    elif opt in "'2','i'":
        try:
            pdb.information(f,pathname)
        except NameError:
            print('No Opened Pdb File')

    elif opt in "'3','h'":
        pdb.hist_menu()
        try:
            pdb.histogram(f)
        except NameError:
            print('No Opened Pdb File')

# # else:opt=input('Invalid option\nPlease choose from the menu option')

# main_pdb()  
        
