#encrypting


letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y' ,'z']

plain_text = input('Plese enter your message: ')

shifts =int(input('Please enter no.of shifts: '))

encrypt_text =''



for i in plain_text:

    if i in letters:

        position = letters.index(i)

        new_position = position + shifts



        if new_position > len(letters)-1:

            encrypt_text += letters[(new_position) - (len(letters))]

        else:

            encrypt_text+= letters[new_position]

    else:

        encrypt_text += i

       

print(encrypt_text)



#decrypting text

plain_text = input('Plese enter your message: ')

shifts =int(input('Please enter no.of shifts: '))

decrypt_text=''

for i in plain_text:

    if i in letters:

        position = letters.index(i)

        new_position = position - shifts



        if new_position > len(letters)-1:

            decrypt_text += letters[(new_position) -(len(letters))]

        else:

            decrypt_text += letters[new_position]

    else:

        decrypt_text += i

       

print(decrypt_text)

