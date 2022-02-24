# """
# Desplay function
# """



filename = ' None'


def display():
    """
    Desplay function

    """  
    curr_filename = 'Current PDB: '+ filename
    print()
    print('*' * 80)
    print('*', 'PDB FILE ANALYZER',' '*58,'*')
    print('*' * 80)
    print('*', 'select an option from below:',' '*48 +'*') 
    print('*', ' '*76, '*')
    print('{:7s} {:2s} {:30s} {:>4s} {:31s} {:s}'.format('*' , '1)','Open a pdb file','(O)',' ', '*' ))
    print('{:7s} {:2s} {:30s} {:>4s} {:31s} {:s}'.format('*' , '2)','Information' ,'(I)',' ', '*' ))
    print('{:7s} {:2s} {:30s} {:>4s} {:31s} {:s}'.format('*' , '3)','Show histogram of amino acids' ,'(H)',' ', '*' ))
    print('{:7s} {:2s} {:30s} {:>4s} {:31s} {:s}'.format('*' , '4)','Diplay secondary structure' ,'(S)',' ', '*' ))
    print('{:7s} {:2s} {:30s} {:>4s} {:31s} {:s}'.format('*' , '5)','Export PDB file' ,'(X)',' ', '*' ))
    print('{:7s} {:2s} {:30s} {:>4s} {:31s} {:s}'.format('*' , '6)','Exit' ,'(Q)',' ', '*' ))
    print('{:7s} {:>70s} {:s}'.format('*',curr_filename,'*' ))
    print('*' *80)
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
                # print(len(line))
                count+=1
            elif line.startswith('MASTER') and len(line)==81:
                # print(line)
                count+=1
        return count
    except:
        print("File no found")



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

def pdb_opened(path):
    """
    takes the path for pdb file
    """
    with open(path)as fh:
        file=fh.readlines()
    return file



def title(file):
    """
    extracts the title of a pdb file
    """
    title_info = 'Title: ' 
    for line in file:
        if line.startswith('TITLE'):
            title_line=line.split(maxsplit=1)[1]
            if title_line.split(maxsplit=1)[0].isdigit():
                title_info+=title_line.split(maxsplit=1)[1].strip()
            else:
                title_info+=title_line.strip()
    x='\n'.join([title_info[i:i+80] for i in range(0,len(title_info),80)])
            
    return x

def seqres(file):
    """
    takes the open pdb file and provides access to amino acids and chains in a pdb
    """
    global amino_dict_list 
    global ammino_list  
    global chains 
    global aa_num_dic  
    global amino_seq
    
    amino_dict_list = [] # a list of all amino acids with their respective chains
    amino_list = []     #all amino acids regardless of which chain they belong
    chain = []          #chains present in a pdb file
    aa_num = []         #number of amino acids
    for line in file:
        if line.startswith('SEQRES') and len(line.split()[4])==3: #some files contain nucleotides thus 'len(line.split()[4])==3' condition eliminates them

            amino_dict_list.append({line.split()[2]:line.split()[4:]})
            amino_list.append(line.split()[4:])
            chain.append(line.split()[2])
            # amino.append(f'{line.split()[2]}{line.split()[4:]}')
            a,b=line.split()[2],line.split()[3]
            aa_num.append((f'{a}:{b}'))

    chains=list(set(chain)) # remove duplicates and make a list
    chains.sort()
    
    aa_num_dic={}
    aa_n=list(set(aa_num)) ## remove duplicates and make a list
    for i in aa_n:
        aa_num_dic[i[0]]=i[2:]
    # create a dictionary of chains and respective amino acids       
    three_aa_dict={}
    for i in amino_dict_list:
        for a,b in i.items():
            if a in three_aa_dict.keys():
                three_aa_dict[a]+=b
            else:
                three_aa_dict[a]=b
    #transilate the three letter code to one letter code of amino acid and
    #create a dictionary of chains and respective amino acids
    amino_seq={k:''.join([aa_dict.get(i) for i in v]) for k,v in three_aa_dict.items()}
            
            
def helix(file):
    """
    takes the open pdb file and returns a dictionay of helix count in the chains
    """
    helix=[]
    for line in file:
        if line.startswith('HELIX'):
            helix.append(line.split()[7])
    
    helices={} # create a dictionary of helix count

    for j in chains:
        for i in helix:
            if i == j:
                helices[i]=helix.count(j)
            if j not in helix:
                helices[j]=0
    return helices
