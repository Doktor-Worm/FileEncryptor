import base64

fileUsed = open(r"DayNight.txt", "r")
lines = fileUsed.readlines()
String = ' '.join(map(str, lines))
#The line above makes the list into a string for further encrpytion
encryptType = input("Put in 16,32,64,85")
encryptedp1 = String.encode("ascii")
#begins part of the encryption process that is reused throughout


if encryptType == '16':
    h = open('HexadecimalEncrypt.txt', 'w')
    hc1 = base64.b16encode(encryptedp1)
    fhf = hc1.decode("ascii")
    h.write(fhf)
    #encrypts file in base16 and creates a new file with the name HexadecimalEncrypt.txt
elif encryptType == '32':
    c = open('base32Encrpytion.txt', 'w')
    cc1 = base64.b32encode(encryptedp1)
    fcf = cc1.decode("ascii")
    c.write(fcf)
    # encrypts file in base32 and creates a new file for it
elif encryptType == '64':
    s = open('base64Encryption.txt', 'w')
    encryptp2 = base64.b64encode(encryptedp1)
    finalencrypt = encryptp2.decode("ascii")
    s.write(finalencrypt)
    # encrypts file in base65 and creates a new file for it
elif encryptType == '85':
    e = open('Base85encrypt.txt', 'w')
    ec1 = base64.b85encode(encryptedp1)
    fef = ec1.decode("ascii")
    e.write(fef)
    # encrypts file in base85 and creates a new file for it
print("File encrypted")