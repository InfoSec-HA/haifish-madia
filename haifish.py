from tkinter import *
import tkinter.scrolledtext as sc
import threading
from bs4 import BeautifulSoup as bs 
from tkinter import ttk
import requests

root = Tk()
root.geometry('970x560')
root.title('Haifish-media script is created by Eng InfoSec-HA')
root.configure(background='whitesmoke')

# Images
fac_img = PhotoImage(file='img/fac.png')
git_img = PhotoImage(file='img/git.png')
inst_img = PhotoImage(file='img/ins.png')
tel_img = PhotoImage(file='img/tel.png')
x_img = PhotoImage(file='img/x.png')


# Define 
def data():
    username = en1.get()
    def face():
        fac_url = 'https://www.facebook.com/'
        r = requests.get(fac_url+username)
        soup = bs(r.content,'html.parser')
        title1 = soup.find('title')
        al = title1.string 
        if al == 'facebook':
            text1.insert('end','[+] Facebook :','blue')
            text1.insert('end',username,'gray')
            text1.insert('end','\n')
            text1.insert('end',fac_url+username)
            text1.insert('end','[X] Not Found ','red')
            text1.insert('end','\n-----------------\n')
        else:
            tv.insert(parent='',index=0,image=fac_img,values=('facebook',fac_url,username,'Found'))
            
    def ins():
        ins_url = 'https://www.instagram.com/'
        r = requests.get(ins_url+username)
        soup = bs(r.content,'html.parser')
        title1 = soup.find('title')
        al = title1.string 
        if al == 'instagram':
            text1.insert('end','[+] Instagram :','blue')
            text1.insert('end',username,'gray')
            text1.insert('end','\n')
            text1.insert('end',ins_url+username)
            text1.insert('end','[X] Not Found ','red')
            text1.insert('end','\n-----------------\n')
        else:
            tv.insert(parent='',index=0,image=inst_img,values=('instagram',ins_url,username,'Found'))
    def git():
        git_url = 'https://github.com/'
        r = requests.get(git_url+username)
        soup = bs(r.content,'html.parser')
        title1 = soup.find('title')
        al = title1.string 
        if al == 'github':
            text1.insert('end','[+] Github :','blue')
            text1.insert('end',username,'gray')
            text1.insert('end','\n')
            text1.insert('end',git_url+username)
            text1.insert('end','[X] Not Found ','red')
            text1.insert('end','\n-----------------\n')
        else:
            tv.insert(parent='',index=0,image=git_img,values=('github',git_url,username,'Found'))
    def x():
        x_url = 'https://x.com/'
        r = requests.get(x_url+username)
        soup = bs(r.content,'html.parser')
        title1 = soup.find('title')
        al = title1.string 
        if al == 'x':
            text1.insert('end','[+] X :','blue')
            text1.insert('end',username,'gray')
            text1.insert('end','\n')
            text1.insert('end',x_url+username)
            text1.insert('end','[X] Not Found ','red')
            text1.insert('end','\n-----------------\n')
        else:
            tv.insert(parent='',index=0,image=x_img,values=('x',x_url,username,'Found'))
    def tel():
        tel_url = 'https://telegram.org/'
        r = requests.get(tel_url+username)
        soup = bs(r.content,'html.parser')
        title1 = soup.find('title')
        al = title1.string 
        if al == 'telegram':
            text1.insert('end','[+] Telegram :','blue')
            text1.insert('end',username,'gray')
            text1.insert('end','\n')
            text1.insert('end',tel_url+username)
            text1.insert('end','[X] Not Found ','red')
            text1.insert('end','\n-----------------\n')
        else:
            tv.insert(parent='',index=0,image=tel_img,values=('telegram',tel_url,username,'Found'))
    tel()
    x()
    git()
    ins()
    face()
def go():
    threading.Thread(target=data).start()
    
# Title
title = Label(root, text='Haifish-media for finding pepole accounts', font=('Courier,18'), fg='black')
title.pack(fill=X)

# Image Logo
photo = PhotoImage(file='run2.png')
panel = Label(root, image=photo)
panel.place(x=2,y=35,width='200',height='440')
# Entry
usr = Label(root,text='Enter the targent name :')
usr.place(x=5,y=400)
en1 = Entry(root, font=('Arial','12'), justify =CENTER)
en1.place(x=30,y=480,width=150,height=24)

# Button

button1 = Button(root,text='run',width=10,height=1,cursor='hand2',command=go)
button1.place(x=30,y=513 )

# TreeView
tv = ttk.Treeview(root)
style = ttk.Style(root)
style.theme_use('clam')
style.configure('Treeview',rowheight=35,background='#D8D8D8',fieldbackground='#D8D8D8',foreground='black')
tv['columns']=('namesocial','urlname','username','status')

tv.column('#0',anchor=CENTER, width=50)
tv.column('namesocial',anchor=CENTER, width=40)
tv.column('urlname',anchor=CENTER, width=130)
tv.column('username',anchor=CENTER, width=100)
tv.column('status',anchor=CENTER, width=30)

tv.heading('#0', text='Social Madia',anchor=CENTER)
tv.heading('namesocial', text='Social Name',anchor=CENTER)
tv.heading('urlname', text='Link',anchor=CENTER)
tv.heading('username', text='User Name ',anchor=CENTER)
tv.heading('status', text='Status',anchor=CENTER)
tv.place(x=205,y=35,width=765,height=240)

# Text & scrol
text1 = sc.ScrolledText(root)
text1['font']=('courier','10','bold')
text1.place(x=205,y=280,width=760,height=270)
text1.tag_config('red',background='red',foreground='white')
text1.tag_config('gray',background='red',foreground='gray')
text1.tag_config('blue',background='blue',foreground='white')

root.mainloop()