def sheets(file):
    """
    takes the open pdb file and returns a dictionary of sheets count in chains 
    """
    sheet_num=[]
    for line in file:
        if line.startswith('SHEET'):
            sheet_num.append(line.split()[5])
    sheets={}
    for j in chains:
        for i in sheet_num:
            if i == j:

                sheets[i]=sheet_num.count(j)
            if j not in sheet_num:
                sheets[j]=0
    return sheets

def print_info(filename,title,chains,helices,sheets,amino):
    print(f'PDB File: {filename}')
    
    print(title)
    if len(chains)==2:
        print('CHAINS:',chains[0],'and',chains[1])
    elif len(chains)==1:
        print('CHAIN:',', '.join(chains))

    else: print('CHAINS:',', '.join(chains))
    # amino_seq={k:''.join([aa_dict.get(i) for i in v]) for k,v in one_aa_dict.items()}

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

                print('{:3s}{:9s}{:50s}'.format(' ','Sequence:  ',amino.get(i)[j:50]))
                break
            for k in range(50,len(amino_seq.get(i)),50):
                print(('{:3s}{:9s}{:50s}'.format(' ',' '*11 ,amino.get(i)[k:k+50])))
        else:print('{:3s}{:9s}{:50s}'.format(' ','Sequence:  ',amino.get(i)))
    print()
    
def inf(y):
    # file=pdb_opened(y)
    # title(x)
    seqres(file)
    helix(file)
    sheets(file)
    print_info(filename,title(file),chains,helix(file),sheets(file),amino_seq)

# def information(file,filename):
#     "displays summary infomation of the loaded pdb"
     
#     title_info = ''
#     chain = []
#     aa_num =[]
#     helix=[]
#     sheet=[]
#     sheet_num=[]
#     amino=[]
#     amino_dict={}
#     ammino_list=[]
#     another={}
#     amino_dict_list=[]
    
#     for line in file:

#         if line.startswith('TITLE'):

#             p=line.split()

#             x=' '.join(p[1:])#extracting TITLE informations 
#             title_info += x
#         if line.startswith('SEQRES') and len(line.split()[4])==3: #information about the chains
#             # if len(0
#             amino_dict_list.append({line.split()[2]:line.split()[4:]})
#             ammino_list.append(line.split()[4:])
#             chain.append(line.split()[2])
#             amino.append(f'{line.split()[2]}{line.split()[4:]}')
#             a,b=line.split()[2],line.split()[3]
#             aa_num.append((f'{a}:{b}'))


#         # extracting helix
#         if line.startswith('HELIX'):
#             helix.append(line.split()[7])

#         # extracting sheets
#         if line.startswith('SHEET'):
#             sheet_num.append(line.split()[5])
#         # tittle and chains in the pdb file
#     print(f'PDB File: {filename}' )
#     print('TITTLE:', title_info)
#     chains=list(set(chain))
#     chains.sort()
#     if len(chains)==2:
#         print('CHAINS:',chains[0],'and',chains[1])
#     elif len(chains)==1:
#         print('CHAIN:',', '.join(chains))

#     else: print('CHAINS:',', '.join(chains))


# #         CREATING DICTIONARIES OF HELIX COUNT AND SHEET COUNT
#     helices={}

#     for j in chains:
#         for i in helix:
#             if i == j:

#                 helices[i]=helix.count(j)
#             if j not in helix:
#                 helices[j]=0

#     # sheets={chain_name:sheet_n.count(chain_name) for chain_name in sheet_n}
#     sheets={}
#     for j in chains:
#         for i in sheet_num:
#             if i == j:

#                 sheets[i]=sheet_num.count(j)
#             if j not in sheet_num:
#                 sheets[j]=0

#     aa_num_dic={}
#     aa_n=set(aa_num)
#     aa_n=list(aa_n)
#     for i in aa_n:
#         aa_num_dic[i[0]]=i[2:]
    
#     # helixes={chain_nam:helix.count(chain_nam) for chain_nam in helix}



#     one_aa_dict={}
#     for i in amino_dict_list:
#         for a,b in i.items():
#             if a in one_aa_dict.keys():
#                 one_aa_dict[a]+=b
#             else:
#                 one_aa_dict[a]=b
#     # print(one_dict)
#     amino_seq={k:''.join([aa_dict.get(i) for i in v]) for k,v in one_aa_dict.items()}

#     for i in chains:

