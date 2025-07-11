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
canvas = tk.Canvas(canvas_frame, height=300, width=300, bg='white')
canvas.pack()   





#ACCESSORIES
glasses_var = tk.BooleanVar()
glasses_button = ttk.Checkbutton(accessory_frame, text='Glasses', variable=glasses_var, style='glassesstyle.TCheckbutton')
glasses_button.pack(anchor=tk.W, pady=5)

hat_var = tk.BooleanVar()
hat_button = ttk.Checkbutton(accessory_frame, text='Hat', variable=hat_var, style='hatstyle.TCheckbutton')
hat_button.pack(anchor=tk.W, pady=5)


beard_var = tk.BooleanVar()
beard_button = ttk.Checkbutton(accessory_frame, text='Beard', variable=beard_var, style='beardstyle.TCheckbutton')
beard_button.pack(anchor=tk.W, pady=5)





#GENDER
gender_var = tk.StringVar()
male_button = ttk.Radiobutton(genderandcolor_frame, value='male', variable=gender_var, text='Male', style='male.TRadiobutton')
male_button.pack(anchor=tk.E, pady=0, padx=22)
male_button.bind('<Button-1>', lambda event: canvas.create_rectangle(170,250, 190,200))

female_button = ttk.Radiobutton(genderandcolor_frame, value='female', variable=gender_var,text='Female', style='female.TRadiobutton')
female_button.pack(anchor=tk.E, pady=15)





#COLOR THEMES
colortheme_label = ttk.Label(genderandcolor_frame, text='Color theme:', style='colorthemelabel.TLabel')
colortheme_label.pack(anchor=tk.W)
colortheme_items = ('BLUE', 'RED', 'GREEN', 'YELLOW', 'WHITE', 'BLACK')
colortheme = ttk.Spinbox(genderandcolor_frame, values=colortheme_items)
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






















window.mainloop()
 

