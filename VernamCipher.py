
# 1. Secured text editor (Text encryption by
# Vernam Cipher)
from appJar import gui


avaliableChar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','0','1','2','3','4','5','6','7','8','9','\n'];

threshold = len(avaliableChar);

plainValue = [];
keyValue = [];
cipherValue = [];
Cipher = '';
Plain = '';

f = open('test.txt','r')
message = f.read()


def numValue(x):
    for i in range(0, len(avaliableChar)):
        if(x == avaliableChar[i]):
            num = i;
    return num;

def CharValue(x):
    char = avaliableChar[x];
    return char;


def Encryption(Cipher):

    plainValue = [];
    keyValue = [];
    cipherValue = [];
    Cipher = '';

    plainText = app.getEntry("plainText")
    size = len(app.getEntry("plainText"))
    key = app.getEntry("key")

    while (len(key) < len(plainText)):
        key += key;

    if (len(key) > len(plainText)):
        key = key[:len(plainText)];

    for i in range(0, size):
        num = numValue(plainText[i])
        plainValue.append(num);

    for i in range(0, size):
        num = numValue(key[i])
        keyValue.append(num);

    for i in range(0, size):
        plainval = plainValue[i];
        keyval = keyValue[i];
        cipherval = plainval + keyval;

        if cipherval > threshold - 1:
            cipherval -= threshold;
        cipherValue.append(cipherval);

    for i in range(0, size):
        Cipher += CharValue(cipherValue[i]);



    app.setLabel("output", Cipher)




def Decryption(Plain):

    plainValue = [];
    keyValue = [];
    cipherValue = [];
    Plain = '';

    cipherText = app.getEntry("plainText")
    key = app.getEntry("key")

    while(len(key) < len(cipherText)):
        key += key;

    if(len(key) > len(cipherText)):
        key = key[:len(cipherText)];

    size = len(cipherText);
    threshold = len(avaliableChar);



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


    app.setLabel("output", Plain)



#Change input message when change function
def change():

        if app.getRadioButton("options")=="Decryption":
            app.setLabel("EP", "Enter your Cipher Text :)")
        else:
            app.setLabel("EP", "Enter your Plain Text :)")




def press(button):
    if button == "Cancel":
        app.stop()

    elif button == "Reset":

        app.clearEntry("key", callFunction=False)
        app.clearEntry("plainText", callFunction=False)
        app.clearLabel("output")


    else:

        button == "Confirm"

        options = app.getRadioButton("options")

        if options == "Encryption":

            Encryption(Cipher)


        else:
            Decryption(Cipher)


def pressUpload():
    app.openBox(title="selectpPath", dirName=None, fileTypes=[('text', '*.txt')], asFile=False, parent=None)


app = gui()

app.setPadding([20,20])
app.setInPadding([2,2])

app.setTitle("Vernam Cipher Encryption ")


app.setSize("500x700")
app.setLocation("CENTER")

app.addButton("Upload", pressUpload)

app.addLabel("EP", "Enter your Plain Text :)")
app.getLabelWidget("EP").config(font=("Comic Sans", "30", "bold"))
app.setLabelFg("EP","Blue")

app.addEntry("plainText")
app.getEntryWidget("plainText").config(font=("Comic Sans", "20", "bold"))


app.addLabel("EK", "Enter your Key : ")
app.getLabelWidget("EK").config(font=("Comic Sans", "30", "bold"))


app.addEntry("key")
app.getEntryWidget("key").config(font=("Comic Sans", "20", "bold"))


app.setBg("pink", override=False)


app.addRadioButton("options", "Encryption")
app.getRadioButtonWidget("options", "Encryption").config(font=("Courier 20"))


app.addRadioButton("options", "Decryption")
app.getRadioButtonWidget("options", "Decryption").config(font=("Courier 20"))



app.setRadioButtonChangeFunction("options",change)


app.addLabel("output","")
app.getLabelWidget("output").config(font=("Sans Serif", "20", "bold"))
app.setLabelBg("output", "red")
app.setLabelFg("output", "yellow")



app.addButtons(["Confirm","Reset","Cancel"],press)


#app.go()




plainText = app.getEntry("plainText")





print message