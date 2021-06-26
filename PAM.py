# Modules
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


from tkinter import *
from tkinter import ttk, messagebox, filedialog, font
from os import listdir, remove
from datetime import datetime

# Main window details and labels
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


win = Tk()
win.geometry("800x500")
win.title('MAM')
win.resizable(False, False)
font1 = font.Font(family='Helvetica', size=12, weight='bold', slant='italic')

photo = PhotoImage(file='background.png')
Background_Label = Label(win, image=photo)
Background_Label.place(x=75, y=0, relwidth=1.0, relheight=1.0)

Purple_label = Label(win, text='', bg='purple')
Purple_label.place(x=75, y=350, anchor=CENTER, width=150, height=300)

logo = PhotoImage(file='logo2.png')
logo_Label = Label(win, image=logo, bg='purple')
logo_Label.place(x=75, y=425, anchor=CENTER)

# Daily work window widgets
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Today_Work_Button = Button(win, text='TODAY WORKS', font=font1, command=lambda: Today())
Today_Work_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Past_Days_Button = Button(win, text='OTHER DAYS\nWORKS', font=font1, command=lambda: Past_Days())
Past_Days_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Show_Today_Works_Button = Button(win, text='SHOW & UPDATE', font=font1, command=lambda: Show_Update())
Show_Today_Works_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Write_Daily_Report_Button = Button(win, text='DAILY REPORT', font=font1, command=lambda: Daily_Report())
Write_Daily_Report_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Past_Day_Show_Button = Button(win, text='SHOW OTHER\n DAYS REPORT', font=font1, command=lambda: Other_Report())
Past_Day_Show_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Past_Day_Show_Plan_Button = Button(win, text='SHOW OTHER\n DAYS PLAN', font=font1, command=lambda: Other_Plan())
Past_Day_Show_Plan_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Write_New_Today_Works_Button = Button(win, text='SET PLAN\nFOR A DATE', font=font1, command=lambda: New_Day())
Write_New_Today_Works_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Creat_Today_Works_Button = Button(win, text='SET PLAN', font=font1, command=lambda: Set_Today())
Creat_Today_Works_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Creat_Daily_Report_Button = Button(win, text='END OF DAY', font=font1, command=lambda: End_Of_Day())
Creat_Daily_Report_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Save_Update_Button = Button(win, text='UPDATE', font=font1, command=lambda: Save_Update())
Save_Update_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Write_Daily_Report_Text = Text(win, font=font1)
Write_Daily_Report_Text_yScrollbar = Scrollbar(win, command=Write_Daily_Report_Text.yview)
Write_Daily_Report_Text.config(yscrollcommand=Write_Daily_Report_Text_yScrollbar.set)

Write_New_Today_Works_Text = Text(win, font=font1)
Write_New_Today_Works_Text_yScrollbar = Scrollbar(win, command=Write_New_Today_Works_Text.yview)
Write_New_Today_Works_Text.config(yscrollcommand=Write_New_Today_Works_Text_yScrollbar.set)

Show_Today_Works_Text = Text(win)
Show_Today_Works_Text_yScrollbar = Scrollbar(win, command=Show_Today_Works_Text.yview)
Show_Today_Works_Text.config(yscrollcommand=Show_Today_Works_Text_yScrollbar.set, font=font1)

Show_Past_Day_Text = Text(win)
Show_Past_Day_Text_yScrollbar = Scrollbar(win, command=Show_Past_Day_Text.yview)
Show_Past_Day_Text.config(yscrollcommand=Show_Past_Day_Text_yScrollbar.set, font=font1)

text_entry_day = StringVar()
text_entry_month = StringVar()
text_entry_year = StringVar()

text_entry_day.set("Day")
Days_Entry = Entry(win, font=font1, textvariable=text_entry_day)

text_entry_month.set("Month")
Month_Entry = Entry(win, font=font1, textvariable=text_entry_month)

text_entry_year.set("Year")
Years_Entry = Entry(win, font=font1, textvariable=text_entry_year)

# Project window widgets
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Projects_Path = 'Projects/'
List_Projects_Name_TXT = listdir(Projects_Path)
if 'desktop.ini' in List_Projects_Name_TXT:
    List_Projects_Name_TXT.remove('desktop.ini')

List_Projects_Name = []

for Projects_Names in List_Projects_Name_TXT:
    List_Projects_Name.append(Projects_Names[0: Projects_Names.index('.')])

Combobox_Values = ()

for Value_Project_Names in List_Projects_Name:
    Combobox_Values += Value_Project_Names,

