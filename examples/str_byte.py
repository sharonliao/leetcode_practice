# write byte
with open('data/data_b.bin','wb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')

# write str
with open('data/data_str.bin','w') as f:
    f.write('this is a str')

# read byte rto byte
with open ('data/data_b.bin','rb') as f :
    data = f.read()
    print(data)

# read byte to str
with open('data/data_str.bin','r',encoding = 'cp1252') as f:
    data = f.read()
    print(data)


def to_str(bytes_or_str):
    if isinstance(bytes_or_str,bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_str(b'foo')))
print(repr(to_str('foo')))


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str,str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


    
