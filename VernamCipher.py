avaliableChar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9'];

print 'Enter your Plain Text : ';
plainText = raw_input();

print 'Enter your Key : ';
key = raw_input();

if(len(plainText) != len(key)):
    print "Invalid key, application terminated.";

size = len(plainText);

plainValue = [size];
keyValue = [size];
cipherValue = [size];
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
    plainValue[i] = num;

for i in range(0, size):
    num = numValue(key[i])
    keyValue[i] = num;

for i in range(0,size) :
    print plainValue[i];


for i in range(0, size):
    cipherValue[i] = plainValue[i] + keyValue[i];
    if cipherValue[i] > 25:
        cipherValue[i] -= 26;

for i in range(0, size):
    Cipher += CharValue(cipherValue[i]);

print Cipher;