#         print('{:2s}{:6s}{:10s}'.format('-','Chain',i))
#         print('{:3s}{:22s}{:>4}'.format(' ','Number of amino acids:',aa_num_dic.get(i)))
#         print('{:3s}{:22s}{:>4}'.format(' ','Number of helix:',helices.get(i)))
#         if len(sheets)==0:
#             pass
#         else:print('{:3s}{:22s}{:>4}'.format(' ','Number of sheet:',sheets.get(i)))
#         # print('{:3s}{:9s}{:50s}'.format(' ','Sequence:  ',one_aa_dic.get(i)))
#         if len(amino_seq.get(i))>50:
#             for j in range(0,len(amino_seq.get(i)),50):

#                 print('{:3s}{:9s}{:50s}'.format(' ','Sequence:  ',amino_seq.get(i)[j:50]))
#                 break
#             for k in range(50,len(amino_seq.get(i)),50):
#                 print(('{:3s}{:9s}{:50s}'.format(' ',' '*11 ,amino_seq.get(i)[k:k+50])))
#         else:print('{:3s}{:9s}{:50s}'.format(' ','Sequence:  ',amino_seq.get(i)))
#     print()
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
        hist_menu()
        print()
        
    if order.lower()=='aa':
        print()
        for i in dict_alph_asc.items():

            print('{:3s}{:1s}{:1s}{:>4}{:1s}{:1s}{:1s}{:1s}{:100s}'.format(i[0].capitalize(),' ','(',i[1],')',' ',':',' ','*'*i[1]))
        # print()

    if order.lower()=='da':
        print()
        az=ammino_unpacked
        az.sort(reverse=True)
        dict_alph_desc={aa:az.count(aa) for aa in az}
        for i in dict_alph_desc.items():

            print('{:3s}{:1s}{:1s}{:>4}{:1s}{:1s}{:1s}{:1s}{:100s}'.format(i[0].capitalize(),' ','(',i[1],')',' ',':',' ','*'*i[1]))
        # print()
    if order.lower()=='an':
        print()
        for i in sorted(dict_alph_asc.items(),key=lambda x:x[1]):
            print('{:3s}{:1s}{:1s}{:>4}{:1s}{:1s}{:1s}{:1s}{:100s}'.format(i[0].capitalize(),' ','(',i[1],')',' ',':',' ','*'*i[1]))
        # print()
    if order.lower()=='dn':
        print()
        for i in sorted(dict_alph_asc.items(),key=lambda x:x[1],reverse=True):
            print('{:3s}{:1s}{:1s}{:>4}{:1s}{:1s}{:1s}{:1s}{:100s}'.format(i[0].capitalize(),' ','(',i[1],')',' ',':',' ','*'*i[1]))
        # print()


def secondary_structure(file,filename):
    """
    takes an open pdb file and extract secondary structures
    that's helices and sheets
    they are desplayed as aligned to the amino acid sequence
    '|' represents the sheet position and '/' represents the helix position
    
    """
#     chains and amino acid extraction
    ammino_list=[]
    chain=[]
    # amino_ac=[]
    aa_num=[]
    amino_dict_list=[]
#     for hilices extraction
    start_str_helix=[]
    stru_name_helix=[]
    start_pos_helix=[]
    end_pos_helix=[]
    start_helix=[]
    stop_helix=[]
#     for sheet extraction
    start_sheet=[]
    stop_sheet=[]
    sheet_name=[]
    start_str_sheet=[]
    #     chains and amino acid extraction
    for line in file:
        if line.startswith('SEQRES') and len(line.split()[4])==3: 
            amino_dict_list.append({line.split()[2]:line.split()[4:]})
            ammino_list.append(line.split()[4:])
            chain.append(line.split()[2])
            a,b=line.split()[2],line.split()[3]
            aa_num.append((f'{a}:{b}'))#information about the chains
            # amino_ac.append({line.split()[2]:line.split()[4:]})
      
    #     for hilices extraction

        elif line.startswith('HELIX'):
                start_pos_helix.append({line.split()[4]:[int(line.split()[5])-1]})
                end_pos_helix.append({line.split()[4]:[int(line.split()[8])-1]})
                start_helix.append({line.split()[4]:int(line.split()[5])-1})
                stop_helix.append({line.split()[4]:int(line.split()[8])-1})
                if len(line.split()[1])==1:
                    start_str_helix.append({line.split()[4]:[int(line.split()[5])-1]})
                else:
                    start_str_helix.append({line.split()[4]:[int(line.split()[5])-1,int(line.split()[5])]})
                if len(line.split()[1])==1:
                    stru_name_helix.append({line.split()[4]:[f'{line.split()[1]}',int(line.split()[5])-1]})
                if len(line.split()[1])==2:
                    stru_name_helix.append({line.split()[4]:[f'{list(line.split()[1])[0]}',f'{list(line.split()[1])[1]}',int(line.split()[5])-1,int(line.split()[5])]})
                if len(line.split()[1])==3: 
                    stru_name_helix.append({line.split()[4]:[f'{list(line.split()[1])[0]}',f'{list(line.split()[1])[1]}',f'{list(line.split()[1])[2]}',int(line.split()[5])-1,int(line.split()[5]),int(line.split()[5])]})
