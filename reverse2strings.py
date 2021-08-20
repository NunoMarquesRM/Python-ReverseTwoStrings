#python 3.6.9

def invertedArray(str):
    tmp = []
    index = len(str)
    while( index > 0 ):
        tmp += str[ index - 1]
        index -= 1
    return tmp

def InvertedMerge(str1, str2):
    tmpStr1 = invertedArray(str1)
    tmpStr2 = invertedArray(str2)
    maximo = 0

    if(len(tmpStr1) > len(tmpStr2)):
        maximo = len(tmpStr1)
    else:
        maximo = len(tmpStr2)
    
    i = 0
    final = ""
    while( i < maximo ):
        if(i < len(tmpStr1)):
            final += tmpStr1[i]
        if(i < len(tmpStr2)):
            final += tmpStr2[i]
        i+=1
    return final
