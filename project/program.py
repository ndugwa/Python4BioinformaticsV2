#!/usr/bin/env python

"""
Desplay function
"""


c ='Current PDB: '
x= 'None'
y= c + x
def display1():
    """
    Desplay function
    """
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
   
    try:
        with open(file) as fh:
            global pdb
            pdb=fh.readlines()
        count=0
        for line in pdb:
            if line.startswith('HEADER') and len(line) == 81:
            #flag =True
                count+=1
            if line.startswith('MASTER') and len(line)==81:
                count+=1
        return count
    except:
        print("File no found")

#extracting infomation
aa_dict = {'ARG':'R','HIS':'H','LYS':'K','ASP':'D','GLU':'E',
              'SER':'S','THR':'T','ASN':'N','GLN':'Q','CYS':'C',
              'SEC':'U','GLY':'G','PRO':'P','ALA':'A','VAL':'V',
              'ILE':'I','LEU':'L','MET':'M','PHE':'F','TYR':'Y',
              'TRP':'W'}
def information(openedfile):
    
    # with open(filename)as file:
        # fh=file.readlines()
        title_info = ''
        chain = []
        aa_num =[]
        helix=[]
        sheet=[]
        sheet_n=[]
        amino=[]
        amino_dict={}
        ammino_list=[]
        another={}
       # chain_set 
        for line in openedfile:

            if line.startswith('TITLE'):

                p=line.split()

                x=' '.join(p[1:])#extracting TITLE informations 
                title_info += x
            if line.startswith('SEQRES'): #information about the chains
                ammino_list.append(line.split()[4:])
                chain.append(line.split()[2])
                # amino.append(f'{line.split()[2]}{line.split()[4:]}')
                a,b=line.split()[2],line.split()[3]
                # aa_num.append((f'{a}:{b}'))
                
      
         # tittle and chains in the pdb file        
        print('TITTLE:', title_info)
        chains=list(set(chain))
        if len(chains)==2:
            print('CHAINS:',chains[0],'and',chains[1])
        else: print(', '.join(chains))

        
        
#DRAWING A HISTOGRAM        
def histogram():
    print('Choose an option to order by:')
    print('{:2s}{:35s}{:>4s}'.format(' ','number of amino acids - ascending','(an)'))
    print('{:2s}{:34s}{:>4s}'.format(' ','number of amino acids - descending',' (dn)'))
    print('{:2s}{:35s}{:>4s}'.format(' ','alphabetically - ascending', '(aa)'))
    print('{:2s}{:35s}{:>4s}'.format(' ','alphabetically - descending','(da)'))
    global order
    order=input('Order by: ')
    return order



"""
program
"""

#b=display1().lower()
options= "'1','2','3','4','5','6','o','i','h','s','q'"
for b in options:
# while b !='q':
    b=display1().lower()
    if b in "'q','5'":

        leave = input("Do you want to exit(E) or do you want go back to the menu (M): ").lower()
        if leave== 'm':
            pass
            # b=display1().lower()
            # b=display1().lower() 
            #break 
        elif leave == 'e':
            break  

        elif leave != 'e' or leave != 'm':
            leave = input("Ivalid option\nChoose exit(E) or menu (M): ").lower()
