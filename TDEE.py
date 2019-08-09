#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("TDEE Calculator")

ttk.Label(app, text="Unit", width=12).grid(column=0, row=0, padx=2)
ttk.Label(app, text="Age", width=12).grid(column=0, row=3, padx=2)
ttk.Label(app, text="Gender", width=12).grid(column=1, row=0, padx=2)
ttk.Label(app, text="Bodyfat", width=12).grid(column=1, row=3, padx=2)
ttk.Label(app, text="height1", width=12).grid(column=2, row=0, padx=2)
ttk.Label(app, text="height2", width=12).grid(column=2, row=3, padx=2)
ttk.Label(app, text="weight", width=12).grid(column=3, row=0, padx=2)
ttk.Label(app, text="Activity", width=12).grid(column=0, row=5, padx=2)
ttk.Label(app, text="Want to...", width=12).grid(column=2, row=5, padx=2)
ttk.Label(app, text="Diet", width=12).grid(column=3, row=5, padx=2)
ttk.Label(app, text="BMI", width=12).grid(column=0, row=7, padx=2)
ttk.Label(app, text="BMR", width=12).grid(column=1, row=7, padx=2)
ttk.Label(app, text="TDEE", width=12).grid(column=2, row=7, padx=2)

bmilabel = ttk.Label(app, text=bmi, width=12, ).grid(column=0, row=8, padx=2)
bmrlabel = ttk.Label(app, text="BMR", width=12, ).grid(column=1, row=8, padx=2)
tdeelable = ttk.Label(app, text="TDEE", width=12, ).grid(column=2, row=8, padx=2)
##### BMI #####
##### BMR #####
##### TDEE #####

def actcon(act):
    if act == 0:
        return 1.2
    elif act == 1:
        return 1.375
    elif act == 2:
        return 1.55
    elif act == 3:
        return 1.725
    elif act == 4:
        return 1.9
        
def gencon(gender):
    if gender == 1:
        return 5
    elif gender == 2:
        return -161
def bmi():
    if unit == 1 :
        h = 30.48*h1 + 2.54*h2
    elif unit == 2:
        pass
    return weight/h/h


def bmr():
    gcon = gencon(gender)
    if unit == 1 :
        h = 30.48*h1 + 2.54*h2
        return 22.0462*weight + 6.25*h - 5*age + gcon
    elif unit == 2:
        return 22.0462*weight + 6.25*h1 - 5*age + gcon

def tdee():
    acon = actcon(act)
    return bmr*acon


###### Unit #####

unit = tk.IntVar()

rad1 = tk.Radiobutton(app, text="Imperial", variable=unit, value=1)
rad1.grid(column=0, row=1, sticky=tk.W, padx=2)

rad2 = tk.Radiobutton(app, text="Metric", variable=unit, value=2)
rad2.grid(column=0, row=2, sticky=tk.W, padx=2)

##### Age #####

age = tk.IntVar()
ageEntered = ttk.Entry(app, width=12, textvariable=age)
ageEntered.grid(column=0, row=4, padx=2)

##### Gender #####

gender = tk.IntVar()

rad3 = tk.Radiobutton(app, text="Male", variable=gender, value=1)
rad3.grid(column=1, row=1, sticky=tk.W, padx=2)

rad4 = tk.Radiobutton(app, text="Female", variable=gender, value=2)
rad4.grid(column=1, row=2, sticky=tk.W, padx=2)

##### Bodyfat #####

fat = tk.DoubleVar()
fatEntered = ttk.Entry(app, width=12, textvariable=fat)
fatEntered.grid(column=1, row=4, padx=2)

##### height1 #####

h1 = tk.DoubleVar()
h1Entered = ttk.Entry(app, width=12, textvariable=h1)
h1Entered.grid(column=2, row=1, padx=2)

##### height2 #####

h2 = tk.DoubleVar()
h2Entered = ttk.Entry(app, width=12, textvariable=h2)
h2Entered.grid(column=2, row=4, padx=2)

##### Weight #####

weight = tk.DoubleVar()
weightEntered = ttk.Entry(app, width=12, textvariable=weight)
weightEntered.grid(column=3, row=1, padx=2)

##### Activity #####

act = tk.IntVar()
actChosen = ttk.Combobox(app, width=13, textvariable=act, state="readonly")
actChosen["values"] = ("Sedentary", "Light Exercise", "Moderate Exercise", "Heavy Exercise", "Athlete")
actChosen.grid(column=0, row=6, padx=2)
actChosen.current(0)

##### Want to... #####

want = tk.IntVar()
wantChosen = ttk.Combobox(app, width=13, textvariable=want, state="readonly")
wantChosen["values"] = ("Maintain", "Increase Muscles", "Loss fat")
wantChosen.grid(column=2, row=6, padx=2)
wantChosen.current(0)

##### Diet #####

diet = tk.IntVar()
dietChosen = ttk.Combobox(app, width=15, textvariable=diet, state="readonly")
dietChosen["values"] = ("Normal fitness", "Mediterranean Diet", "Keto Diet", "Paleo", "Vegan")
dietChosen.grid(column=3, row=6, padx=2)
dietChosen.current(0)





app.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




