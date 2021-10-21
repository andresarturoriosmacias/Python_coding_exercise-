def int_to_roman(x):
    valid_number = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
    i=0
    result = 0
    char_list = []
    for char in x:
        char_list.append(char)
    print(char_list)
    while i in range(len(x)):
        print('Counter: ',str(i),' Len: ',str(len(x))) 
        if i+1<len(x) and valid_number[x[i]] < valid_number[x[i+1]]:
            special_number = str(x[i] + x[i+1])
            if special_number in valid_number:
                print('Value added to result',str(valid_number[special_number]))
                result += valid_number[special_number]
                i+=2
                print('Counter i value:',str(i))
            else:
                print('Invalid number', x)
                break
        else:
            print('Value added to result',str(valid_number[x[i]]))
            result += valid_number[x[i]]
            i+=1
    return result
        
print(int_to_roman('CMII'))
