# QrCode Generator and Detector 
from qrcode.main import QRCode 
import random 
from tkinter import * 
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

 
name = 'tempfile_00'+str(random.randint(0,999))

path = '' # ((<pyimage2>)) / path_specified 
file_name = os.path.basename(path) #File name
 
# QRCode_Generator
def qrcode_generator(data, name=name):
    global path
    qrcode = QRCode(version=1) 
    qrcode.add_data(data) 
    image = qrcode.make_image() 
    image.save(f'{name}.png')
    path = f'{name}.png'
    # print(f'Name of obj: {name}.png')


# QRCode_Detector
def qrcode_detector(code):
    import cv2
    detector = cv2.QRCodeDetector()
    img = cv2.imread(code)
    data, points, straight_qrcode = detector.detectAndDecode(img)
    print(f'Data in qrcode: {data}')
    entryVar.set(data)

# Functions
def save():
    save = asksaveasfilename(filetypes=[('Png Files', '*.png')])
    qrcode_generator(data=entryVar.get(),
                     name=f'{save}')
    # os.rename(str(path), str(save))
    clear()
 
def clear():
    global path, file_name
    entryVar.set('')
    path = ''
    Label(root, relief=RIDGE).place(x=590,y=60)

    try:
        # For Generator Window
        os.remove(file_name)
    except:
        # For Detector Window
        file_name = ''



def open():
    global file_name, path
    path = askopenfilename(filetypes=[('Png Files', '*.png')])
    file_name = os.path.basename(path)
    img = PhotoImage(file=file_name)
    file_name=img
    Label(root, image=img, relief=RIDGE, width=290,height=290).place(x=590,y=60)


# Generator Window & Its Functions
def generator():
    root.title('QRCode Generator') 
    root.geometry('900x500+500+250') 
    root.resizable(False,False)

    lbl.config(text="QRCode Generator")
    
    Button(root, text='Save',font=('Constantia', '15'), command=save).place(x=635,y=365, width=90, height=30) 
    Button(root, text='Clear',font=('Constantia', '15'), command=clear).place(x=740,y=365, width=90, height=30) 
 
    lbl2.config(text='Enter your data:') 
    entry.config(font=('Constantia', '15', 'bold'))

    Button(root, text='Submit',font=('Constantia', '15'), command=lambda:generator_submit(entryVar.get())).place(x=690,y=445, width=150, height=35) 


def generator_submit(data):
    qrcode_generator(data)
    global path, file_name
    file_name = os.path.basename(path)
    img = PhotoImage(file=file_name)
    path=img
    Label(root, image=img, relief=RIDGE,width=290,height=290).place(x=590,y=60, width=290, height=290)

# Detector Window  & Its Functions
def detector():
    root.title('QRCode Detector') 
    root.geometry('900x500+500+250') 
    root.resizable(False,False)

    lbl.config(text="QRCode Detector")
 
    Button(root, text='Open',font=('Constantia', '15'), command=open).place(x=635,y=365, width=90, height=30) 
    Button(root, text='Submit',font=('Constantia', '15'), command=lambda: detector_submit()).place(x=740,y=365, width=90, height=30) 
 
    lbl2.config(text='Your data is here:') 
 
    # entryVar = StringVar() 
    entry.config(font=('Constantia', '11'))

    Button(root, text='Clear',font=('Constantia', '15'), command=clear).place(x=690,y=445, width=150, height=35) 

def detector_submit():
    qrcode_detector(code=path)


# Main Window
if __name__ == '__main__': 
    root = Tk() 
    root.title('QRCode Generator') 
    root.geometry('900x500+500+250') 
    root.resizable(False,False)
    icon_image = PhotoImage(file='icon.png')
    root.iconphoto(False,icon_image)

    bg_image = PhotoImage(file='background.png')
    lbl = Label(root, image=bg_image).place(x=0,y=0)

    lbl = Label(root, text='QrCode Generator',font=('Constantia', '45', 'bold'), bg='#ECDBBE')
    lbl.place(x=30,y=50)
    
    Button(root, text='Save',font=('Constantia', '15'), command=save).place(x=635,y=365, width=90, height=30) 
    Button(root, text='Clear',font=('Constantia', '15'), command=clear).place(x=740,y=365, width=90, height=30) 
 
    lbl2 = Label(root, text='Enter your data:',font=('Constantia', '18', 'bold'),bg='#ECDBBE')
    lbl2.place(x=30,y=375) 
 
    entryVar = StringVar() 
    entry = Entry(root,font=('Constantia', '15', 'bold'), textvariable=entryVar)
    entry.place(x=30,y=410, width=840, height=30)

    Button(root, text='Submit',font=('Constantia', '15'), command=lambda:generator_submit(entryVar.get())).place(x=690,y=445, width=150, height=35) 
 
    menu = Menu(root) 
    fileMenu = Menu(menu, tearoff=0) 
    menu.add_cascade(label='QRCode Generator', command=generator) 
    menu.add_cascade(label='QRCode Detector', command=detector) 
 
    root.config(menu=menu) 
 
    root.mainloop()
