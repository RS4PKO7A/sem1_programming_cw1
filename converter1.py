from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()

def CurrencyConversion():
    from_cur=var.get()
    to_cur=var1.get()
    amount=(e1.get())
    try:
        amount = float(amount)
        if from_cur == 'Currency' and to_cur == 'Currency':
            messagebox.showerror("No input!!", "Please choose a currency to convert.")
        elif from_cur == to_cur:
            messagebox.showinfo("No conversion", "Please select a different currency to convert.")
            total = amount
            output.set(total)
        # Conversion of Nepalese Rupees (NPR)
        elif from_cur == 'Nepalese Rupees (NPR)' and to_cur == 'United States (USD)':
            total = amount * 0.0083
            output.set(total)
        elif from_cur == 'Nepalese Rupees (NPR)' and to_cur == 'European (EUR)':
            total = amount * 0.0075
            output.set(total)
        elif from_cur == 'Nepalese Rupees (NPR)' and to_cur == 'Indian Rupees (INR)':
            total = amount * 0.62
            output.set(total)
        elif from_cur == 'Nepalese Rupees (NPR)' and to_cur == 'Canadian (CAD)':
            total = amount * 0.011
            output.set(total)
        # Conversion of United States (USD)
        elif from_cur == 'United States (USD)' and to_cur == 'Nepalese Rupees (NPR)':
            total = amount * 120.32
            output.set(total)
        elif from_cur == 'United States (USD)' and to_cur == 'European (EUR)':
            total = amount * 0.90
            output.set(total)
        elif from_cur == 'United States (USD)' and to_cur == 'Indian Rupees (INR)':
            total = amount * 75.07
            output.set(total)
        elif from_cur == 'United States (USD)' and to_cur == 'Canadian (CAD)':
            total = amount * 1.28
            output.set(total)
        # Conversion of European (EUR)
        elif from_cur == 'European (EUR)' and to_cur == 'United States (USD)':
            total = amount * 1.11
            output.set(total)
        elif from_cur == 'European (EUR)' and to_cur == 'Nepalese Rupees (NPR)':
            total = amount * 133.86
            output.set(total)
        elif from_cur == 'European (EUR)' and to_cur == 'Indian Rupees (INR)':
            total = amount * 83.52
            output.set(total)
        elif from_cur == 'European (EUR)' and to_cur == 'Canadian (CAD)':
            total = amount * 1.42
            output.set(total)
        # Conversion of Indian Rupees (INR)
        elif from_cur == 'Indian Rupees (INR)' and to_cur == 'United States (USD)':
            total = amount * 0.013
            output.set(total)
        elif from_cur == 'Indian Rupees (INR)' and to_cur == 'Nepalese Rupees (NPR)':
            total = amount * 1.6
            output.set(total)
        elif from_cur == 'Indian Rupees (INR)' and to_cur == 'European (EUR)':
            total = amount * 0.012
            output.set(total)
        elif from_cur == 'Indian Rupees (INR)' and to_cur == 'Canadian (CAD)':
            total = amount * 0.017
            output.set(total)
        # Conversion of Candian (CAD)
        elif from_cur == 'Canadian (CAD)' and to_cur == 'Nepalese Rupees (NPR)':
            total = amount * 94.21
            output.set(total)
        elif from_cur == 'Canadian (CAD)' and to_cur == 'United States (USD)':
            total = amount * 0.78
            output.set(total)
        elif from_cur == 'Canadian (CAD)' and to_cur == 'European (EUR)':
            total = amount * 0.70
            output.set(total)
        elif from_cur == 'Canadian (CAD)' and to_cur == 'Indian Rupees (INR)':
            total = amount * 58.78
            output.set(total)
        else:
            messagebox.showerror("Invalid Input!!.", "Please try again with valid info.")

    except:
        messagebox.showerror("Invalid amount!!",'Please enter a valid amount.')


Currency_list = ['Currency','Nepalese Rupees (NPR)', 'United States (USD)', 'European (EUR)',
                         'Indian Rupees (INR)', 'Canadian (CAD)']

root.configure(background='Sky blue')
root.geometry('600x300+400+200')
root.title("Currency Converter")
root.iconbitmap('currency.ico')
root.resizable(FALSE,FALSE)

var=StringVar(root)
var.set(Currency_list[0])

variable=ttk.OptionMenu(root,var,*Currency_list)
variable.config()
variable.place(x=50,y=60)

var1=StringVar(root)
var1.set(Currency_list[0])

variable1=ttk.OptionMenu(root,var1,*Currency_list)
variable1.config()
variable1.place(x=50,y=90)


global e1
global output
output=IntVar()

def switch():
    a=from_cur
    to_cur=from_cur
    to_cur=a
Label(root, text="Convert your currency with just few clicks!!.",
      fg='dark blue',
      bg='sky blue',
      font=('times',24)).place(x=0,y=0)
Label(root, text="From:",bg='sky blue').place(x=10,y=60)
Label(root, text="To:",bg='sky blue').place(x=10,y=90)
Label(root, text="Amount:",bg='sky blue').place(x=10,y=130)

Label(root,text="Converted Amount: ",bg='sky blue').place(x=10,y=180)
Label(root,text=' ',textvariable=output,bg='sky blue').place(x=120 ,y=180)
b1=ttk.Button(root,text='Convert',command=CurrencyConversion)
b1.place(x=200,y=130)

e1=ttk.Entry(root)
e1.place(x=65,y=130)



root.mainloop()