Projects_Names_Combobox = ttk.Combobox(win, values=Combobox_Values, font=font1, state="readonly")
win.option_add('*TCombobox*Listbox.font', font1)

Show_Project_Button = Button(win, text='SHOW', font=font1, command=lambda: Show_Project())
Show_Project_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

New_Project_Button = Button(win, text='NEW', font=font1, command=lambda: New_Project())
New_Project_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Edit_Project_Button = Button(win, text='EDIT', font=font1, command=lambda: Edit_Project())
Edit_Project_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

New_Show_Project_Button = Button(win, text='CHANGE', font=font1, command=lambda: Change_Project())
New_Show_Project_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

New_Edit_Project_Button = Button(win, text='CHANGE', font=font1, command=lambda: Change_Project_2())
New_Edit_Project_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Edit_Save_Project_Button = Button(win, text='SAVE', font=font1, command=lambda: Save_Edit())
Edit_Save_Project_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Finish_Project_Buttons = Button(win, text='FINISH', font=font1, command=lambda: Finish())
Finish_Project_Buttons.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Show_Project_Text = Text(win, font=font1)
Show_Project_Text_yScrollbar = Scrollbar(win, command=Show_Project_Text.yview)
Show_Project_Text.config(yscrollcommand=Show_Project_Text_yScrollbar.set)

Edit_Project_Text = Text(win, font=font1)
Edit_Project_Text_yScrollbar = Scrollbar(win, command=Edit_Project_Text.yview)
Edit_Project_Text.config(yscrollcommand=Edit_Project_Text_yScrollbar.set)

# Main window Buttons
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Project_Button = Button(win, text='PROJECTS', font=font1, command=lambda: PROJECT())
Project_Button.place(x=75, y=150, anchor=CENTER, width=150, height=100)
Project_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')

Daily_Works_Button = Button(win, text='DAILY\nWORKS', font=font1, command=lambda: DAILY_WORKS())
Daily_Works_Button.place(x=75, y=50, anchor=CENTER, width=150, height=100)
Daily_Works_Button.config(background='purple', foreground='white', borderwidth=0, activebackground='pink')


# daily work part
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def DAILY_WORKS():
    Projects_Names_Combobox.place_forget()
    Show_Project_Button.place_forget()
    New_Show_Project_Button.place_forget()
    Finish_Project_Buttons.place_forget()
    New_Project_Button.place_forget()
    Edit_Project_Button.place_forget()
    New_Edit_Project_Button.place_forget()
    Edit_Save_Project_Button.place_forget()
    Show_Project_Text.place_forget()
    Show_Project_Text_yScrollbar.place_forget()
    Edit_Project_Text.place_forget()
    Edit_Project_Text_yScrollbar.place_forget()
    Today_Work_Button.place_forget()
    Past_Days_Button.place_forget()
    Show_Today_Works_Button.place_forget()
    Write_Daily_Report_Button.place_forget()
    Past_Day_Show_Button.place_forget()
    Past_Day_Show_Plan_Button.place_forget()
    Write_New_Today_Works_Button.place_forget()
    Creat_Today_Works_Button.place_forget()
    Creat_Daily_Report_Button.place_forget()
    Save_Update_Button.place_forget()
    Write_Daily_Report_Text.place_forget()
    Write_Daily_Report_Text_yScrollbar.place_forget()
    Write_New_Today_Works_Text.place_forget()
    Write_New_Today_Works_Text_yScrollbar.place_forget()
    Show_Today_Works_Text.place_forget()
    Show_Today_Works_Text_yScrollbar.place_forget()
    Show_Past_Day_Text.place_forget()
    Show_Past_Day_Text_yScrollbar.place_forget()
    Days_Entry.place_forget()
    Month_Entry.place_forget()
    Years_Entry.place_forget()

    Show_Project_Text.delete(0.0, END)
    Edit_Project_Text.delete(0.0, END)
    Show_Past_Day_Text.delete(0.0, END)
    Show_Today_Works_Text.delete(0.0, END)
    Write_New_Today_Works_Text.delete(0.0, END)
    Write_Daily_Report_Text.delete(0.0, END)

    Today_Work_Button.place(x=575, y=475, anchor=CENTER, width=150, height=50)
    Past_Days_Button.place(x=425, y=475, anchor=CENTER, width=150, height=50)
    Write_New_Today_Works_Button.place(x=725, y=475, anchor=CENTER, width=150, height=50)


