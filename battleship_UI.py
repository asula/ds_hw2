# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:13:56 2016

@author: Marit
"""


from string import ascii_lowercase

arr = ['|   ']*5
battlefield = '    1   2   3   4   5  ' + '\n' + \
              'A |   |   |   |   |   |' + '\n' + \
              'B |   |   |   |   |   |' + '\n' + \
              'C |   |   |   |   |   |' + '\n' + \
              'D |   |   |   |   |   |' + '\n' + \
              'E |   |   |   |   |   |' + '\n' + \
              'F |   |   |   |   |   |' 
              
#print battlefield

field = [arr]*5

#for arr in field:
#    print ''.join(arr) + '|'

field[0][2] = '| X '

#print ''.join(field[0]) + '|'


#print l
dim = 10
player_field = [[0]*dim for i in range(dim)]


def generate_battlefield(player_field):
    
    header_row = ['   '] + [' ' + str(nr+1) + '  ' for nr in range(dim)]
    alphabet = list(ascii_lowercase)
    print ''.join(header_row)


    for i in range(len(player_field)):
        row = player_field[i]
        arr = [alphabet[i].upper()+' ']
        for col in row:
            if col == 0:
                arr.append('|   ')
            else:
                arr.append('| O ')
        print ''.join(arr) + '|'

        
    
def are_concecutive(array):
    array = sorted(array)
    alphabet = list(ascii_lowercase)

    if type(array[0]) == str:
        for i in range(len(array)-1):
            if alphabet.index(array[i])+1 != alphabet.index(array[i+1]):
                return False
        
    else:
        for i in range(len(array)-1):
            if array[i]+1 != array[i]+1:
                return False
    return True
        
      
    
def are_equal(array):

    for i in range(len(array)-1):
        if array[i]!=array[i+1]:
            return False
    return True

# Error handling:

line = 'B2,B3,B4,B5'
def is_allowed_pos(pos_list):

    first_list = [pos[0].lower() for pos in pos_list]
    sec_list = [int(pos[1]) for pos in pos_list]

    if are_equal(first_list) and are_concecutive(sec_list) or \
       are_concecutive(first_list) and are_equal(sec_list):
        return True
    else:
        return False
    

def parse_user_input(line):
    alphabet = list(ascii_lowercase)
    pos_list = line.split(',')

    for pos in pos_list:
        x = int(alphabet.index(pos[0].lower()))
        y = int(pos[1:])-1

        player_field[x][y] = 1

def is_allowed_length(pos_list,length):
    if len(pos_list) != length:
        return False
    else:
        return True

for i in range(4):   
    generate_battlefield(player_field)
    print ('\n')
    
    inp = raw_input('Please insert size ' + str(i+1) + ' ship position: \n')

    pos_list = inp.split(',')
    while not is_allowed_pos(pos_list) or not is_allowed_length(pos_list,i+1):
        if not is_allowed_length(pos_list,i+1):
            print 'Inserted ship size is wrong.'
        else:
            print 'Ship must be placed in concecutive positions!\n'
        inp = raw_input('Please insert size ' + str(i+1) + ' ship position: \n')
        pos_list = inp.split(',')
    print ('\n')
    parse_user_input(inp)
    
generate_battlefield(player_field)



           
