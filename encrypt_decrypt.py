plain_text="Love will find a way."

encrypted_text=""
for c in plain_text:
    x=ord(c)
    x=x+1
    cc=chr(x)
    encrypted_text=encrypted_text+cc
print(encrypted_text)

plain_text=""
for c in encrypted_text:
    x=ord(c)
    x=x-1
    cc=chr(x)
    plain_text=plain_text+cc
print(plain_text)
