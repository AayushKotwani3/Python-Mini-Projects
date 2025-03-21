
# enCoding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning



import random as r  # importing random module and aliasing it to r
import string       #importing string module

# encoding function takes a string and encode it according to instructions
def encode(s):
    f_str=' '
    nstr=[]
    words=s.split(" ") # create a list of all the words and store it in a list
    for word in words:   
        if len(word)>=3:   #checks the length of string if its greater than 3

            new_str=word[1:]+word[0]    #new_str variable creates a new string using slicing this string starts from the second letter till end and appends the first letter  at the end 

            #using random module to generate random 3 character string to append at the beginning 
            pre=''.join(r.choices(string.ascii_letters,k=3)) #this line will generate a list with 3 random characters and store it in pre variable
            
            #using random module to generate random 3 character string to append at the end
            post=''.join(r.choices(string.ascii_letters,k=3))

            new_str=pre+new_str+post #this line finalize the encoded string and append it in nstr
            nstr.append(new_str) 

        else:     #if the length of string is smaller than 3 it comes in this else block
            nstr.append(word[::-1]) #this line reverses the string and append it to nstr list
    return f_str.join(nstr)    #returns the encoded string

# decoding function takes a string and decode it according to instructions
def decode(s):
    f_str=' '
    nstr=[]
    words=s.split(" ")      # create a list of all the words and store it in a list   
    for word in words:   
        if len(word)>=3:    #checks the length of string if its greater than 3
            new_str=word[3:-3]     #new_str variable stores a new string using slicing it removes 3 characters from beginning and end of the given string
            last_char=new_str[-1]     #last_char variable stores the last character from the new_str
            new_str=last_char+new_str[:-1]   #now the decoded string is finalized in new_str variable first it takes the last_char and append new_str till -1 index
            nstr.append(new_str)
        else:    #if the length of string is smaller than 3 it comes in this else block
            nstr.append(word[::-1])    #this line reverses the string and append it in  nstr list   
    return f_str.join(nstr)   #returns the decoded string

