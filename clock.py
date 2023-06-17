from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import*
from time import*
from math import*
class Clock:
    def __init__(self,root):
        self.root=root
        self.root.title('GUI analog cum digital clock')
        self.root.geometry('1300x700+0+0')
        self.root.config(bg='#EADDCA')
        frame = Frame(self.root, width=1000, height=650,bg='yellow',bd=5,relief='solid')
        frame.place(x=195, y=150)
        title=Label(self.root,text='CLOCK',font=('times new roman',50,'bold'),bg='blue',fg='white',bd=5,relief='solid').place(x=0,y=50,relwidth=1)
        #analog clock
        self.lbl1=Label(frame,bg='white',bd=7,relief=SOLID)
        self.lbl1.place(x=100,y=150,height=400,width=400)
        #digital clock
        self.lbl2_time=Label(frame,font=('times new roman',50),fg='white',bg='#FF5733',bd=5,relief='solid')
        self.lbl2_time.place(x=580,y=250,height=100,width=400)
        self.lbl3_day=Label(frame,font=('times new roman',50),fg='black',bg='white',bd=5,relief='solid')
        self.lbl3_day.place(x=580,y=350,height=100,width=400)
        self.lbl4_date=Label(frame,font=('times new roman',50),fg='white',bg='green',bd=5,relief='solid')
        self.lbl4_date.place(x=580,y=450,height=100,width=400)
        self.working_analog()
        self.working_digital()
    def clock_image(self,hr,min,sec):
        clock=Image.new("RGB",(400,400),('white'))
        draw=ImageDraw.Draw(clock)
        #clock Image
        bg=Image.open('clk.jpg')
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        org=200,200
        #hour hands image
        draw.line((org,200+40*sin(radians(hr)),200-40*cos(radians(hr))),fill='black',width=5)
        # minute hands image
        draw.line((org,200+60*sin(radians(min)),200-60*cos(radians(min))),fill='black',width=4)
        #seconds hands image
        draw.line((org,200+90*sin(radians(sec)),200-90*cos(radians(sec))),fill='black',width=2)
        # draw.ellipse((195,195,210,210),fill='black')
        clock.save('clock.png')
    def working_analog(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second     
        hr=(h/12)*360
        min=(m/60)*360
        sec=(s/60)*360
        self.clock_image(hr,min,sec)
        self.img=ImageTk.PhotoImage(file='clock.png')
        self.lbl1.config(image=self.img)#to place that image into that level
        self.lbl1.after(1000,self.working_analog)
    def working_digital(self):
        time_str=strftime('%I:%M:%S %p')#%I-hour %M-minute %S-Second %p-AM/PM
        
        self.lbl2_time.config(text=time_str)
        day_str=strftime('%A')
        date_str=strftime('%d %B %Y')
        self.lbl3_day.config(text=date_str)
        
        
        self.lbl4_date.config(text=day_str)
        self.root.after(1000,self.working_digital)#for updating the whole date day time


root=Tk()
obj=Clock(root)
root.mainloop()
