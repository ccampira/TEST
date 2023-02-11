from tkinter import *
from PIL import Image, ImageTk
import json
import csv
from time import strftime
from customer_classes import *

customer_list=[]
def add_customer():
    page_two.grid_forget()
    add_frame.grid()
    # add_frame.place(relx=.29, rely=.2)
    # add_frame.grid_propagate(False)
    logo_label.place(relx=1, rely=1)


def save_data():
    global cname
    global city
    global state
    global zip
    with open('exnar_customer.csv', 'a', newline='') as fp:
        data = csv.writer(fp)
        data.writerow([cname.get(), city.get(), state.get(), zip.get()])
        # print(f'{cname.get()}, {city.get()}, {state.get()}, {zip.get()}')
    fp.close()
    customer_add = Customer(cname, city, state, zip)
    customer_list.append(customer_add)
    add_frame.grid_forget()
    page_two.grid()
    new_customer = Label(customer_frame, text=f'{cname.get():<50}{city.get():<45}{state.get():<50}{zip.get():>25}',
                        font=('Verdana', 11), bg="white", justify=LEFT, relief=RAISED)
    new_customer.grid()
    cname_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zip_entry.delete(0, END)

def button_click():
    username = user_name.get()
    password = pass_word.get()
    if username in user_accounts:
        if password != user_accounts[username]['Password']:
            results_lbl.config(text=username + ', the password is incorrect')
        else:
            results_lbl.config(text=username + ', the password is correct')
            bg_label.grid_forget()
            box1.grid_forget()
            page_two.grid()
            logo_label.place(relx=1, rely=1)
            welcome_label.grid(row=0, column=0)
            info_label.grid(row=1, column=0)
            today_time()
            with open('exnar_customer.csv') as fp:
                data = csv.reader(fp)
                for row in data:
                    customer_labels = Label(customer_frame, text=f'{row[0]:<50}{row[1]:<45}{row[2]:<50}{row[3]:>25}',
                                        font=('Verdana', 11), bg="white", justify=LEFT, relief=RAISED)
                    customer_labels.grid()

                # for i in customer_list:
                #     customer_list[i] = Customer(row[0],row[1],row[2],row[3])
                #
                # map(print,customer_list)
    else:
        results_lbl.config(text='Username/Password is incorrect')


def close():
    window.destroy()


def today_time():
    time_string = strftime('%H:%M:%S %p \n %x')
    time_label.config(text=time_string)


file_handle = open('users.json')
user_accounts = json.load(file_handle)
file_handle.close()

window = Tk()
window.geometry('1920x1080')  # left number is width, right number is height
window.title('Exnar Digital LLC')
window.config(bg='#30D6FF')  # we are using rgb color
window.resizable(1, 0)

menubar = Menu(window)  # add a menu to window object/instance

filemenu = Menu(menubar)  # add File menu and commands
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save as')
filemenu.add_command(label='Close')
filemenu.add_command(label='Exit', command=window.quit)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff=False)  # if tearoff = false then it will be glued to the menu bar.
# If tearoff = true then it will allow you to move it.
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find...', command=None)
edit.add_command(label='Find again', command=None)

# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)

# Add an icon for windows pc
window.iconbitmap('EXNAR Logo.ico')
window.columnconfigure(0, weight=1)

# background Image
bg_img = Image.open('wallpaper.jpg')
new_width = 1920
new_height = 1080
wallpaper = bg_img.resize((new_width, new_height), Image.ANTIALIAS)
wallpaper.save('wallpaper.jpg')
bg = ImageTk.PhotoImage(wallpaper)
bg_label = Label(window, image=bg)
bg_label.grid(row=0, column=0)


# PAGE 2
page_two = Frame(window, bg='light blue', width=1920, height=1080, borderwidth=2)

# PAGE 3
page_three = Frame(window, bg='light blue', width=1920, height=1080, borderwidth=2)

# ADD CUSTOMER FRAME
add_frame = Frame(window, width=1920, height=1080, borderwidth=2)



#REFRESH PAGE
refresh_page = Frame(window, bg='light blue', width=1920, height=1080, borderwidth=2)



# page_two - Customer LIST
bg2_img = Image.open('wallpaper2.jpg')
new_width2 = 1920
new_height2 = 1080
wallpaper2 = bg2_img.resize((new_width2, new_height2), Image.ANTIALIAS)
wallpaper2.save('wallpaper2.jpg')
bg2 = ImageTk.PhotoImage(wallpaper2)
bg_label2 = Label(page_two, image=bg2)
bg_label2.grid(row=0, column=0)
bg_label2.grid_propagate(False)

