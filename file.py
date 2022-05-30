
from itertools import chain
import os,math,sys,re
from collections import Counter
#  Problem one

# x1=int(input("Enter x1 = "))
# y1=int(input("\nEnter y1 = "))
# x2=int(input("\nEnter x2 = "))
# y2=int(input("\nEnter y2 = "))
# distance=float(math.sqrt(pow((x2-x1),2)+pow((y2-y1),2)))
# print("Distance = ",distance)

###############

# Problem two
# def redund():
#     nums=[1,5,2,1,1,3,2]
#     reduce=set(nums)
#     res=list(reduce)
#     return res

# print(redund())



# Problem three

# def splitStr(str1,str2):
#     str1_lenth=len(str1)
#     n1=math.ceil(str1_lenth/2)
#     front_str1=str1[0:n1]
#     back_str1=str1[n1:]
    
#     str2_lenth=len(str2)
#     n2=math.ceil(str2_lenth/2)
#     front_str2=str2[0:n2]
#     back_str2=str2[n2:]


#     part1=front_str1+front_str2
#     part2=back_str1+back_str2

#     return part1+" "+part2
# str1=input("Enter first string: ")
# str2=input("Enter second string: ")

# print("Result = ",splitStr(str1,str2))


# problem four

# filename=sys.argv[1]
# f=open(filename)
# data=f.read()
# mystr=data.split() 
# f.close()
# words=Counter(mystr)
# mostCommon=words.most_common(20)
# f = open("popular_words.txt", 'w')
# for result in mostCommon:  
#  newData=result[0]+','
#  f.writelines(newData)
# f.close()

# Problem five
# def rem_vowel(str):
#     return (re.sub("[aeiouAEIOU]","",str))  

# str=input("Enter string : ")
# print("After remove vowels from string = ",rem_vowel(str))

# Problem six
def location(str,char):
   
    output=[]
    # How to use find()
    for pos,letter in enumerate(str):
        if(letter==char):
            output.append(pos)
        else:
            print ("Doesn't contains given character")
    return output
mystr=input("Enter string : ")
mychar=input("Enter Character : ") 


print("output : ",location(mystr,mychar))