#     for sheet extraction

        elif line.startswith('SHEET'):            
                start_str_sheet.append({line.split()[5]:[int(line.split()[6])-1, int(line.split()[6])]})          
                start_sheet.append({line.split()[5]:int(line.split()[6])-1})
                stop_sheet.append({line.split()[5]:int(line.split()[9])-1})
                if len(line.split()[1])==1 and len(line.split()[2])==1:
                    sheet_name.append({line.split()[5]:[f'{line.split()[1]}',f'{line.split()[2]}',int(line.split()[6])-1,int(line.split()[6])]})
                elif len(line.split()[1])==2 and len(line.split()[2])==1:
                    sheet_name.append({line.split()[5]:[f'{list(line.split()[1])[0]}',f'{list(line.split()[1])[1]}',f'{line.split()[2]}',int(line.split()[6])-1,int(line.split()[6]),int(line.split()[6])+1]})
                elif len(line.split()[1])==3 and len(line.split()[2])==1:
                    sheet_name.append({line.split()[5]:[f'{list(line.split()[1])[0]}',f'{list(line.split()[1])[1]}',f'{list(line.split()[1])[2]}',f'{line.split()[2]}',int(line.split()[6])-1,int(line.split()[6]),int(line.split()[6])+1,int(line.split()[6])+2]})
                elif len(line.split()[1])==1 and len(line.split()[2])==2:
                    sheet_name.append({line.split()[5]:[f'{line.split()[1]}',f'{list(line.split()[2])[0]}',f'{list(line.split()[2])[1]}',int(line.split()[6])-1,int(line.split()[6]),int(line.split()[6])+1]})
                elif len(line.split()[1])==1 and len(line.split()[2])==3:
                    sheet_name.append({line.split()[5]:[f'{line.split()[1]}',f'{list(line.split()[2])[0]}',f'{list(line.split()[2])[1]}',f'{list(line.split()[2])[2]}',int(line.split()[6])-1,int(line.split()[6]),int(line.split()[6])+1,int(line.split()[6])+2]})
                elif len(line.split()[1])==2 and len(line.split()[2])==2:
                    sheet_name.append({line.split()[5]:[f'{list(line.split()[1])[0]}',f'{list(line.split()[1])[1]}',f'{list(line.split()[2])[0]}',f'{list(line.split()[2])[1]}',int(line.split()[6])-1,int(line.split()[6]),int(line.split()[6])+1,int(line.split()[6])+2]})
                elif len(line.split()[1])==3 and len(line.split()[2])==3: 
                    sheet_name.append({line.split()[5]:[f'{list(line.split()[1])[0]}',f'{list(line.split()[1])[1]}',f'{list(line.split()[1])[2]}',f'{list(line.split()[2])[0]}',f'{list(line.split()[2])[1]}',f'{list(line.split()[2])[2]}',int(line.split()[6])-1,int(line.split()[6]),int(line.split()[6])+1,int(line.split()[6])+2,int(line.split()[6])+3,int(line.split()[6])+4]})     
    aa_num_dic={}
    aa_n=set(aa_num)
    aa_n=list(aa_n)
    for i in aa_n:
        aa_num_dic[i[0]]=i[2:]                                                

    chains=list(set(chain)) # remove duplicates and make a list
    chains.sort()

     # create a dictionary of chains and respective amino acids       
    three_aa_dict={}
    for i in amino_dict_list:
        for a,b in i.items():
            if a in three_aa_dict.keys():
                three_aa_dict[a]+=b
            else:
                three_aa_dict[a]=b
    #transilate the three letter code to one letter code of amino acid and
    amino_seq={k:''.join([aa_dict.get(i) for i in v]) for k,v in three_aa_dict.items()}

    #create a dictionary of chains and respective amino acids
    sheet_name_dict={}
    for i in sheet_name:
        for k,v in i.items():
            if k in sheet_name_dict.keys():
                sheet_name_dict[k]+=[v]
            else:sheet_name_dict[k]=[v]
    # print(sheet_name_dict)
    helix_name_dict={}
    for i in stru_name_helix:
        for k,v in i.items():
            if k in helix_name_dict.keys():
                helix_name_dict[k]+=[v]
            else:helix_name_dict[k]=[v]
    # create all postions of the helix
    start_helix_dic={}
    for i in start_helix:
        for k,v in i.items():
            if k in start_helix_dic.keys():
                start_helix_dic[k]+=v
            else:start_helix_dic[k]=v
    # print(start_helix_dic)
    stop_helix_dict={}
    for i in stop_helix:
        for k,v in i.items():
            if k in stop_helix_dict.keys():
                stop_helix_dict[k]+=v
            else:stop_helix_dict[k]=v
    # print(stop_helix_dict)
    #finding all positions of sheets
    start_sheet_dict={}
    for i in start_sheet:
        for k,v in i.items():
            if k in start_sheet_dict.keys():
                start_sheet_dict[k]+=[v]
            else:
                start_sheet_dict[k]=[v]
    start_helix_dict={}
    for i in start_helix:
        for k,v in i.items():
            if k in start_helix_dict.keys():
                start_helix_dict[k]+=[v]
            else:
                start_helix_dict[k]=[v]
    stop_sheet_dict={}
    for i in stop_sheet:
        for k,v in i.items():
            if k in stop_sheet_dict.keys():
                stop_sheet_dict[k]+=[v]
            else:
                stop_sheet_dict[k]=[v]
    stop_helix_dict={}
    for i in stop_helix:
        for k,v in i.items():
            if k in stop_helix_dict.keys():
                stop_helix_dict[k]+=[v]
            else:
                stop_helix_dict[k]=[v]

    all_sheet=[]
    for k in start_sheet_dict.keys():
        s=start_sheet_dict.get(k)
        t=stop_sheet_dict.get(k)
        for i in range(0,len(s)):
            a=t[i]-s[i]
            b=s[i]
            for j in range(b,(a+1+b)):
                all_sheet.append({k:j})


    all_helix=[]
    for k in start_helix_dict.keys():
        s=start_helix_dict.get(k)
        t=stop_helix_dict.get(k)
        for i in range(0,len(s)):
            a=t[i]-s[i]
            b=s[i]

            for j in range(b,(a+1+b)):
                all_helix.append({k:j})

    all_sheet_dict={}
    for i in all_sheet:
        for k,v in i.items():
            if k in all_sheet_dict.keys():
                all_sheet_dict[k]+=[v]
            else:all_sheet_dict[k]=[v]


    all_helix_dict={}
    for i in all_helix:
        for k,v in i.items():
            if k in all_helix_dict.keys():
                all_helix_dict[k]+=[v]
            else:all_helix_dict[k]=[v]

    # update all the sheet position and helix to include all chains



    start_sheet_dict={}
    for i in start_str_sheet:
        for k,v in i.items():
            for l in v:
                if k in start_sheet_dict.keys():
                    start_sheet_dict[k]+=[l]
                else:
                    start_sheet_dict[k]=[l]


    start_helix_dict={}
    for i in start_str_helix:
        for k,v in i.items():
            for l in v:
                if k in start_helix_dict.keys():
                    start_helix_dict[k]+=[l]
                else:
                    start_helix_dict[k]=[l]

    # updating the dictionaries
    for i in chains:
        if start_sheet_dict.get(i):
            pass
        else:start_sheet_dict[i]=[100000]
        if start_helix_dict.get(i):
            pass
        else:start_helix_dict[i]=[100000]
        if all_sheet_dict.get(i):
            pass
        else:all_sheet_dict[i]=[100000]
        if all_helix_dict.get(i):
            pass
        else:all_helix_dict[i]=[100000]

     #Obtaining the secondary structure     
    structure=''
    helix_pos=0
    secondary_seq=''
    print(f"Secondary Structure of the PDB id {filename.split('.')[0]}:")
    for i in chains:
        print(f'Chain {i}:')
        print('(1)')

        for j in range(len(amino_seq.get(i)),):
            if j in all_helix_dict.get(i):#replace the aminao acid in helix structure with '/'
                secondary_seq+='/'
            elif j in all_sheet_dict.get(i):#replace the amino acid in the sheet structure with "|"
                secondary_seq+='|'
            elif j not in all_helix_dict.get(i) and j not in all_sheet_dict.get(i): #replace the other amino acids with '-'
                secondary_seq+='-'
            if j in start_helix_dict.get(i):#structures
                for h in helix_name_dict.get(i):   
                    if len(h[:])==6 :
                        if j==h[3]:
                            structure+=h[0]
                            if j+1==h[4]:
                                structure+=h[1]
                            if j+2==h[5]:
                                structure+=h[2]
                    elif len(h[:])==4 :
                        if j==h[2]:
                            structure+=h[0]
                            if j+1==h[3]:
                                structure+=h[1]
                    elif len(h[:])==2:
                         if j==h[1]:
                                structure+=h[0]

            elif j in start_sheet_dict.get(i):
                for t in sheet_name_dict.get(i):
                    if len(t[:])==12 :
                        if j==t[6]:
                            structure+=t[0]
                        if j+1==t[7]:
                            structure+=t[1]
                        if j+2==t[8]:
                            structure+=t[2]
                        if j+3==t[9]:
                            structure+=t[3]
                        if j+4==t[10]:
                            structure+=t[4]
                        if j+5==t[11]:
                            structure+=t[5]
                    elif len(t[:])==10 :
                        if j==t[5]:
                            structure+=t[0]
                            if j+1==t[6]:
                                structure+=t[1]
                            if j+2==t[7]:
                                structure+=t[2]
                            if j+3==t[8]:
                                structure+=t[3]
                            if j+4==t[9]:
                                structure+=t[4]
                    elif len(t[:])==8 :
                        if j==t[4]:
                            structure+=t[0]
                        if j+1==t[5]:
                            structure+=t[1]
                        if j+2==t[6]:
                            structure+=t[2]
                        if j+3==t[7]:
                            structure+=t[3]
                    elif len(t[:])==6 :
                        if j==t[3]:
                            structure+=t[0]
                        if j+1==t[4]:
                            structure+=t[1]
                        if j+2==t[5]:
                            structure+=t[2]
                    if len(t[:])==4 :
                        if j==t[2]:
                            structure+=t[0]
                        if j+1==t[3]:
                            structure+=t[1]
            else:structure+='*'
        #showing the strutuctues 
        for k in range(0,len(secondary_seq),80):
            print(amino_seq.get(i)[k:k+80])
            print(secondary_seq[k:k+80])
            print(structure[k:k+80].replace('*', ' '))
            print(f'({aa_num_dic.get(i)})')
        print()
        structure=''
        helix_pos=0
        secondary_seq=''

