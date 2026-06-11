# def palindrome(text):
#     return text==text[::-1]



# i=input("enter the text:") 
# print(palindrome(i))   

# s=input("enter 1st the string:")
# s1=input("enter 2nd string:")
# c=s+s1
# v=""
# for i in c:
#     if i not in v:
#         v=v+i
# print("output:",v)

# s=input("enter the string:")
# r=int(input("enter no of rotations:"))
# a=r%len(s)
# final=s[a:]+s[:a]
# print("".join(final))


# s=list(input("enter the string").split())
# for i in s:
#     s=0

#     for j in i:

#         integer =int(j)
#         s+=integer
#     print(s,end=" ")


# s=input("enter the string:")
# for i in s:
#     if (s.count(i)==1):
#         print(i)
#         break

# s=input('enter the string:')
# a=len(s)
# for i in range(a):

#     print(s[:i+1])

# s=input("enter the string:")
# vowels='aeoiu'
# if (len(s)==3):

#     if (s[1]  in vowels) and (s[0] not in vowels) and (s[2] not in vowels):
#         print("Yes")
#     else:
#         print("NO")

# else:
#     print("not a 3 letter string")

s=list(input("enter the string:").split())

print(min(s,key=len))