def Today():
    Today_Work_Button.place_forget()
    Past_Days_Button.place_forget()
    Show_Today_Works_Button.place_forget()
    Write_Daily_Report_Button.place_forget()
    Past_Day_Show_Button.place_forget()
    Past_Day_Show_Plan_Button.place_forget()
    Write_New_Today_Works_Button.place_forget()
    Creat_Today_Works_Button.place_forget()
    Creat_Daily_Report_Button.place_forget()
    Save_Update_Button.place_forget()
    Write_Daily_Report_Text.place_forget()
    Write_Daily_Report_Text_yScrollbar.place_forget()
    Write_New_Today_Works_Text.place_forget()
    Write_New_Today_Works_Text_yScrollbar.place_forget()
    Show_Today_Works_Text.place_forget()
    Show_Today_Works_Text_yScrollbar.place_forget()
    Show_Past_Day_Text.place_forget()
    Show_Past_Day_Text_yScrollbar.place_forget()
    Days_Entry.place_forget()
    Month_Entry.place_forget()
    Years_Entry.place_forget()

    Past_Days_Button.place(x=275, y=475, anchor=CENTER, width=150, height=50)
    Show_Today_Works_Button.place(x=575, y=475, anchor=CENTER, width=150, height=50)
    Write_Daily_Report_Button.place(x=425, y=475, anchor=CENTER, width=150, height=50)
    Write_New_Today_Works_Button.place(x=725, y=475, anchor=CENTER, width=150, height=50)


def Past_Days():
    Today_Work_Button.place_forget()
    Past_Days_Button.place_forget()
    Show_Today_Works_Button.place_forget()
    Write_Daily_Report_Button.place_forget()
    Past_Day_Show_Button.place_forget()
    Past_Day_Show_Plan_Button.place_forget()
    Write_New_Today_Works_Button.place_forget()
    Creat_Today_Works_Button.place_forget()
    Creat_Daily_Report_Button.place_forget()
    Save_Update_Button.place_forget()
    Write_Daily_Report_Text.place_forget()
    Write_Daily_Report_Text_yScrollbar.place_forget()
    Write_New_Today_Works_Text.place_forget()
    Write_New_Today_Works_Text_yScrollbar.place_forget()
    Show_Today_Works_Text.place_forget()
    Show_Today_Works_Text_yScrollbar.place_forget()
    Show_Past_Day_Text.place_forget()
    Show_Past_Day_Text_yScrollbar.place_forget()
    Days_Entry.place_forget()
    Month_Entry.place_forget()
    Years_Entry.place_forget()

    Today_Work_Button.place(x=575, y=475, anchor=CENTER, width=150, height=50)
    Past_Day_Show_Button.place(x=425, y=475, anchor=CENTER, width=150, height=50)
    Past_Day_Show_Plan_Button.place(x=275, y=475, anchor=CENTER, width=150, height=50)
    Write_New_Today_Works_Button.place(x=725, y=475, anchor=CENTER, width=150, height=50)
    Days_Entry.place(x=420, y=25, anchor=CENTER, width=50)
    Month_Entry.place(x=475, y=25, anchor=CENTER, width=50)
    Years_Entry.place(x=530, y=25, anchor=CENTER, width=50)


def Other_Report():
    Show_Past_Day_Text.delete(0.0, END)

    try:
        Daily_Path = 'Daily Works/Report-'
        Day = str(Days_Entry.get())
        Month = str(Month_Entry.get())
        Year = str(Years_Entry.get())
        Today_Work_Name = Daily_Path + Day + "-" + Month + "-" + Year + '.txt'

        with open(Today_Work_Name, 'r') as opened:
            Show_Past_Day_Text.insert(INSERT, opened.read())

        Show_Past_Day_Text.place(x=475, y=225, anchor=CENTER, width=550, height=300)
        Show_Past_Day_Text_yScrollbar.place(x=760, y=225, anchor=CENTER, height=300, width=20)

    except:
        messagebox.showwarning("DATE DON'T FOUND", "YOU DON'T ENTER REPORT ON THIS DATE OR YOUR DON'T ENTER NUMBER")


def Other_Plan():
    Show_Past_Day_Text.delete(0.0, END)

    try:
        Daily_Path = 'Daily Works/'
        Day = str(Days_Entry.get())
        Month = str(Month_Entry.get())
        Year = str(Years_Entry.get())
        Today_Work_Name = Daily_Path + Day + "-" + Month + "-" + Year + '.txt'

        with open(Today_Work_Name, 'r') as opened:
            Show_Past_Day_Text.insert(INSERT, opened.read())

        Show_Past_Day_Text.place(x=475, y=225, anchor=CENTER, width=550, height=300)
        Show_Past_Day_Text_yScrollbar.place(x=760, y=225, anchor=CENTER, height=300, width=20)

    except:
        messagebox.showwarning("DATE DON'T FOUND", "YOU DON'T ENTER REPORT ON THIS DATE OR YOUR DON'T ENTER NUMBER")


