from tkinter import *
import calendar


def openWindowF():


    enterededTemp = int(enterTemp.get())    
    info = Label(gui, text = "Coneverted Values", bg= "#E28743", font=("times new roman",18,"bold"))
    info.grid(row = 2, column=2, pady=5)

    info = Label(gui, text = f"Entered Celsius value: {enterededTemp}", bg= "#E28743", font=("times new roman",14,))
    info.grid(row = 3, column=2, pady=5)

    convert = (enterededTemp * 1.8) + 32
    convert2 = round(convert,2)

    info = Label(gui, text = f"Coneverted Farenheit value: {convert2}", bg= "#E28743", font=("times new roman",14,))
    info.grid(row = 4, column=2, pady=5)

    # Farenheit =  Celsius * 1.8 + 32.

def openWindowC():


    enterededTemp = int(enterTemp.get())
    info = Label(gui, text = "Coneverted Values", bg= "#E28743", font=("times new roman",14,"bold"))
    info.grid(row = 2, column=2, pady=5)

    info = Label(gui, text = f"Entered Farenheit value: {enterededTemp}", bg= "#E28743", font=("times new roman",14,"bold"))
    info.grid(row = 3, column=2, pady=5)

    convert=(enterededTemp -32) *0.55
    convert2 = round(convert,2)

    info = Label(gui, text = f"Coneverted Celsius value: {convert2}", bg= "#E28743", font=("times new roman",14,"bold"))
    info.grid(row = 4, column=2, pady=5)

    # Celsius = Fahrenheit  - 32 * 0.55.

if __name__ == "__main__":

    gui = Tk()

    gui.geometry("600x300")

    gui.config(background="#E28743")

    gui.title("Calendar")

    cal = Label(gui, text = "Temperature Converter", bg= "#E28743" , font=("times new roman",22,"bold"),)

    cal.grid(row = 1, column=1, padx=147,pady=5, columnspan=2)

    info = Label(gui, text = "Enter a Celsius OR Farenheit value below. ", bg= "#E28743", font=("times new roman",14,))
    info.grid(row = 2, column=1, pady=5)


    enterTemp = Entry(gui, background="#E28743" ) 
    enterTemp.grid(row = 3, column=1, padx=5,pady=10)

    confirm = Button(gui, text = "Calculate into Celsius", bg= "#E28743", font=("times new roman",14, ), command = openWindowC)
    confirm.grid(row=4,column=1,pady=10, )

    confirm = Button(gui, text = "Calculate into Farenheit", bg= "#E28743", font=("times new roman",14, ), command = openWindowF)
    confirm.grid(row=5,column=1,pady=10, )

    exit = Button(gui, text = "Exit", bg= "#E28743", font=("times new roman",14,"bold"), command=exit)
    exit.grid(row=6, column=1, pady=10)

    gui.mainloop()

# e47229





