import tkinter as tk 
from tkinter import ttk
import tkinter.font

window = tk.Tk()
window.geometry('800x800')
window.title('Make a Character')

#STYLES   
s = ttk.Style()
s.configure('glassesstyle.TCheckbutton', font=('Helvetica', 14, 'bold'), foreground="#2C2C2C")
s.configure('hatstyle.TCheckbutton', font=('Helvetica', 14, 'bold'), foreground="#2C2C2C")
s.configure('beardstyle.TCheckbutton', font=('Helvetica', 14, 'bold'), foreground="#2C2C2C")
s.configure('male.TRadiobutton', font=('Helvetica', 14, 'bold'), foreground="#2C2C2C")
s.configure('female.TRadiobutton', font=('Helvetica', 14, 'bold'), foreground="#2C2C2C")
s.configure('colorthemelabel.TLabel', font=('Helvetica', 12, 'bold'), foreground="#2C2C2C")
s.configure('agelabel.TLabel', font=('Helvetica', 12, 'bold'), foreground="#2C2C2C")
s.configure('namelabel.TLabel', font=('Helvetica', 12, 'bold'), foreground="#2C2C2C")





#LABEL
label = tk.Label(window, text='Tkinter Avatar Customizer', font=('Inter', 20, 'bold'), fg="#4A4A4A")
label.pack(pady=10)





#FRAMES
#TOP FRAME
top_frame = ttk.Frame(window)
top_frame.pack(pady=20)

accessory_frame = ttk.Frame(top_frame)
accessory_frame.pack(side=tk.LEFT, padx= 55)

canvas_frame=ttk.Frame(top_frame)
canvas_frame.pack(side=tk.LEFT, padx=30)

genderandcolor_frame=ttk.Frame(top_frame)
genderandcolor_frame.pack(side=tk.LEFT, padx=30)





#BOTTOM FRAME
bottom_frame =ttk.Frame(window)
bottom_frame.pack(pady=20, padx=10)

ageanamelabelandsavebutton_frame = ttk.Frame(bottom_frame)
ageanamelabelandsavebutton_frame.pack(side=tk.LEFT, padx=20)

agespinboxnameentryandresetbutton_frame =ttk.Frame(bottom_frame)
agespinboxnameentryandresetbutton_frame.pack(side=tk.LEFT, padx=20)





#CANVAS
# canvas = tk.Canvas(canvas_frame, height=300, width=300)
# canvas.pack()   





#ACCESSORIES
def draw_glasses(event):
    if glasses_var.get():
        canvas.delete('glasses')
    else:
        (canvas.create_oval(110, 100, 140,130, width=1, tags='glasses'), canvas.create_line(140,115, 152,110 ,165,115, smooth=1, tags='glasses'),canvas.create_oval(165,100, 195,130, tags='glasses'))   
glasses_var = tk.BooleanVar()
glasses_button = ttk.Checkbutton(accessory_frame, text='Glasses', variable=glasses_var, style='glassesstyle.TCheckbutton')
glasses_button.bind('<ButtonRelease-1>', draw_glasses)
glasses_button.pack(anchor=tk.W, pady=5)


hat_var = tk.BooleanVar()
hat_button = ttk.Checkbutton(accessory_frame, text='Hat', variable=hat_var, style='hatstyle.TCheckbutton')
hat_button.pack(anchor=tk.W, pady=5)


def draw_beard(event):
    if beard_var.get():
        canvas.delete('beard')
    else:
        (canvas.create_polygon(85, 125, 110, 172, 135, 130, 140, 130, 153, 150, 160, 145, 173, 130, 178, 130, 198, 172, 223, 125, 220, 135, 215, 150, 210, 
                                                                    165, 200, 180, 185, 195, 152, 205, 120, 195, 105, 180, 95, 165, 90, 150, 85, 135, fill="#5f3d26", outline="", width=0, tags='beard'), 
                                                                    (canvas.create_line(135, 153, 150, 165, 170,153, width=3, smooth=1, tags='beard') ))
beard_var = tk.BooleanVar()
beard_button = ttk.Checkbutton(accessory_frame, text='Beard', variable=beard_var, style='beardstyle.TCheckbutton')
beard_button.bind('<ButtonRelease-1>',draw_beard)
beard_button.pack(anchor=tk.W, pady=5)