def New_Day():
    Creat_Today_Works_Button.place_forget()
    Creat_Daily_Report_Button.place_forget()
    Today_Work_Button.place_forget()
    Past_Days_Button.place_forget()
    Show_Today_Works_Button.place_forget()
    Write_Daily_Report_Button.place_forget()
    Past_Day_Show_Button.place_forget()
    Past_Day_Show_Plan_Button.place_forget()
    Write_New_Today_Works_Button.place_forget()
    Save_Update_Button.place_forget()
    Write_Daily_Report_Text.place_forget()
    Write_Daily_Report_Text_yScrollbar.place_forget()
    Write_New_Today_Works_Text.place_forget()
    Write_New_Today_Works_Text_yScrollbar.place_forget()
    Show_Today_Works_Text.place_forget()
    Show_Today_Works_Text_yScrollbar.place_forget()
    Show_Past_Day_Text.place_forget()
    Show_Past_Day_Text_yScrollbar.place_forget()
    Days_Entry.place_forget()
    Month_Entry.place_forget()
    Years_Entry.place_forget()

    Past_Days_Button.place(x=425, y=475, anchor=CENTER, width=150, height=50)
    Today_Work_Button.place(x=575, y=475, anchor=CENTER, width=150, height=50)
    Write_New_Today_Works_Text.place(x=475, y=225, anchor=CENTER, width=550, height=300)
    Write_New_Today_Works_Text_yScrollbar.place(x=760, y=225, anchor=CENTER, height=300, width=20)
    Creat_Today_Works_Button.place(x=725, y=475, anchor=CENTER, width=150, height=50)
    Days_Entry.place(x=420, y=25, anchor=CENTER, width=50)
    Month_Entry.place(x=475, y=25, anchor=CENTER, width=50)
    Years_Entry.place(x=530, y=25, anchor=CENTER, width=50)


def Set_Today():
    Daily_Path = 'Daily Works/'
    Day = Days_Entry.get()
    Month = Month_Entry.get()
    Year = Years_Entry.get()
    try :

        if type(int(Day)) is int and type(int(Month)) is int and type(int(Year)) is int:
            Today_Work_Name = Daily_Path + str(Day) + "-" + str(Month) + "-" + str(Year) + '.txt'
            Today_Plan = Write_New_Today_Works_Text.get(0.0, END)
            with open(Today_Work_Name, 'w') as fileOpen:
                fileOpen.write(Today_Plan)
                messagebox.showinfo('SUCCESS', 'DAY SETED')
                Write_New_Today_Works_Text.delete(0.0, END)
                Creat_Today_Works_Button.place_forget()
                Write_New_Today_Works_Text.place_forget()
                Days_Entry.place_forget()
                Month_Entry.place_forget()
                Years_Entry.place_forget()
                Write_New_Today_Works_Text_yScrollbar.place_forget()
                Write_New_Today_Works_Button.place(x=725, y=475, anchor=CENTER, width=150, height=50)

        else :
            messagebox.showwarning("WARNING", "YOUR DATE ISN'T A NUMBER ")
    except :
        messagebox.showwarning("WARNING", "YOUR DATE ISN'T A NUMBER ")


def Daily_Report():
    Creat_Today_Works_Button.place_forget()
    Creat_Daily_Report_Button.place_forget()
    Today_Work_Button.place_forget()
    Past_Days_Button.place_forget()
    Past_Day_Show_Plan_Button.place_forget()
    Show_Today_Works_Button.place_forget()
    Write_Daily_Report_Button.place_forget()
    Past_Day_Show_Button.place_forget()
    Write_New_Today_Works_Button.place_forget()
    Save_Update_Button.place_forget()
    Write_Daily_Report_Text.place_forget()
    Write_Daily_Report_Text_yScrollbar.place_forget()
    Write_New_Today_Works_Text.place_forget()
    Write_New_Today_Works_Text_yScrollbar.place_forget()
    Show_Today_Works_Text.place_forget()
    Show_Today_Works_Text_yScrollbar.place_forget()
    Show_Past_Day_Text.place_forget()
    Show_Past_Day_Text_yScrollbar.place_forget()
    Days_Entry.place_forget()
    Month_Entry.place_forget()
    Years_Entry.place_forget()

    Past_Days_Button.place(x=275, y=475, anchor=CENTER, width=150, height=50)
    Show_Today_Works_Button.place(x=425, y=475, anchor=CENTER, width=150, height=50)
    Creat_Daily_Report_Button.place(x=575, y=475, anchor=CENTER, width=150, height=50)
    Write_New_Today_Works_Button.place(x=725, y=475, anchor=CENTER, width=150, height=50)
    Write_Daily_Report_Text.place(x=475, y=225, anchor=CENTER, width=550, height=300)
    Write_Daily_Report_Text_yScrollbar.place(x=760, y=225, anchor=CENTER, height=300, width=20)


