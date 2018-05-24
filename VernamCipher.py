avaliableChar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9'];

print 'Enter your Plain Text : ';
plainText = raw_input();

print 'Enter your Key : ';
key = raw_input();

if(len(plainText) != len(key)):
    print "Invalid key, application terminated.";

size = len(plainText);
threshold = len(avaliableChar);

plainValue = [];
keyValue = [];
cipherValue = [];
Cipher = '';


def numValue(x):
    for i in range(0, len(avaliableChar)):
        if(x == avaliableChar[i]):
            num = i;
    return num;

def CharValue(x):
    char = avaliableChar[x];
    return char;

for i in range(0, size):
    num = numValue(plainText[i])
    plainValue.append(num);

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

print 'CipherText is : '
print Cipher;






