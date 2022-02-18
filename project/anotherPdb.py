
filename = 'None'

def display():
    """
    Desplay function

    """    
    curr_filename = f'Current PDB:{filename}'

    print('*' * 100),
    print('*', 'PDB FILE ANALYZER',' '*78,'*')
    print('*' * 100)
    print('*', 'select an option from below:',' '*68 +'*') 
    print('*', ' '*96, '*')
    print('{:7s} {:2s} {:30s} {:>4s} {:51s} {:s}'.format('*' , '1)','Open a pdb file','(O)',' ', '*' ))
    print('{:7s} {:2s} {:30s} {:>4s} {:51s} {:s}'.format('*' , '2)','Information' ,'(I)',' ', '*' ))
    print('{:7s} {:2s} {:30s} {:>4s} {:51s} {:s}'.format('*' , '3)','Show histogram of amino acids' ,'(H)',' ', '*' ))
    print('{:7s} {:2s} {:30s} {:>4s} {:51s} {:s}'.format('*' , '4)','Diplay secondary structure' ,'(S)',' ', '*' ))
    # print('{:7s} {:2s} {:30s} {:>4s} {:51s} {:s}'.format('*' , '5)','Export PDB file' ,'(X)',' ', '*' ))
    print('{:7s} {:2s} {:30s} {:>4s} {:51s} {:s}'.format('*' , '5)','Exit' ,'(Q)',' ', '*' ))
    print('{:7s} {:>90s} {:s}'.format('*',curr_filename,'*' ))
    print('*' *100)
    opts=input(':' )
    return opts
display()
filename= "pdb"
display()