def End_Of_Day():
    Daily_Path = 'Daily Works/Report-'
    Today_Date = datetime.now().strftime('%d-%m-%Y')
    Today_Work_Name = Daily_Path + Today_Date + '.txt'
    Today_Plan = Write_Daily_Report_Text.get(0.0, END)
    with open(Today_Work_Name, 'w') as fileOpen:
        fileOpen.write(Today_Plan)
        messagebox.showinfo('SUCCESS', 'GOOD NIGHT')
        Write_Daily_Report_Text.delete(0.0, END)
        Creat_Daily_Report_Button.place_forget()
        Write_Daily_Report_Text.place_forget()
        Write_Daily_Report_Text_yScrollbar.place_forget()
        Write_Daily_Report_Button.place(x=575, y=475, anchor=CENTER, width=150, height=50)


def Show_Update():
    Creat_Today_Works_Button.place_forget()
    Creat_Daily_Report_Button.place_forget()
    Today_Work_Button.place_forget()
    Past_Days_Button.place_forget()
    Show_Today_Works_Button.place_forget()
    Write_Daily_Report_Button.place_forget()
    Past_Day_Show_Button.place_forget()
    Past_Day_Show_Plan_Button.place_forget()
    Write_New_Today_Works_Button.place_forget()
    Save_Update_Button.place_forget()
    Write_Daily_Report_Text.place_forget()
    Write_Daily_Report_Text_yScrollbar.place_forget()
    Write_New_Today_Works_Text.place_forget()
    Write_New_Today_Works_Text_yScrollbar.place_forget()
    Show_Today_Works_Text.place_forget()
    Show_Today_Works_Text_yScrollbar.place_forget()
    Show_Past_Day_Text.place_forget()
    Show_Past_Day_Text_yScrollbar.place_forget()
    Days_Entry.place_forget()
    Month_Entry.place_forget()
    Years_Entry.place_forget()

    try:
        Daily_Path = 'Daily Works/'
        Today_Date = datetime.now().strftime('%d-%m-%Y')
        Today_Work_Name = Daily_Path + Today_Date + '.txt'

        with open(Today_Work_Name, 'r') as opened:
            Show_Today_Works_Text.insert(INSERT, opened.read())

        Show_Today_Works_Text.place(x=475, y=225, anchor=CENTER, width=550, height=300)
        Show_Today_Works_Text_yScrollbar.place(x=760, y=225, anchor=CENTER, height=300, width=20)
        Save_Update_Button.place(x=575, y=475, anchor=CENTER, width=150, height=50)

    except:
        messagebox.showwarning("FILE DON'T FOUND", "YOU DON'T SET A PLAN FOR TODAY")
        Show_Today_Works_Button.place(x=425, y=475, anchor=CENTER, width=150, height=50)

    Past_Days_Button.place(x=275, y=475, anchor=CENTER, width=150, height=50)

    Write_Daily_Report_Button.place(x=425, y=475, anchor=CENTER, width=150, height=50)
    Write_New_Today_Works_Button.place(x=725, y=475, anchor=CENTER, width=150, height=50)


