def ant(text):
    new=[]                 
    v=['a','e','i','o','u'] 
    for i in text:          
        if i not in v:  
            new.append(i)
        else:
            new.append(".")
                 
    return ''.join(new)

print (ant(input("請輸入一小串英文：")))