customer_frame = Frame(bg_label2, bg='white', width=1920, height=1080, borderwidth=1)
customer_frame.grid(row=3, column=0)

# Welcome Label
welcome_label = Label(bg_label2, text=f'Welcome ccampira.', font=('Impact', 40), bg='white')

info_label = Label(bg_label2, text=f'The list below includes information about all of Exnar Digital LLC '
                                   f'customers.', font=('Verdana', 20), bg='white')

data_label = Label(customer_frame, text=f"{'Company Name':<50}{'City':<45}{'State':<50}{'Zip Code':<30}",
                                   font=('Verdana', 11, 'bold'), bg="white", justify=CENTER)
data_label.grid()



# ADD CUSTOMER PAGE----------------------------------------------------------------------------------------
bg3_img = Image.open('wallpaper3.jpg')
new_width3 = 1920
new_height3 = 1080
wallpaper3 = bg2_img.resize((new_width3, new_height3), Image.ANTIALIAS)
wallpaper3.save('wallpaper3.jpg')
bg3 = ImageTk.PhotoImage(wallpaper3)
bg_label3 = Label(add_frame, image=bg3)
bg_label3.grid(column=0, row=0)
bg_label3.grid_propagate(False)

# refresh_frame = Frame(bg_label3, bg='white', width=1920, height=1080, borderwidth=1)
# refresh_frame.grid(row=3, column=0)

# Configure variables
user_name = StringVar()
user_name.set("Type 'ccampira' for username")
pass_word = StringVar()
pass_word.set("type 'carlos' for password")

# Variables
cname = StringVar()
cname.set('')
city = StringVar()
city.set('')
state = StringVar()
state.set('')
zip = StringVar()
zip.set('')

# LOGO IMAGE
logo = Image.open('EXNAR Logo.png')
new_width = 350
new_height = 200
img = logo.resize((new_width, new_height), Image.ANTIALIAS)
img.save('EXNAR LOGO.png')
logo = ImageTk.PhotoImage(img)
logo_label = Label(window, image=logo)
logo_label.place(relx=.396, rely=.1)

# LOGO IMAGE TWO
logo2 = Image.open('EXNAR Logo.png')
new_width = 350
new_height = 200
img = logo2.resize((new_width, new_height), Image.ANTIALIAS)
img.save('EXNAR LOGO.png')
logo2 = ImageTk.PhotoImage(img)
logo_label2 = Label(bg_label2, image=logo2)
logo_label2.place(relx=.6, rely=.1)

# LOGO IMAGE THREE
logo3 = Image.open('EXNAR Logo.png')
new_width = 350
new_height = 200
img = logo3.resize((new_width, new_height), Image.ANTIALIAS)
img.save('EXNAR LOGO.png')
logo3 = ImageTk.PhotoImage(img)
logo_label3 = Label(bg_label3, image=logo2)
logo_label3.place(relx=.6, rely=.1)

# FRAME WITH USERNAME & PASSWORD
box1 = Frame(window, bg='white', width=310, height=200, borderwidth=2, relief=RAISED)
box1.grid(row=0, columnspan=3)

# LOG IN TO YOUR ACCOUNT MESSAGE
Login_label = Label(box1, text='Login to your Account', width=20, font=('Impact', 20), fg='black')
Login_label.grid(columnspan=2, row=0, column=2)

# label for username and password
username_label = Label(box1, text='Username', fg='black', font=('Impact', 20))
username_label.grid(columnspan=1, row=1, column=2, padx=50, pady=20)
user_password = Label(box1, font=('Impact', 20), text='Password')
user_password.grid(columnspan=1, row=3, column=2, padx=50, pady=20)

# BOX 1, USER & PASSWORD ENTRY BOXES
username_entry = Entry(box1, textvariable=user_name, justify=LEFT, width=30, font=('Verdana', 11))
username_entry.grid(columnspan=1, row=1, column=3, padx=20, pady=20)
password_entry = Entry(box1, textvariable=pass_word, justify=LEFT, width=30, font=('Verdana', 11))
password_entry.grid(columnspan=1, row=3, column=3, padx=20, pady=20)

results_lbl = Label(box1, justify=CENTER, font=('Verdana', 11), bg='white')
results_lbl.grid(columnspan=2, row=4, column=2)

# TIME LABEL
time_label = Label(bg_label2, bg='lightblue', font=('Impact', 15))
time_label.grid(row=0, column=2)



# Submit button
submit_button = Button(bg_label, command=button_click, font=('Impact', 20), text='Log In',
                       relief=GROOVE, bg='black', fg='white')
