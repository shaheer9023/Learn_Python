# Label the program written in problem 4 with comments.

import os # here we import built-in module os

directoryPath = "." # yahan hmny ek  variable me apni directory assign kr rahay or "." ka mtlb h current directory

content=os.listdir(directoryPath) ;''' yahan hum ek veriable content ko built-in function os.listdr() se assign kr rahay hai jo directoryPath ko as a argument le raha h or ye function directory me mojood files ko list krta h '''


for product in content: #yahan for loop given data ko loop me print karayga
    print(product)
