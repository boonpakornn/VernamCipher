avaliableChar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',
                 'Y','Z',' ','0','1','2','3','4','5','6','7','8','9',' ','\n','.'];

PLAINTEXT= [];
num = 0;

with open("test.txt") as f:
  while True:
    c = f.read(1)
    if not c:
      break

    #print(ord(c))
    PLAINTEXT.append(c)


print PLAINTEXT




def numValue(x):
    for i in range(0, len(avaliableChar)):
        if(x == avaliableChar[i]):
            num = i;
            print num
    return num;


def CharValue(x):
    char = avaliableChar[x];
    return char;

print 'Please select type of Text Encryption (E (Encryption) / D (Decryption)) : ';
type = raw_input();

def encrypt():
    print 'Enter your Plain Text : ';
    plainText =  PLAINTEXT

    print 'Enter your Key : ';
    key = "T1e2s3t4";

    while(len(key) < len(plainText)):
        key += key;

    if(len(key) > len(plainText)):
        key = key[:len(plainText)];

    size = len(plainText);
    threshold = len(avaliableChar);

    plainValue = [];
    keyValue = [];
    cipherValue = [];
    Cipher = '';

    for i in range(0, size):
        print plainText

        num = numValue(plainText[i])
        plainValue.append(num);
        ######################
        print plainValue
        print len(plainValue)

    for i in range(0, size):
        num = numValue(key[i])
        keyValue.append(num);

    for i in range(0, size):
        plainval = plainValue[i];
        keyval = keyValue[i];
        cipherval = plainval+keyval;

        if cipherval > threshold-1:
            cipherval -= threshold;
        cipherValue.append(cipherval);

    for i in range(0, size):
        Cipher += CharValue(cipherValue[i]);

    return Cipher;

def decrypt():

    print 'Enter your Cipher Text : ';
    cipherText = "gcs.q154R cys1r"

    print 'Enter your Key : ';
    key = "T1e2s3t4"

    while(len(key) < len(cipherText)):
        key += key;

    if(len(key) > len(cipherText)):
        key = key[:len(cipherText)];

    size = len(cipherText);
    threshold = len(avaliableChar);

    cipherValue = [];
    keyValue = [];
    plainValue = [];
    Plain = '';

    for i in range(0, size):
        num = numValue(cipherText[i])
        cipherValue.append(num);

    for i in range(0, size):
        num = numValue(key[i])
        keyValue.append(num);

    for i in range(0, size):
        cipherval = cipherValue[i];
        keyval = keyValue[i];
        plainval = cipherval-keyval;

        if plainval < 0 :
            plainval += threshold;
        plainValue.append(plainval);

    for i in range(0, size):
        Plain += CharValue(plainValue[i]);

    return Plain;



if(type == 'E'):

    # PLAINTEXT
    #
    # for i in message:
    #
    #     output = encrypt();
    #
    # PLAINTEXT = output+

    print 'CipherText is : '

    output = encrypt();

    print output
elif(type == 'D'):
    output = decrypt();
    print 'PlainText is : '
    print output
else:
    print 'Invalid command, Application terminated';


