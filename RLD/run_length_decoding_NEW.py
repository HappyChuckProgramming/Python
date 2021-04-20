
def decode(m_str):
    ret_str = ""

    if m_str != "":
        for i in range(0, len(m_str), 2):
            num = int(m_str[i])
            ch = m_str[i+1]
            ret_str += ch*num

    return ret_str

def decode_new(m_str):
    ret_str = ""
    index = 0
    
    if m_str != "":
        while (index < len(m_str)):
            first = ""
            while (m_str[index] in '0123456789'):
                first += m_str[index]
                index += 1
            num = int(first)

            ch = m_str[index]
            index += 1

            ret_str += ch*num

        return ret_str

def decode_new_simpler(m_str):
    number= ""
    ret_str = ""

    for index in range(len(m_str)):
        try:
            int(m_str[index])
            check = True
        except ValueError:
            check = False

        if check:
            number += m_str[index]
        else:
            ret_str += int(number)*m_str[index]
            number=""

    return ret_str

    
#client code
x = '12A'
y = decode_new_simpler(x)
print(y)

x = '3A101B2C10D'
y = decode_new_simpler(x)
print(y)

