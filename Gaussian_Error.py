import math
from uncertainties import ufloat
from uncertainties.umath import *
import tkinter as tk

def calc():
    if e1.get(): a = ufloat(e1.get(), float(e7.get()))
    if e2.get(): b = ufloat(e2.get(), float(e8.get()))
    if e3.get(): c = ufloat(e3.get(), float(e9.get()))
    if e4.get(): d = ufloat(e4.get(), float(e10.get()))
    if e5.get(): e = ufloat(e5.get(), float(e11.get()))
    if e6.get(): f = ufloat(e6.get(), float(e12.get()))
    solution["text"] = '{:.3u}'.format(eval(e13.get()))

def clear():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.delete(0, tk.END)
    e6.delete(0, tk.END)
    e7.delete(0, tk.END)
    e8.delete(0, tk.END)
    e9.delete(0, tk.END)
    e10.delete(0, tk.END)
    e11.delete(0, tk.END)
    e12.delete(0, tk.END)
    e13.delete(0, tk.END)


master = tk.Tk()
master.title("Gaussian Error Propagation")
tk.Label(master, text="Variable").grid(row=0, column=0)
tk.Label(master, text="Value").grid(row=0, column=1)
tk.Label(master, text="Accuracy").grid(row=0, column=2)

tk.Label(master, text="a").grid(row=1)#P
tk.Label(master, text="b").grid(row=2)#a
tk.Label(master, text="c").grid(row=3)#s
tk.Label(master, text="d").grid(row=4)#l
tk.Label(master, text="e").grid(row=5)#x
tk.Label(master, text="f").grid(row=6)#D
tk.Label(master, text='func').grid(row=7)

solution = tk.Label(master, text="")
solution.grid(row=8, column=2)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)

e7 = tk.Entry(master)
e8 = tk.Entry(master)
e9 = tk.Entry(master)
e10 = tk.Entry(master)
e11 = tk.Entry(master)
e12 = tk.Entry(master)

e13 = tk.Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)

e7.grid(row=1, column=2)
e8.grid(row=2, column=2)
e9.grid(row=3, column=2)
e10.grid(row=4, column=2)
e11.grid(row=5, column=2)
e12.grid(row=6, column=2)

e13.grid(row=7,column=1, columnspan=2,sticky = tk.W+tk.E)

e1.insert(10, "1")
e2.insert(10, "435")
e3.insert(10, "2.1")
e4.insert(10, "930")
e5.insert(10, "271")
e6.insert(10, "21")
e7.insert(10, "0")
e8.insert(10, "10")
e9.insert(10, "0.5")
e10.insert(10, "10")
e11.insert(10, "10")
e12.insert(10, "0.5")

e13.insert(10, "(a*b*pow(1+pow((c*d)/(e*f),2),1/2))/((c*d)/(e*f))")

tk.Button(master, text='Calc', command=calc).grid(row=8, column=1, sticky=tk.W, pady=4)
tk.Button(master, text='Clear', command=clear).grid(row=8, column=0, sticky=tk.W, pady=4)

master.mainloop()

tk.mainloop()