def export_pdb(file):
    """
    exports the pdb file
    """
    if file:
        print("Sorry! Underdevelopment")




 ## THE MAIN PROGRAM
options= "'1','2','3','4','5','6','o','i','h','s','q','x'"
if __name__=='__main__':
    for opt in options:
      
        opt=display().lower()
       
        if opt in "'q','6'":
            exit_status=Exit(opt)
            if exit_status==True:
                break

        elif opt in "'1','o'":
            opened=input("Enter a Valid PATH for a PDB File: ")
            valid=validpdb(opened)
            loaded="None"

            if valid==2:
                    pathname=opened.split('/')[-1]
                    
                    if filename==pathname:
                        x=input("do you what to overwrite the current file? y/n: ")
                        if x=='y':
                            print(f'The File {pathname} has been successfully replaced')
                    else:
                        filename = pathname
                        loaded=pathname
                        print(f'The File {pathname} has been successfully loaded')
                        with open(opened) as fh:
                            file=fh.readlines()

                    # display().lower(),

            else:print("File not a PDB File ")

        elif opt in "'2','i'":
            try:
                inf(file)
                        # file=pdb_opened(y)
                        # # title(x)
                        # seqres(file)
                        # helix(file)
                        # sheets(file)
                        # print_info(filename,title(x),chains,helix(file),sheets(file),amino_seq)

                # information(file,pathname)
            except NameError:
                print('No Opened Pdb File')

        elif opt in "'3','h'":
            # hist_menu()
            try:
                hist_menu()
                histogram(file)
            except NameError:
                print('No Opened Pdb File')

        elif opt in "'4','s'":
            try:
                secondary_structure(file,pathname)
            except NameError:
                print('No Opened Pdb File')
                
        elif opt in "'5','x'":
            try:
                export_pdb(file)
            except NameError:
                print('No Opened Pdb File') 
         