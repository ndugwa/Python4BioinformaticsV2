# """
# Desplay function
# """



filename = ' None'


def display():
    """
    Desplay function

    """

    
    curr_filename = 'Current PDB: '+ filename

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

"""
validate pdb file
"""


def validpdb(file):
    """"
     takes a file and returns 2 if its a valid pdb file
     and any other number if not a pdb file
    """
    try:
        with open(file) as fh:
            # global pdbfile
            pdbfile=fh.readlines()
        count=0
        for line in pdbfile:
            if line.startswith('HEADER') and len(line) == 81:
                print(line)
                count+=1
            elif line.startswith('MASTER') and len(line)==81:
                print(line)
                count+=1
        return count
    except:
        print("File no found")


def pathr(opened):
    # opened=input("Enter a Valid PATH for a PDB File: ")
    valid=validpdb(opened)
    if valid==2:
        pathname=opened.split('/')[-1]
        # filename ='Current PDB: '+ pathname
        print(f'The File {pathname} has been successfully loaded')
        with open(opened) as fh:
            fp=fh.readlines()
            pathname=opened.split('/')[-1]
        
    else:
        print('file not a pdb ')
    return (fp)
#Exit function
def Exit(e):

    "exit the program if option q or 5 entered "
    # if e in "'q','5'":
    while e !=True:
        flag= False

        leave = input("Do you want to exit(E) or do you want go back to the menu (M): ").lower()
        if leave== 'm':
            flag=False
        elif leave == 'e':
            flag=True
                        
        elif leave != 'e' or leave != 'm':
            print("Ivalid option")
        return(flag) 
aa_dict = {'ARG':'R','HIS':'H','LYS':'K','ASP':'D','GLU':'E',
              'SER':'S','THR':'T','ASN':'N','GLN':'Q','CYS':'C',
              'SEC':'U','GLY':'G','PRO':'P','ALA':'A','VAL':'V',
              'ILE':'I','LEU':'L','MET':'M','PHE':'F','TYR':'Y',
              'TRP':'W'}
                

"information"
def information(file,filename):
    "displays summary infomation of the loaded pdb"
     
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
    
    for line in file:

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
    print(f'PDB File: {filename}' )
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

"histogram"
def hist_menu():
    print('Choose an option to order by:')
    print('{:2s}{:35s}{:>4s}'.format(' ','number of amino acids - ascending','(an)'))
    print('{:2s}{:34s}{:>4s}'.format(' ','number of amino acids - descending',' (dn)'))
    print('{:2s}{:35s}{:>4s}'.format(' ','alphabetically - ascending', '(aa)'))
    print('{:2s}{:35s}{:>4s}'.format(' ','alphabetically - descending','(da)'))
    global order
    order=input('Order by: ')
    return order



def histogram(p):
     
    
    ammino_list=[]
    for line in p:
        if line.startswith('SEQRES'): #extractint ammino acids
            ammino_list.append(line.split()[4:])

# unpacking a nested list of amino acids
    ammino_unpacked=[]
    for i in ammino_list:
        for j in i:
            ammino_unpacked.append(j)


    

    ammino_unpacked.sort()
    dict_alph_asc={aa:ammino_unpacked.count(aa) for aa in ammino_unpacked}
   
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

       
options= "'1','2','3','4','5','6','o','i','h','s','q'"
if __name__=='__main__':
    for opt in options:
        print (opt)
        opt=display().lower()
        if opt==None:
            print('No option Selected')
            break
                    
        else:   # opt=pdb.display().lower()
            if opt in "'q','5'":
                exit_status=Exit(opt)
                if exit_status==True:
                    break
            
            elif opt in "'1','o'":
                opened=input("Enter a Valid PATH for a PDB File: ")
                valid=validpdb(opened)
                # print(valid)
                # filename = pathr

                if valid==2:
                        pathname=opened.split('/')[-1]
                        if filename==pathname:
                            x=input("do you what to overwrite the current file? y/n: ")
                            if x=='y':
                                print(f'The File {pathname} has been successfully replaced')
                        else:
                            filename = pathname
                            print(f'The File {pathname} has been successfully loaded')
                            with open(opened) as fh:
                                f=fh.readlines()

                        # display().lower(),

                else:print("File not a PDB File ")
                
            elif opt in "'2','i'":
                try:
                    information(f,pathname)
                except NameError:
                    print('No Opened Pdb File')

            elif opt in "'3','h'":
                # hist_menu()
                try:
                    hist_menu()
                    histogram(f)
                except NameError:
                    print('No Opened Pdb File')

