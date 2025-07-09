import tkinter as tk 
from tkinter import ttk
import tkinter.font

window = tk.Tk()
window.geometry('800x800')
window.title('Make a Character')

    
s = ttk.Style()
s.configure('glassesstyle.TCheckbutton', font=('Helvetica', 14, 'bold'), foreground="#2C2C2C")
s.configure('hatstyle.TCheckbutton', font=('Helvetica', 14, 'bold'), foreground="#2C2C2C")
s.configure('beardstyle.TCheckbutton', font=('Helvetica', 14, 'bold'), foreground="#2C2C2C")
s.configure('male.TRadiobutton', font=('Helvetica', 14, 'bold'), foreground="#2C2C2C")
s.configure('female.TRadiobutton', font=('Helvetica', 14, 'bold'), foreground="#2C2C2C")
s.configure('colorthemelabel.TLabel', font=('Helvetica', 14, 'bold'), foreground="#2C2C2C")
#LABEL
label = tk.Label(window, text='Tkinter Avatar Customizer', font=('Inter', 20, 'bold'), fg="#4A4A4A")
label.pack(pady=10)


#FRAMES
top_frame = ttk.Frame(window)
top_frame.pack(pady=20)

accessory_frame = ttk.Frame(top_frame)
accessory_frame.pack(side=tk.LEFT, padx=30)

canvas_frame=ttk.Frame(top_frame)
canvas_frame.pack(side=tk.LEFT, padx=30)

genderandcolor_frame=ttk.Frame(top_frame)
genderandcolor_frame.pack(side=tk.LEFT, padx=30)

colortheme_frame = ttk.Frame(top_frame)
colortheme_frame.pack(side=tk.LEFT, padx=2)

agenameandsaveoptions_frame=  ttk.Frame(top_frame)
agenameandsaveoptions_frame.pack(side=tk.LEFT, padx=30)

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

female_button = ttk.Radiobutton(genderandcolor_frame, value='female', variable=gender_var,text='Female', style='female.TRadiobutton')
female_button.pack(anchor=tk.E, pady=15)


#COLOR THEMES
colortheme_label = ttk.Label(genderandcolor_frame, text='Color theme:', style='colorthemelabel.TLabel')
colortheme_label.pack(anchor=tk.E)
colortheme_items = ('BLUE', 'RED', 'GREEN', 'YELLOW', 'WHITE', 'BLACK')
colortheme = ttk.Spinbox(genderandcolor_frame, values=colortheme_items)
colortheme.pack(anchor=tk.E)


#AGE
age_spinbox_items = 1 +=  
age_spinbox = ttk.Spinbox(agenameandsaveoptions_frame, )





























window.mainloop()