def Save_Update():
    Daily_Path = 'Daily Works/'
    Today_Date = datetime.now().strftime('%d-%m-%Y')
    Today_Work_Name = Daily_Path + Today_Date + '.txt'
    Today_Plan = Show_Today_Works_Text.get(0.0, END)
    with open(Today_Work_Name, 'w') as fileOpen:
        fileOpen.write(Today_Plan)
        Show_Today_Works_Text.delete(0.0, END)
        Show_Today_Works_Text.place_forget()
        Show_Today_Works_Text_yScrollbar.place_forget()
        Save_Update_Button.place_forget()
        Show_Today_Works_Button.place(x=575, y=475, anchor=CENTER, width=150, height=50)

    # project part


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def PROJECT():
    Today_Work_Button.place_forget()
    Past_Days_Button.place_forget()
    Show_Project_Text.place_forget()
    Edit_Project_Text.place_forget()
    Show_Project_Text_yScrollbar.place_forget()
    Edit_Project_Text_yScrollbar.place_forget()
    New_Edit_Project_Button.place_forget()
    New_Show_Project_Button.place_forget()
    Edit_Save_Project_Button.place_forget()
    Finish_Project_Buttons.place_forget()
    Past_Day_Show_Button.place_forget()
    Past_Day_Show_Plan_Button.place_forget()
    Show_Today_Works_Button.place_forget()
    Write_Daily_Report_Button.place_forget()
    Write_New_Today_Works_Button.place_forget()
    Creat_Today_Works_Button.place_forget()
    Creat_Daily_Report_Button.place_forget()
    Past_Days_Button.place_forget()
    Show_Today_Works_Button.place_forget()
    Write_Daily_Report_Button.place_forget()
    Past_Day_Show_Button.place_forget()
    Write_New_Today_Works_Button.place_forget()
    Write_Daily_Report_Text.place_forget()
    Write_Daily_Report_Text_yScrollbar.place_forget()
    Write_New_Today_Works_Text.place_forget()
    Write_New_Today_Works_Text_yScrollbar.place_forget()
    Show_Project_Text.place_forget()
    Show_Project_Text_yScrollbar.place_forget()
    Show_Past_Day_Text.place_forget()
    Show_Past_Day_Text_yScrollbar.place_forget()
    Days_Entry.place_forget()
    Month_Entry.place_forget()
    Years_Entry.place_forget()

    Show_Project_Text.delete(0.0, END)
    Edit_Project_Text.delete(0.0, END)
    Show_Past_Day_Text.delete(0.0, END)
    Show_Today_Works_Text.delete(0.0, END)
    Write_New_Today_Works_Text.delete(0.0, END)
    Write_Daily_Report_Text.delete(0.0, END)

    Projects_Path = 'Projects/'
    List_Projects_Name_TXT = listdir(Projects_Path)
    if 'desktop.ini' in List_Projects_Name_TXT:
        List_Projects_Name_TXT.remove('desktop.ini')

    List_Projects_Name = []

    for Projects_Names in List_Projects_Name_TXT:
        List_Projects_Name.append(Projects_Names[0: Projects_Names.index('.')])

    Combobox_Values = ()

    for Value_Project_Names in List_Projects_Name:
        Combobox_Values += Value_Project_Names,

    Projects_Names_Combobox.config(values=Combobox_Values)
    Projects_Names_Combobox.place(x=475, y=50, width=400, anchor=CENTER)
    Show_Project_Button.place(x=425, y=475, anchor=CENTER, width=150, height=50)
    New_Project_Button.place(x=575, y=475, anchor=CENTER, width=150, height=50)
    Edit_Project_Button.place(x=725, y=475, anchor=CENTER, width=150, height=50)


# _________________________________________________________________________________________ Project Button place

def New_Project():
    Enter_Project = Toplevel(win)  # |
    Enter_Project.title('New Project')  # |
    Enter_Project.geometry('700x600')  # |------> New Project window specification
    Enter_Project.resizable(False, False)  # |
    Enter_Project.config(bg="purple")  # |

    Enter_Project_Name_Label = Label(Enter_Project, text="PROJECT NAME", font=font1)  # |
    Enter_Project_Name_Label.place(x=100, y=30, anchor=CENTER)  # |------> Project name label specification
    Enter_Project_Name_Label.config(bg="purple", fg='white')  # |

    Enter_Project_Name_Entry = Entry(Enter_Project, font=font1)  # |------> Project name entry specification
    Enter_Project_Name_Entry.place(x=250, y=70, anchor=CENTER, width=350)  # |

    Enter_Project_Details_Label = Label(Enter_Project, text='PROJECT DETAILS', font=font1)  # |
    Enter_Project_Details_Label.place(x=110, y=120, anchor=CENTER)  # |------> Project details label specification
    Enter_Project_Details_Label.config(bg="purple", fg='white')  # |

    Enter_Project_Details_Text = Text(Enter_Project)  # |
    Enter_Project_Details_Text.place(x=350, y=300, anchor=CENTER, width=550,
                                     height=300)  # |------> Project details text specification
    Enter_Project_Details_Text.config(font=font1)  # |

    Enter_Project_Details_Text_Scrollbar = Scrollbar(Enter_Project, command=Enter_Project_Details_Text.yview)  # |
    Enter_Project_Details_Text_Scrollbar.place(x=635, y=300, anchor=CENTER, height=300,
                                               width=20)  # |------> Text scrollbar specification
    Enter_Project_Details_Text.config(yscrollcommand=Enter_Project_Details_Text_Scrollbar.set)  # |

    Enter_Project_Create_Button = Button(Enter_Project, text="CREATE", font=font1, command=lambda: CREATE())  # |
    Enter_Project_Create_Button.place(x=575, y=550, anchor=CENTER, width=100)  # |-------> Create Button specification
    Enter_Project_Create_Button.config(activebackground='purple', activeforeground='white')  # |

    # _________________________________________________________________________________________ When Click on CREATE under function runing
    def CREATE():

        Project_Name = Enter_Project_Name_Entry.get()  # this line get project name
        Project_Path = 'Projects/'  # Default project path
        Project_Created = Project_Path + str(Project_Name) + '.txt'
        Project_Details = Enter_Project_Details_Text.get(0.0, END)  # this line get project details

        if Project_Name == "":
            messagebox.showwarning('WARNING !', 'PROJECT NAME IS EMPTY')  # If Project name is empty show error

        else:
            with open(Project_Created, 'w') as fileOpen:  # |
                fileOpen.write(Project_Details)  # |------> Create a txt file for save
                Enter_Project.destroy()  # |
                messagebox.showinfo('SUCCESS', 'PROJECT CREATED')  # |

            Projects_Path = 'Projects/'
            List_Projects_Name_TXT = listdir(Projects_Path)
            if 'desktop.ini' in List_Projects_Name_TXT:
                List_Projects_Name_TXT.remove('desktop.ini')

            List_Projects_Name = []

            for Projects_Names in List_Projects_Name_TXT:
                List_Projects_Name.append(Projects_Names[0: Projects_Names.index('.')])

            Combobox_Values = ()

            for Value_Project_Names in List_Projects_Name:
                Combobox_Values += Value_Project_Names,

            Projects_Names_Combobox.config(values=Combobox_Values)


