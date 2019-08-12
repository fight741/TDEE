from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("TDEE Calculator")

##### Function of BMI BMR TDEE #####
# Male, Metric as default

def bmi(unit=1, weight=1, h=1, h1=1, h2=1):  
    if unit == 1 :
        return weight/((h/100)**2)
    elif unit == 2:
        ih = 30.48*h1 + 2.54*h2
        iw = weight/2.20462
        return iw/((ih/100)**2)
# 1 = Metric ; 2 = Imperial

def bmr(unit=1, gender=1, age=0, weight=1, h=1, h1=1, h2=1):
    if gender == 1:
        gcon = 5
    elif gender == 2:
        gcon = -161
        
    if unit == 1 :
        return 10*weight + 6.25*h - 5*age + gcon
    elif unit == 2:
        ih = 30.48*h1 + 2.54*h2
        iw = weight/2.20462
        return 10*iw + 6.25*ih - 5*age + gcon
# 1 = Metric ; 2 = Imperial
    
def tdee(bmr, act):
    if act == 0:
        return bmr*1.2
    elif act == 1:
        return bmr*1.375
    elif act == 2:
        return bmr*1.55
    elif act == 3:
        return bmr*1.725
    elif act == 4:
        return bmr*1.9

def ccb():
    gunit = unit.get()
    ggender = gender.get()
    gage = age.get()
    gweight = weight.get()
    gh = h1.get()
    gh1 = h1.get()
    gh2 = h2.get()
    gact=act.get()
    
    if gact == "Sedentary":
        gact=0
    elif gact == "Light Exercise":
        gact=1
    elif gact == "Moderate Exercise":
        gact=2
    elif gact == "Heavy Exercise":
        gact=3
    elif gact == "Athlete":
        gact=4

    bmilabel.config(text=round(bmi(gunit, gweight, gh, gh1, gh2), 2))
    bmrlabel.config(text=round(bmr(gunit, ggender, gage, gweight, gh, gh1, gh2), 2))
    tdeelable.config(text=round(tdee(bmr(gunit, ggender, gage, gweight, gh, gh1, gh2), gact), 2))
    
ttk.Label(app, text="Unit", width=12).grid(column=0, row=0, padx=2)
ttk.Label(app, text="Age", width=12).grid(column=1, row=0, padx=2)
ttk.Label(app, text="Gender", width=12).grid(column=0, row=3, padx=2)
ttk.Label(app, text="Bodyfat", width=12).grid(column=1, row=2, padx=2)
ttk.Label(app, text="cm or ft.", width=12).grid(column=2, row=0, padx=2)
ttk.Label(app, text="inch", width=12).grid(column=2, row=2, padx=2)
ttk.Label(app, text="Weight", width=12).grid(column=1, row=4, padx=2)
ttk.Label(app, text="Activity", width=12).grid(column=2, row=4, padx=2)
ttk.Label(app, text="BMI", width=12).grid(column=4, row=0, padx=2)
ttk.Label(app, text="BMR", width=12).grid(column=4, row=2, padx=2)
ttk.Label(app, text="TDEE", width=12).grid(column=4, row=4, padx=2)

bmilabel = ttk.Label(app, font = "Verdana 10 bold", background="light grey", width=12)
bmilabel.grid(column=4, row=1, padx=2)
bmrlabel = ttk.Label(app, font = "Verdana 10 bold", background="light grey", width=12)
bmrlabel.grid(column=4, row=3, padx=2)
tdeelable = ttk.Label(app, font = "Verdana 10 bold", background="light grey", width=12)
tdeelable.grid(column=4, row=5, padx=2)


###### Unit #####

unit = tk.IntVar()

rad1 = tk.Radiobutton(app, text="Metric", variable=unit, value=1)
rad1.grid(column=0, row=1, sticky=tk.W, padx=2)

rad2 = tk.Radiobutton(app, text="Imperial", variable=unit, value=2)
rad2.grid(column=0, row=2, sticky=tk.W, padx=2)

##### Age #####

age = tk.IntVar()
ageEntered = ttk.Entry(app, width=12, textvariable=age)
ageEntered.grid(column=1, row=1, padx=2)

##### Gender #####

gender = tk.IntVar()

rad3 = tk.Radiobutton(app, text="Male", variable=gender, value=1)
rad3.grid(column=0, row=4, sticky=tk.W, padx=2)

rad4 = tk.Radiobutton(app, text="Female", variable=gender, value=2)
rad4.grid(column=0, row=5, sticky=tk.W, padx=2)

##### Bodyfat #####

fat = tk.DoubleVar()
fatEntered = ttk.Entry(app, width=12, textvariable=fat)
fatEntered.grid(column=1, row=3, padx=2)

##### height1 #####

h1 = tk.DoubleVar()
h1Entered = ttk.Entry(app, width=12, textvariable=h1)
h1Entered.grid(column=2, row=1, padx=2)

##### height2 #####

h2 = tk.DoubleVar()
h2Entered = ttk.Entry(app, width=12, textvariable=h2)
h2Entered.grid(column=2, row=3, padx=2)

##### Weight #####

weight = tk.DoubleVar()
weightEntered = ttk.Entry(app, width=12, textvariable=weight)
weightEntered.grid(column=1, row=5, padx=2)

##### Activity #####

act = tk.StringVar()
actChosen = ttk.Combobox(app, width=13, textvariable=act, state="readonly")
actChosen["values"] = ("Sedentary", "Light Exercise", "Moderate Exercise", "Heavy Exercise", "Athlete")
actChosen.grid(column=2, row=5, padx=2)
actChosen.current(0)

##### Button #####

cb = ttk.Button(app, text="Calculate !", command=ccb)
cb.grid(column=3, row=3, padx=2)

#####

app.mainloop()
