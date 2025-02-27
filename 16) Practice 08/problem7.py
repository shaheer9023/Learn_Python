# 7. Write a python function to remove a given word from a list ad strip it at the same time.
def stripping(list,wordToRemove):
 newList=[]
 for item in list:
   if(item!=wordToRemove):
    newList.append(item.strip(wordToRemove))
 return newList

list=["shaheer","ahmad","anas","zaid"]
print(stripping(list,"d"))    