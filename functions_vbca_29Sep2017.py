'''
By: Victor 
Date: September 29th 2017

    0- Hello world (2+2)
    1- Write a fibonacci function
    2- Write a function reverse to reverse a list. Can you do this without using list slicing?
    3- Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?
    4- Write a function cumulative_product to compute cumulative product of a list of numbers.
    5- Write a function unique to find all the unique elements of a list. (int & strings)
    6- Write a function dups to find all duplicates in the list. (int & strings)
    7- Write a function group(list, size) that take a list and splits into smaller lists of given size.

'''


def plus2(*number):
    if len(number)<2:
        raise ValueError('Need at least 2 numbers')
    if len(number)>2:
        raise ValueError('No more of 2 numbers')      
    if not (isinstance(number[0], (int,float)) and isinstance(number[1], (int,float))):
        raise TypeError('Please insert only numbers') 
    try: 
        result = number[0]+number[1]
    except TypeError as e:    
        raise TypeError('Please insert 2 numbers')     
    return result    

def fibonacci(*number):
    if len(number)<1:
        raise ValueError('Method waiting 1 number')
    if len(number)>1:
        raise ValueError('No more of 2 values')    
    if not (isinstance(number[0], int)):
         raise TypeError('Only a number value') 
    if  number[0] < 1 :
         raise TypeError('Please write a correct position')     
    if number[0] == 1:                         #case 0
        return [0]
    elif number[0] == 2:                       #case 1
        return [0, 1]
    else:
        lst = fibonacci(number[0]-1)                 #case 3 or more
        lst.append(lst[-1] + lst[-2])  #we add list a lass value
        return lst

def reverse_list(*original_list):
    if len(original_list)<1:
        raise ValueError('Method need a list for process')
    if len(original_list)>1:
        raise ValueError('Method only need one list') 
    if not (isinstance(original_list[0], list)):
         raise TypeError('This element is not a list') 
    size= len(original_list[0])   
    return_list = [];                            #final list
    return_list= [original_list[0][size-i-1] for i,v in enumerate(original_list[0])]     
    return return_list                           #return


def cumulative_plus(*original_list):
    if len(original_list)<1:
        raise ValueError('Method need a list for process')
    if len(original_list)>1:
        raise ValueError('Method only need one list') 
    if not (isinstance(original_list[0], list)):
         raise TypeError('This element is not a list') 
    final_list=[];                              #final list
    totalnumber=0
    totalstring=''
    flagstring=False
    position=0
    for item in original_list[0]: 
       if (isinstance(original_list[0][position], int) and flagstring==False):
           totalnumber=totalnumber+original_list[0][position]
           final_list.append(totalnumber)
       elif (isinstance(original_list[0][position], (str,int))) :
           final_list.append(str(totalnumber)+str(original_list[0][position]))
           totalnumber=str(totalnumber)+str(original_list[0][position])
           flagstring=True
       else:
           raise TypeError('Invalid value type, only string and int')     
       position+=1
    return final_list



def cumulative_product(*original_list):
    if len(original_list)<1:
        raise ValueError('Method need a list for process')
    if len(original_list)>1:
        raise ValueError('Method only need one list') 
    if not (isinstance(original_list[0], list)):
         raise TypeError('This element is not a list') 
    lst=[];                              #final list
    total=1;                             #total
    for item in original_list[0]:                  #loop
        if not (isinstance(item, (int,float))):
            raise TypeError('Only a number value') 
        total = total * item;            #box
        lst.append(total);               #add box
    return lst     


def unique_element_list(*original_list):
    if len(original_list)<1:
        raise ValueError('Method need a list for process')
    if len(original_list)>1:
        raise ValueError('Method only need one list') 
    if not (isinstance(original_list[0], list)):
         raise TypeError('This element is not a list') 
    final_list=[x for x in original_list[0] if (original_list[0]).count(x) == 1]
    #         loop elements origin        condition    item into element =1
    return final_list


def double_element_list(*original_list):
    if len(original_list)<1:
        raise ValueError('Method need a list for process')
    if len(original_list)>1:
        raise ValueError('Method only need one list') 
    if not (isinstance(original_list[0], list)):
         raise TypeError('This element is not a list') 
    final_list=[x for x in original_list[0] if (original_list[0]).count(x) > 1]
    #         loop elements origin        condition    item into element =1
    return list(set(final_list))


#consecutive-strings
#1 - https://www.codewars.com/kata/consecutive-strings

def longest_consec(strarr, k):
    n= int(len(strarr))
    if(n==0 or k>n or k<=0):          #Initial contidion, we safe that 1) we have a array for comparate 2)position are more than array   3)k will count a positions          
        return "Please check the argumentes"
    message=''                        #variables for count position and comparate
    position=-1
    comparate=0
    contador=0
    for item in set(strarr):          #loop for get the position
        if(comparate<len(strarr[contador])):
             comparate=len(strarr[contador])
             position=contador
        contador=contador+1
    contador=0  
    if((position+1)+k>n and k>=2):    #watching the final results, we try to code the behavior of the operations, I see a move not controlable after position and move make a overflow in array,
        if(len(strarr)==position+1):
            contador=contador-position
            position=(n+position-k)
        elif(len(strarr[position])>len(strarr[position+1])):
            position=(n+position-k)-1
            contador=contador-1    
    for i in range(k):                #Print the message, I got successfull on all test but "random test" failed code
        message=message+strarr[position+contador]
        contador=contador+1
    return message

#nesting-structure-comparison
#3- https://www.codewars.com/kata/nesting-structure-comparison
def same_structure_as(original,other):                #we take the arrays   
    comparate1 = list_to_text(original, "")           #we recover only the list structure
    comparate2 = list_to_text(other, "")              #we recover only the list structure
    print(comparate1)
    return comparate1 == comparate2                   #comparate
    
def list_to_text(lista, answer):                      #recurse method, we call for check node for search again node and come back with only [] the initial list
    if (isinstance(lista, list)):                     #check elements for be list
        answer += '['
        for node in lista:                           
            if (isinstance(node, list)):              #check the nodes be list
                answer += list_to_text(node, answer)
                #answer += list_to_text(node, "["+answer+"]")
            else:
                answer+= answer+"0]"                  #close search, of non list element
        answer += ']'        
    return answer