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

#LABEL
label = tk.Label(window, text='Tkinter Avatar Customizer', font=('Inter', 20, 'bold'), fg="#4A4A4A")
label.pack()




#ACCESSORIES

glasses_var = tk.BooleanVar()
glasses_button = ttk.Checkbutton(window, text='Glasses', variable=glasses_var, style='glassesstyle.TCheckbutton')
glasses_button.pack(side=tk.TOP, anchor=tk.NW, pady=5, padx=80)

hat_var = tk.BooleanVar()
hat_button = ttk.Checkbutton(window, text='Hat', variable=hat_var, style='hatstyle.TCheckbutton')
hat_button.pack(side=tk.TOP, anchor=tk.NW, pady=5, padx=80)


beard_var = tk.BooleanVar()
beard_button = ttk.Checkbutton(window, text='Beard', variable=beard_var, style='beardstyle.TCheckbutton')
beard_button.pack(side=tk.TOP, anchor=tk.NW, pady=5, padx=80)




#GENDER

male_button = ttk.Radiobutton(window, value='male', text='Male')
male_button.pack(side=tk.TOP, anchor=tk.NE, pady=10, padx=82)

female_button = ttk.Radiobutton(window, value='female', text='Female')
female_button.pack(side=tk.TOP, anchor=tk.NE, pady=10, padx=70)


































window.mainloop()

