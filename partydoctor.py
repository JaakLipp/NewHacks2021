import tkinter as tk
import test

window = tk.Tk()
window.geometry('800x500')
window['background'] = '#E47B7B'

readable_font = 18
window.title("Party Doctor")
main_frame = tk.Frame(master=window, bg='#E47B7B')
main_frame.bg = '#E47B7B'
yesno_frame = tk.Frame(master=main_frame, bg='#E47B7B')
yesno_frame.bg = '#E47B7B'


def on_campus():
    lb.insert(1, "McMaster University")
    lb.insert(2, "Western University")
    lb.insert(3, "Queens University")
    lb.insert(4, "University of Toronto")
    lb.insert(5, "University of Guelph")
    lb.width=25
    lb.pack()
    yes['state'] = 'disabled'


    confirm = tk.Button(text="select", command=choose_uni, master=main_frame, font=readable_font)
    confirm.pack()

def choose_uni():

    school = ""
    for i in lb.curselection():
        print(lb.get(i))
        school = lb.get(i)
    main_frame.destroy()
    yesno_frame.destroy()
    show_guesses()

    helpme = tk.Label(text="EMERGENCY NUMBER: " + test.get_number(school), bg="#E47B7B", font=20)
    helpme.pack(side=tk.BOTTOM)

def show_guesses():
    guess_label = tk.Label(text="Which one of these is the person most likely suffering from")
    guess_label.pack()
    alc_poi = tk.Button(text='Alcohol Poisoning',master=guess_frame,command=show_response(1),font=readable_font)
    alc_poi.grid(column=1, row=1)
    drug_over = tk.Button(text='Drug Overdose',master=guess_frame,command=show_response(2),font=readable_font)
    drug_over.grid(column=2, row=1)
    choking = tk.Button(text='Choking',master=guess_frame,command=show_response(3),font=readable_font)
    choking.grid(column=3, row=1)
    bleeding = tk.Button(text='Bleeding',master=guess_frame,command=show_response(4),font=readable_font)
    bleeding.grid(column=4, row=1)
    other = tk.Button(text='Other or I do not know',master=guess_frame,command=show_response(5),font=readable_font)
    other.grid(column=5, row=1)


    guess_frame.pack()

def show_response(ID):
    if ID == 1:
        print("do this")
    elif ID == 2:
        print("do this")
    elif ID == 3:
        print("do this")
    elif ID == 4:
        print("do this")
    elif ID == 5:
        print("do this")
    elif ID == 6:
        print("do this")





welcome = tk.Label(
    text="Welcome to Party Doctor",
    master=main_frame,
    bg="#E47B7B",
    font=('Helvetica', 40, 'bold')
)
welcome.pack()

campus_question = tk.Label(
    text="Are you on campus currently?",
    master=main_frame,
    bg="#E47B7B",
    font=('Helvetica', 20)
)
campus_question.pack()


lb = tk.Listbox(master=main_frame)

yes = tk.Button(master=yesno_frame, text="Yes", command=on_campus, font=readable_font, width=15)
yes.grid(column=1, row=1)
no = tk.Button(master=yesno_frame, text="No", font=readable_font, width=15)
no.grid(column=2, row=1)
main_frame.pack()
yesno_frame.pack()
guess_frame = tk.Frame(master=window)
responses = []





window.mainloop()
