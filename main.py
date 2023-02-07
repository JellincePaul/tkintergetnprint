import tkinter
def showdata():
    mark = mark_entry.get()
    print(mark)


window = tkinter.Tk()




mark_label = tkinter.Label(window, text="Mark")
mark_label.grid(row=0, column=0)
mark_entry = tkinter.Entry(window)
mark_entry.grid(row=1, column=0)
button = tkinter.Button(window, text="Button", command=showdata)
button.grid(row=2, column=0)








window.mainloop()