#ext = "'q','6'"

    if b in "'1','2','3','4','5','o','i','h','s'":
       # b=display1()
        if b =='1'or b=='o':
            opened=input("Enter a Valid PATH for a PDB File: ")
            #filename=pathname[-1]
            valid=validpdb(opened)
            if valid==2:
                pathname=opened.split('/')[-1]
                y=('Current PDB: '+ pathname)
            
                print(f'The File {pathname} has been successfully loaded')
            else:opened=input("File not a PDB File, Enter another file: ")
             
        
        if b=='2' or b=='i':
            # with open(opened)as file:
                # fh=file.readlines()
            title_info = ''
            chain = []
            aa_num =[]
            helix=[]
            sheet=[]
            sheet_num=[]
            amino=[]
            amino_dict={}
            ammino_list=[]
            another={}
            amino_dict_list=[]
            try:
                for line in pdb:

                    if line.startswith('TITLE'):

                        p=line.split()

                        x=' '.join(p[1:])#extracting TITLE informations 
                        title_info += x
                    if line.startswith('SEQRES'): #information about the chains
                        amino_dict_list.append({line.split()[2]:line.split()[4:]})
                        ammino_list.append(line.split()[4:])
                        chain.append(line.split()[2])
                        amino.append(f'{line.split()[2]}{line.split()[4:]}')
                        a,b=line.split()[2],line.split()[3]
                        aa_num.append((f'{a}:{b}'))


                    # extracting helix
                    if line.startswith('HELIX'):
                        helix.append(line.split()[7])

                  # extracting sheets
                    if line.startswith('SHEET'):
                        sheet_num.append(line.split()[5])
                 # tittle and chains in the pdb file
                print(f'PDB File: {pathname}' )
                print('TITTLE:', title_info)
                chains=list(set(chain))
                chains.sort()
                if len(chains)==2:
                    print('CHAINS:',chains[0],'and',chains[1])
                elif len(chains)==1:
                    print('CHAIN:',', '.join(chains))

                else: print('CHAINS:',', '.join(chains))


    #         CREATING DICTIONARIES OF HELIX COUNT AND SHEET COUNT
                helices={}

                for j in chains:
                    for i in helix:
                        if i == j:

                            helices[i]=helix.count(j)
                        if j not in helix:
                            helices[j]=0

                # sheets={chain_name:sheet_n.count(chain_name) for chain_name in sheet_n}
                sheets={}
                for j in chains:
                    for i in sheet_num:
                        if i == j:

                            sheets[i]=sheet_num.count(j)
                        if j not in sheet_num:
                            sheets[j]=0

                aa_num_dic={}
                aa_n=set(aa_num)
                aa_n=list(aa_n)
                for i in aa_n:
                    aa_num_dic[i[0]]=i[2:]
                
                # helixes={chain_nam:helix.count(chain_nam) for chain_nam in helix}



                one_aa_dict={}
                for i in amino_dict_list:
                    for a,b in i.items():
                        if a in one_aa_dict.keys():
                            one_aa_dict[a]+=b
                        else:
                            one_aa_dict[a]=b
                # print(one_dict)
                amino_seq={k:''.join([aa_dict.get(v) for v in v]) for k,v in one_aa_dict.items()}
            




                seq='Sequence:  '
                for i in chains:

                    print('{:2s}{:6s}{:10s}'.format('-','Chain',i))
                    print('{:3s}{:22s}{:>4}'.format(' ','Number of amino acids:',aa_num_dic.get(i)))
                    print('{:3s}{:22s}{:>4}'.format(' ','Number of helix:',helices.get(i)))
                    if len(sheets)==0:
                        pass
                    else:print('{:3s}{:22s}{:>4}'.format(' ','Number of sheet:',sheets.get(i)))
                    # print('{:3s}{:9s}{:50s}'.format(' ','Sequence:  ',one_aa_dic.get(i)))
                    if len(amino_seq.get(i))>50:
                        for j in range(0,len(amino_seq.get(i)),50):

                            print('{:3s}{:9s}{:50s}'.format(' ',seq,amino_seq.get(i)[j:j+50]))
                            seq=' '*11
                    else:print('{:3s}{:9s}{:50s}'.format(' ','Sequence:  ',amino_seq.get(i)))

            except NameError as name:
                print("No file loaded\nEnter a Valid PATH for a PDB File: ")

    if b=='3' or b=='h':
       
        try:
            histogram()
            ammino_list=[]
            for line in pdb:
                if line.startswith('SEQRES'): #extractint ammino acids
                    ammino_list.append(line.split()[4:])

    # unpacking a nested list of amino acids
            ammino_unpacked=[]
            for i in ammino_list:
                for j in i:
                # a=','.join(i)
                    ammino_unpacked.append(j)


            # ammino_unpacked=list(itertools.chain(*ammino_list))
    #             ammino_unpacked=[]
    #             for i in ammino_list:
    #                 ammino_unpacked.append(i)

            ammino_unpacked.sort()
            dict_alph_asc={aa:ammino_unpacked.count(aa) for aa in ammino_unpacked}
            # print(alph_asc)

            # else: pass
            if order.lower() not in ['aa','da','an','dn']:
                print('invalid option choose from the histogram menu')
                histogram()
            if order.lower()=='aa':                        
                for i in dict_alph_asc.items():

                    print('{:3s}{:1s}{:1s}{:>4}{:1s}{:1s}{:1s}{:1s}{:100s}'.format(i[0].capitalize(),' ','(',i[1],')',' ',':',' ','*'*i[1]))


            if order.lower()=='da':
                az=ammino_unpacked
                az.sort(reverse=True)
                dict_alph_desc={aa:az.count(aa) for aa in az}
                for i in dict_alph_desc.items():

                    print('{:3s}{:1s}{:1s}{:>4}{:1s}{:1s}{:1s}{:1s}{:100s}'.format(i[0].capitalize(),' ','(',i[1],')',' ',':',' ','*'*i[1]))
            if order.lower()=='an':
                for i in sorted(dict_alph_asc.items(),key=lambda x:x[1]):
                    print('{:3s}{:1s}{:1s}{:>4}{:1s}{:1s}{:1s}{:1s}{:100s}'.format(i[0].capitalize(),' ','(',i[1],')',' ',':',' ','*'*i[1]))
            if order.lower()=='dn':
                for i in sorted(dict_alph_asc.items(),key=lambda x:x[1],reverse=True):
                    print('{:3s}{:1s}{:1s}{:>4}{:1s}{:1s}{:1s}{:1s}{:100s}'.format(i[0].capitalize(),' ','(',i[1],')',' ',':',' ','*'*i[1]))

        except NameError as name:
            print("No file loaded\n ")