#GENDER
gender_var = tk.StringVar()
male_button = ttk.Radiobutton(genderandcolor_frame, value='male', variable=gender_var, text='Male', style='male.TRadiobutton')
male_button.pack(anchor=tk.E, pady=0, padx=22)
male_button.bind('<Button-1>', lambda event: (
canvas.create_polygon([
    120,193, 120,205, 118,210, 115,213, 110,215,
    105,217, 100,220, 95,225, 90,230, 85,235, 80,240, 75,250, 70,265,
    65,280, 60,300, 57,320, 55,350, 55,450,
    250,450, 255,350, 253,320, 250,300, 245,280, 240,265, 235,250,
    230,240, 225,235, 220,230, 215,225, 210,220, 205,217, 200,215,
    195,213, 190,210, 188,207, 185,205, 185,193,
    120,193
], fill="#2392ab", outline="black", width=3, smooth=True),
canvas.create_oval(85,50,220,205, width=4, fill="#fbdbba"), #HEAD 
                                              canvas.create_oval(85,110, 70,150, fill="#fbdbba", width=4),#EAR LEFT
                                              canvas.create_oval(220,110, 235,150, fill="#fbdbba", width=4), #EAR RIGHT
                                              canvas.create_oval(120, 110, 130,120, fill='black', width=2) , #EYE LEFT
                                              canvas.create_oval(175, 110, 185,120, fill='black', width=2), #EYE RIGHT
                                              canvas.create_line(135, 153, 150, 165, 170,153, width=3, smooth=1), #SMILE
                                              canvas.create_line(110,240, 115,300, width=2),
                                              canvas.create_line(200,240, 195,300, width=2)

                                              ))





female_button = ttk.Radiobutton(genderandcolor_frame, value='female', variable=gender_var,text='Female', style='female.TRadiobutton')
female_button.pack(anchor=tk.E, pady=15)


canvas = tk.Canvas(canvas_frame, height=300, width=300, bg='white')
canvas.pack()   



#COLOR THEMES
colortheme_label = ttk.Label(genderandcolor_frame, text='Color theme:', style='colorthemelabel.TLabel')
colortheme_label.pack(anchor=tk.W)
colortheme_items = ('BLUE', 'RED', 'GREEN', 'YELLOW', 'WHITE', 'BLACK')
colortheme = ttk.Spinbox(genderandcolor_frame, values=colortheme_items)
colortheme.bind('<<SpinboxSelected>>', lambda event: canvas.config(bg=colortheme.get()))
colortheme.bind('<KeyRelease>', lambda event: canvas.config(bg=colortheme.get()))
colortheme.bind('<ButtonRelease-1>', lambda event: canvas.config(bg=colortheme.get()))
colortheme.pack(anchor=tk.E)





#AGE
age_label = ttk.Label(ageanamelabelandsavebutton_frame, text='Age:', style='agelabel.TLabel')
age_label.pack(anchor=tk.W)
age_spinbox = ttk.Spinbox(agespinboxnameentryandresetbutton_frame, from_=1, to=120)
age_spinbox.pack(anchor=tk.W)





#NAME
name_label = ttk.Label(ageanamelabelandsavebutton_frame, text='Name:', style='namelabel.TLabel')
name_label.pack(anchor=tk.W)

name_entry = ttk.Entry(agespinboxnameentryandresetbutton_frame)
name_entry.pack(anchor=tk.W,pady=2)





#SAVE 
save_button = ttk.Button(ageanamelabelandsavebutton_frame, text='Save')
save_button.pack(anchor=tk.W, pady=30)





#RESET
reset_button = ttk.Button(agespinboxnameentryandresetbutton_frame, text='Reset')
reset_button.pack(anchor=tk.W, pady=30)
reset_button.bind('<Button-1>', lambda event: (canvas.delete('all'), gender_var.set(''), age_spinbox.set(''), name_entry.delete(0,tk.END), glasses_var.set(False), 
                                               hat_var.set(False), beard_var.set(False), colortheme.set(''), canvas.config(bg='white')))






















window.mainloop()
 