submit_button.place(relx=.47, rely=.65)


# ADD CUSTOMER PAGE--------------------------------------------------------------------------------------------
cname_label = Label(bg_label3, text='Company Name: ', bg='lightblue', justify=LEFT, width=15, font=("Impact", 40))
cname_label.grid(row=4, column=2, pady=5, padx=5, columnspan=2)
city_label = Label(bg_label3, text='City: ', bg='lightblue', justify=LEFT, width=15, font=("Impact", 40))
city_label.grid(row=5, column=2, pady=5, padx=5, columnspan=2)
cname_entry = Entry(bg_label3, justify=LEFT, width=40, textvariable=cname, font=("Arial", 20))
cname_entry.grid(row=4, column=4, pady=5, padx=5, columnspan=2)
city_entry = Entry(bg_label3, justify=LEFT, width=40, textvariable=city, font=("Arial", 20))
city_entry.grid(row=5, column=4, pady=5, padx=5, columnspan=2)
state_label = Label(bg_label3, text='State: ', bg='lightblue', justify=LEFT, width=15, font=("Impact", 40))
state_label.grid(row=6, column=2, pady=5, padx=5, columnspan=2)
zip_label = Label(bg_label3, text='Zipcode: ', bg='lightblue', justify=LEFT, width=15, font=("Impact", 40))
zip_label.grid(row=7, column=2, pady=5, padx=5, columnspan=2)
state_entry = Entry(bg_label3, justify=LEFT, width=40, textvariable=state, font=("Arial", 20))
state_entry.grid(row=6, column=4, pady=5, padx=5, columnspan=2)
zip_entry = Entry(bg_label3, justify=LEFT, width=40, textvariable=zip, font=("Arial", 20))
zip_entry.grid(row=7, column=4, pady=5, padx=5, columnspan=2)

# Save Customer Button
save_button = Button(bg_label3, text='Save Customer', width=20, font=("Impact", 15), command=save_data)
save_button.grid(columnspan=2, column=3, pady=5, sticky=E)
# -------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------
# BUTTONS

# ACTION BUTTONS FRAME
actions_frame = Frame(bg_label2, bg='white', width=300, height=200, borderwidth=1)
actions_frame.grid(row=8, column=2)

# ADD CUSTOMER BUTTON
add_customer_button = Button(actions_frame, text='Add Customer', font=("Impact", 15), width=15,
                             command=add_customer)
add_customer_button.grid(row=0, column=0)

# EXIT BUTTTON
exit_button = Button(bg_label2, command=close, font=("Impact", 15), text='Exit', width=15)
exit_button.grid(column=2, row=10)
# -------------------------------------------------------------------------------------------------------------------
window.config(menu=menubar)
window.mainloop()  # this displays the GUI


#NOTE:
# I had big expectations for my project, I wanted it to add, and remove, and edit all the customers in the CSV file
# UNfortunately I could not figure out how to remove rows from a csv file or even edit each row of the CSV file
# THE COMMENTED OUT CODE is code that I was planning on using for this problem but I did not have the time to implement
# I plan on finishing my code during the summer to make this program fully funcitonal for EXNAR DIGITAL LLC


# customer_list = []
# Project Functions

# def remove_customer():
#     lines = list()
#     memberName = 'carlos'
#     with open('exnar_customer.csv', 'r') as readFile:
#         customers = csv.reader(readFile)
#         for row in customers:
#             lines.append(row)
#             for field in row:
#                 if field == memberName:
#                     lines.remove(row)
#
#     with open('exnar_customer.csv', 'w') as writeFile:
#         writer = csv.writer(writeFile)
#         writer.writerows(lines)
#
#     with open('exnar_customer.csv') as fp:
#         data = csv.reader(fp)
#         for row in data:
#             customer_labels = Label(refresh_frame, text=f'{row[0]:<50}{row[1]:<45}{row[2]:<50}{row[3]:>25}',
#                                     font=('Verdana', 11), bg="white", justify=LEFT, relief=RAISED)
#             customer_labels.grid()
#
#
# def refresh():
#     page_two.grid_forget()
#     refresh_page.grid()
#     remove_customer()

# #REMOVE BUTTON
# remove_customer_button = Button(actions_frame, text='Remove Customer', font=("Arial", 11), width=15)
# remove_customer_button.grid(row=1, column=0)
# #EDIT BUTTON
# edit_customer_button = Button(actions_frame, text='Edit Customer', font=("Arial", 11), width=15)
# edit_customer_button.grid(row=2, column=0)



