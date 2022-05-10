import tkinter as tk
from datetime import datetime
import os
import json

with open("names.json") as json_file:
    names = json.load(json_file)

# --functions--
def create_account():
    # create_account_page
    create_account_page.place(relx=0.5, rely=0.5, anchor="center")
    root.wm_geometry("350x250")

    # Labels
    lbl_create_account_page = tk.Label(create_account_page, text="Create Account", font=("TkFixedFont", 13, "bold"))
    lbl_create_account_message = tk.Label(create_account_page, text="Enter the following information",
                                          font=("TkFixedFont", 9, "italic"))
    global lbl_username
    lbl_username = tk.Label(create_account_page, text="Username:")
    lbl_password = tk.Label(create_account_page, text="Password:")
    lbl_password_confirmation = tk.Label(create_account_page, text="Confirm Password")

    # Entries
    ent_username = tk.Entry(create_account_page, bd=3)
    ent_password = tk.Entry(create_account_page, bd=3, show="*")
    ent_confirm_password = tk.Entry(create_account_page, bd=3, show="*")

    # Buttons
    btn_create_account = tk.Button(create_account_page, text="Create Account", bd=3,
                                   command=lambda: information_validation("create account", ent_username.get(),
                                                                          ent_password.get(),
                                                                          ent_confirm_password.get(),
                                                                          lbl_create_account_message))

    # Pack
    lbl_create_account_page.pack()
    lbl_create_account_message.pack(pady=5)
    lbl_username.pack()
    ent_username.pack()
    lbl_password.pack()
    ent_password.pack()
    lbl_password_confirmation.pack()
    ent_confirm_password.pack()
    btn_create_account.pack(pady=4)


def information_validation(option, username, password, password_confirmation, config_message):
    used_user = False
    logged_in = False
    for i in names:
        print(i)
        print(i['Username'])
        if username == i['Username']:
            used_user = True
            print('ok')

    if option == "create account":
        if (password == password_confirmation) and (password != "") and used_user == False:
            names.append({"Username": username, "Password": password, 'Sleep' : {}})
            config_message.config(text="")
            with open('names.json', 'w') as json_file:
                json.dump(names, json_file, indent=4, separators=(',', ':'))
        elif used_user:
            config_message.config(text="That username is already in use - Please try again", fg="red")
        else:
            config_message.config(text="Invalid Entry - Please try again", fg="red")
    elif option == "signin":
        for i in names:
            if username == i['Username'] and password in i["Password"]:
                logged_in = True
                file_name = 'test'
                start_and_end_sleep(username, file_name)
        if not logged_in:
            config_message.config(text="Unsuccessful login\nPlease try again", fg="red")
            config_message.pack(pady=1)


def signin():
    # signin_page
    signin_page.place(relx=0.5, rely=0.5, anchor="center")
    root.wm_geometry("350x250")

    # Labels
    lbl_signin_page = tk.Label(signin_page, text="Sign In", font=("TkFixedFont", 13, "bold"))
    lbl_signin_message = tk.Label(signin_page, text="Enter the following information",
                                  font=("TkFixedFont", 9, "italic"))
    lbl_username = tk.Label(signin_page, text="Username:")
    lbl_password = tk.Label(signin_page, text="Password:")

    # Entries
    ent_username = tk.Entry(signin_page, bd=3)
    ent_password = tk.Entry(signin_page, bd=3, show="*")

    # Buttons
    btn_signin = tk.Button(signin_page, text="Sign In", bd=3,
                           command=lambda: information_validation("signin", ent_username.get(), ent_password.get(),
                                                                  "none", lbl_signin_message))

    # Pack
    lbl_signin_page.pack()
    lbl_signin_message.pack(pady=5)
    lbl_username.pack()
    ent_username.pack()
    lbl_password.pack()
    ent_password.pack()
    btn_signin.pack(pady=4)


def start_and_end_sleep(username, file_name):
    # start_and_end_sleep_page
    start_and_end_sleep_page.place(relx=0.5, rely=0.5, anchor="center")
    root.wm_geometry("350x250")
    options.destroy()
    create_account_page.destroy()
    signin_page.destroy()

    # Labels
    lbl_start_and_end_sleep_page = tk.Label(start_and_end_sleep_page, text="Welcome " + str(username) + "!",
                                            font=("TkFixedFont", 13, "bold"))
    lbl_start_and_end_sleep_message = tk.Label(start_and_end_sleep_page,
                                               text="Choose an option:\n1. \"Start Sleep\" if going to bed\n"
                                                    "2. \"End Sleep\" if woke up",
                                               font=("TkFixedFont", 9, "italic"))

    # Buttons
    btn_start_sleep = tk.Button(start_and_end_sleep_page, text="Start Sleep", bd=3,
                                command=lambda: start_sleep(file_name))
    btn_end_sleep = tk.Button(start_and_end_sleep_page, text=" End Sleep ", bd=3, command=lambda: end_sleep(file_name))

    # Pack
    lbl_start_and_end_sleep_page.pack()
    lbl_start_and_end_sleep_message.pack(pady=4)
    btn_start_sleep.pack(side="left")
    btn_end_sleep.pack(side="right")


def start_sleep(file_name):
    with open(file_name, "r+") as old_time:
        now = datetime.now()
        list_of_time_data = [now.year, now.month, now.day, now.hour, now.minute, now.second]
    os.remove(file_name)
    with open(file_name, "w") as time_update:
        for data in list_of_time_data:
            time_update.write(str(data) + ("\n"))


def end_sleep(file_name):
    with open(file_name, "r") as old_time:
        list_of_old_data = []
        for time in old_time:
            list_of_old_data.append(int(time[:-1]))
        old_data = datetime(list_of_old_data[0], list_of_old_data[1], list_of_old_data[2], list_of_old_data[3],
                            list_of_old_data[4], list_of_old_data[5])
        current_time = datetime.now()
        time_difference = current_time - old_data
        print("You slept for " + str(time_difference))


# main window
root = tk.Tk()
root.wm_geometry("350x250")

# main window title
tk_title = root.title()
root.title("Sleep Deprivation Defeater")

# Frames
options = tk.Frame(root)
create_account_page = tk.Frame(root)
signin_page = tk.Frame(root)
start_and_end_sleep_page = tk.Frame(root)

# option frame
options.place(relx=0.5, rely=0.5, anchor="center")

# label
lbl_which_option = tk.Label(options, text="Choose an option:")

# button
btn_create_account = tk.Button(options, text="Sign Up", bd=3, command=create_account)
btn_signin = tk.Button(options, text="Sign In", bd=3, command=signin)

# pack
lbl_which_option.pack(pady=2)
btn_create_account.pack(padx=3, side="left")
btn_signin.pack(padx=3, side="right")

root.mainloop()