# _________________________________________________________________________________________

def Show_Project():
    Today_Work_Button.place_forget()
    Past_Days_Button.place_forget()
    Show_Project_Text.place_forget()
    Edit_Project_Text.place_forget()
    Show_Project_Text_yScrollbar.place_forget()
    Edit_Project_Text_yScrollbar.place_forget()
    New_Edit_Project_Button.place_forget()
    New_Show_Project_Button.place_forget()
    Edit_Save_Project_Button.place_forget()
    Finish_Project_Buttons.place_forget()
    Today_Work_Button.place_forget()
    Past_Day_Show_Button.place_forget()
    Past_Days_Button.place_forget()
    Show_Today_Works_Button.place_forget()
    Write_Daily_Report_Button.place_forget()
    Past_Days_Button.place_forget()
    Write_New_Today_Works_Button.place_forget()
    Show_Project_Text.place_forget()
    Edit_Project_Text.place_forget()
    Show_Project_Text_yScrollbar.place_forget()
    Edit_Project_Text_yScrollbar.place_forget()
    New_Edit_Project_Button.place_forget()
    New_Show_Project_Button.place_forget()
    Edit_Save_Project_Button.place_forget()
    Finish_Project_Buttons.place_forget()

    Show_Project_Button.place(x=425, y=475, anchor=CENTER, width=150, height=50)
    Edit_Project_Button.place(x=725, y=475, anchor=CENTER, width=150, height=50)

    Show_Project_Text.delete(0.0, END)
    Edit_Project_Text.delete(0.0, END)

    try:
        Projects_Names_Selected = Projects_Names_Combobox.get()
        Show_File_Selected = Projects_Path + Projects_Names_Selected + '.txt'

        with open(Show_File_Selected, 'r') as opened:
            Show_Project_Text.insert(INSERT, opened.read())

        Show_Project_Text.place(x=475, y=250, anchor=CENTER, width=550, height=300)
        Show_Project_Text_yScrollbar.place(x=760, y=250, anchor=CENTER, height=300, width=20)
        New_Show_Project_Button.place(x=425, y=475, anchor=CENTER, width=150, height=50)
        Finish_Project_Buttons.place(x=275, y=475, anchor=CENTER, width=150, height=50)

        Show_Project_Button.place_forget()
        Show_Project_Text.config(state=DISABLED)

    except:
        messagebox.showwarning("WARNING", "PROJECT NAME IS EMPTY")


