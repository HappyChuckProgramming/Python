def encode(mstr):
    wordsize = 0
    encoded_msg = ''
    for i in range(len(mstr)):
        ch = mstr[i]
        wordsize = wordsize + 1

        if i == len(mstr)-1:   # ch is last char in mstr
            encoded_msg = encoded_msg + str(wordsize) + ch
            break
        else:
            if ch == mstr[i+1]: # look ahead and check if next up char is same
                pass
            else:              # next up char starts next word
                encoded_msg = encoded_msg + str(wordsize) + ch
                wordsize = 0
     
    return encoded_msg

#client code
x = 'AAAA'
y = encode(x)
print(y)


x = 'AAABBBBCCD'
y = encode(x)
print(y)

x = 'D'
y = encode(x)
print(y)

x = ''
y = encode(x)
print(y)

x = 'EF'
y = encode(x)
print(y)

