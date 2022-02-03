"""
Desplay function
"""


c ='Current PDB: '
x= 'None'
y= c + x
def display1():
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
    print('{:7s} {:>90s} {:s}'.format('*',y,'*' ))
    print('*' *100)
    x=input(':' )
    return x

"""
validate pdb file
"""
def validpdb(file):
    with open(file) as pdb:
       # flag =True
        count=0
        for line in pdb:
            if line.startswith('HEADER') and len(line) == 81:
                #flag =True
                count+=1
            if line.startswith('MASTER') and len(line)==81:
                count+=1
             #   flag=True
        return count






"""
trial program
"""

#b=display1().lower()
options= "'1','2','3','4','5','6','o','i','h','s','q'"
for b in options:
# while b !='q':
    b=display1().lower()
#ext = "'q','6'"

    if b in "'1','2','3','4','5','o','i','h','s'":
       # b=display1()
        if b =='1'or b=='o':
            opened=input("Please enter file name: ")
            #filename=pathname[-1]
            valid=validpdb(opened)
            if valid==2:
                pathname=opened.split('/')[-1]
                y=('Current PDB: '+ pathname)
            
                print('valid pdb file',pathname,"\n")
                #display1().lower()
                # with open(opened) as file:

                #     b=display1().lower()
                # if opened == 'yes':
                #     filename=input('file exit press yes ' )
                #     if filename =='yes':
                #         print("current file updated")
                #     else: pass
            
            else:
                print('invalid pdb file please enter another file')
                #b=display1().lower()

    if b in "'q','5'":

        leave = input("Are sure you want to exit the program?\nEnyter y/n to exit/ go back to the menu: ")
        if leave.lower()== 'n':
            pass
            # b=display1().lower()
            # b=display1().lower() 
            #break 
        elif leave.lower() == 'y':
            break  

        elif leave != 'n' or leave != 'y':
            leave=input('invalid input\nEnyter y/n to exit/stay: ')    
        # elif leave.lower() == 'y':
        #     break
        
    else:
        print('invalid option:' )    
        # print(display1().lower())