def Edit_Project():
    Today_Work_Button.place_forget()
    Past_Days_Button.place_forget()
    Show_Project_Text.place_forget()
    Edit_Project_Text.place_forget()
    Show_Project_Text_yScrollbar.place_forget()
    Edit_Project_Text_yScrollbar.place_forget()
    New_Edit_Project_Button.place_forget()
    New_Show_Project_Button.place_forget()
    Edit_Save_Project_Button.place_forget()
    Finish_Project_Buttons.place_forget()
    Today_Work_Button.place_forget()
    Past_Day_Show_Button.place_forget()
    Past_Days_Button.place_forget()
    Show_Today_Works_Button.place_forget()
    Write_Daily_Report_Button.place_forget()
    Past_Days_Button.place_forget()
    Write_New_Today_Works_Button.place_forget()
    Show_Project_Text.place_forget()
    Edit_Project_Text.place_forget()
    Show_Project_Text_yScrollbar.place_forget()
    Edit_Project_Text_yScrollbar.place_forget()
    New_Edit_Project_Button.place_forget()
    New_Show_Project_Button.place_forget()
    Edit_Save_Project_Button.place_forget()
    Finish_Project_Buttons.place_forget()

    Show_Project_Button.place(x=425, y=475, anchor=CENTER, width=150, height=50)
    Edit_Project_Button.place(x=725, y=475, anchor=CENTER, width=150, height=50)

    Show_Project_Text.delete(0.0, END)
    Edit_Project_Text.delete(0.0, END)

    try:
        Projects_Names_Selected = Projects_Names_Combobox.get()
        Show_File_Selected = Projects_Path + Projects_Names_Selected + '.txt'

        with open(Show_File_Selected, 'r') as opened:
            Edit_Project_Text.insert(INSERT, opened.read())

        Edit_Project_Button.place_forget()

        Edit_Project_Text.place(x=475, y=250, anchor=CENTER, width=550, height=300)
        Edit_Project_Text_yScrollbar.place(x=760, y=250, anchor=CENTER, height=300, width=20)
        New_Edit_Project_Button.place(x=725, y=475, anchor=CENTER, width=150, height=50)
        Edit_Save_Project_Button.place(x=275, y=475, anchor=CENTER, width=150, height=50)

    except:
        messagebox.showwarning("WARNING", "PROJECT NAME IS EMPTY")


def Save_Edit():
    Projects_Names_Selected = Projects_Names_Combobox.get()
    Show_File_Selected = Projects_Path + Projects_Names_Selected + '.txt'

    Edit_Project_Save_Text = Edit_Project_Text.get(0.0, END)

    with open(Show_File_Selected, 'w') as fileOpen:  # |
        fileOpen.write(Edit_Project_Save_Text)  # |------> Create a txt file for save
        messagebox.showinfo('SUCCESS', 'PROJECT UPDAITED')  #
        Edit_Project_Text.delete(0.0, END)

    Edit_Project_Button.place(x=725, y=475, anchor=CENTER, width=150, height=50)

    Edit_Save_Project_Button.place_forget()
    Edit_Project_Text.place_forget()
    Edit_Project_Text_yScrollbar.place_forget()
    New_Edit_Project_Button.place_forget()


def Finish():
    Show_Project_Text.config(state=NORMAL)
    Show_Project_Text.delete(0.0, END)

    Projects_Names_Selected = Projects_Names_Combobox.get()
    Projects_Path = 'Projects/'
    Show_File_Selected = Projects_Path + Projects_Names_Selected + '.txt'

    remove(Show_File_Selected)

    List_Projects_Name_TXT = listdir(Projects_Path)
    if 'desktop.ini' in List_Projects_Name_TXT:
        List_Projects_Name_TXT.remove('desktop.ini')

    List_Projects_Name = []

    for Projects_Names in List_Projects_Name_TXT:
        List_Projects_Name.append(Projects_Names[0: Projects_Names.index('.')])

    Combobox_Values = ()

    for Value_Project_Names in List_Projects_Name:
        Combobox_Values += Value_Project_Names,

    Projects_Names_Combobox.config(values=Combobox_Values)

    messagebox.showinfo('SUCCESS', 'PROJECT FINISHED')

    Show_Project_Button.place(x=425, y=475, anchor=CENTER, width=150, height=50)

    Finish_Project_Buttons.place_forget()
    Show_Project_Text.place_forget()
    Show_Project_Text_yScrollbar.place_forget()
    New_Show_Project_Button.place_forget()


def Change_Project():
    Show_Project_Text.config(state=NORMAL)
    Show_Project_Text.delete(0.0, END)

    Projects_Names_Selected = Projects_Names_Combobox.get()

    Show_File_Selected = Projects_Path + Projects_Names_Selected + '.txt'

    with open(Show_File_Selected, 'r') as opened:
        Show_Project_Text.insert(INSERT, opened.read())

    Show_Project_Text.config(state=DISABLED)


def Change_Project_2():
    Edit_Project_Text.delete(0.0, END)

    Projects_Names_Selected = Projects_Names_Combobox.get()

    Show_File_Selected = Projects_Path + Projects_Names_Selected + '.txt'

    with open(Show_File_Selected, 'r') as opened:
        Edit_Project_Text.insert(INSERT, opened.read())


win.mainloop()