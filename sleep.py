import tkinter as tk
from datetime import datetime
import os
import matplotlib.pyplot as plt
import pandas as pd

#--functions--
def create_account():
  global age
    #create_account_page
  create_account_page.place(relx = 0.5, rely = 0.5, anchor = "center")
  root.wm_geometry("210x270")
  
      #Labels
  lbl_create_account_page = tk.Label(create_account_page, text = "Create Account", font = ("TkFixedFont", 13, "bold"))
  lbl_create_account_message = tk.Label(create_account_page, text = "Enter the following information", font = ("TkFixedFont", 9, "italic"))
  lbl_username = tk.Label(create_account_page, text = "Username:")
  lbl_password = tk.Label(create_account_page, text = "Password:")
  lbl_password_confirmation = tk.Label(create_account_page, text = "Confirm Password:")
  lbl_age = tk.Label(create_account_page, text = "Age:")
  
      #Entries
  ent_username = tk.Entry(create_account_page, bd = 3)
  ent_password = tk.Entry(create_account_page, bd = 3, show = "*")
  ent_confirm_password = tk.Entry(create_account_page, bd = 3, show = "*")
  ent_age = tk.Entry(create_account_page, bd = 3)
  
      #Buttons
  btn_create_account = tk.Button(create_account_page, text = "Create Account", bd = 3, command = lambda: information_validation("create account", ent_username.get(), ent_password.get(), ent_confirm_password.get(), lbl_create_account_message, ent_age.get()))
  
      #Pack
  lbl_create_account_page.pack()
  lbl_create_account_message.pack(pady = 5)
  lbl_username.pack()
  ent_username.pack()
  lbl_password.pack()
  ent_password.pack()
  lbl_password_confirmation.pack()
  ent_confirm_password.pack()
  lbl_age.pack()
  ent_age.pack()
  btn_create_account.pack(pady = 4)

def information_validation(option, usernm, passwd, password_confirmation, config_message, age = 0):
  global file_name, username, password
  username = usernm
  password = passwd
  file_name = username + password + ".txt"
  if option == "create account":
    try:
      age_used = int(age)
      csv_file = username + password + "_" + str(age_used) + ".csv"
    except ValueError:
      config_message.config(text = "Invalid Entry - Please try again", fg = "red")
      print("b")
      return
    try:
      creating_account = open(file_name, "r")
    except FileNotFoundError:
      if (password == password_confirmation) and (password != "") and (username != "") and not("," in username) and not("," in password):
        creating_account = open(file_name, "w")
        create_csv_file = open(csv_file, "w")
        create_csv_file.write("day,decimal_time\n")
        with open("user_and_age.txt", "a") as user_and_age:
          user_and_age.write(username + password + "," + str(age_used) + "\n")
          #account_created_page
        account_created_page.place(relx = 0.5, rely = 0.5, anchor = "center")
        account_created_page.tkraise()
        root.wm_geometry("200x120")
        options.destroy()
        create_account_page.destroy()
        
            #Labels
        lbl_account_created_page = tk.Label(account_created_page, text = "Account Created!", font = ("TkFixedFont", 13, "bold"))
        lbl_username_and_password_display = tk.Label(account_created_page, text = "Username: " + str(username) + "\nPassword: " + str(password), font = ("TkFixedFont", 11))
  
            #Buttons
        btn_signin = tk.Button(account_created_page, text = "Sign In", bd = 3, command = signin)
  
            #Packs
        lbl_account_created_page.pack()
        lbl_username_and_password_display.pack(pady = 4)
        btn_signin.pack()
      else:
        config_message.config(text = "Invalid Entry - Please try again", fg = "red")
    else:
      config_message.config(text = "Invalid Entry - Please try again", fg = "red")
  elif option == "signin":
    try:
      signin_check = open(file_name, "r")
      start_and_end_sleep(file_name)
    except FileNotFoundError:
      config_message.config(text = "Unsuccessful login\nPlease try again", fg = "red")
      config_message.pack(pady = 1)
      
def signin():
    #signin_page
  signin_page.place(relx = 0.5, rely = 0.5, anchor = "center")
  root.wm_geometry("210x190")
  signin_page.tkraise()

      #Labels
  lbl_signin_page = tk.Label(signin_page, text = "Sign In", font = ("TkFixedFont", 13, "bold"))
  lbl_signin_message = tk.Label(signin_page, text = "Enter the following information", font = ("TkFixedFont", 9, "italic"))
  lbl_username = tk.Label(signin_page, text = "Username:")
  lbl_password = tk.Label(signin_page, text = "Password:")
  
      #Entries
  ent_username = tk.Entry(signin_page, bd = 3)
  ent_password = tk.Entry(signin_page, bd = 3, show = "*")

      #Buttons
  btn_signin = tk.Button(signin_page, text = "Sign In", bd = 3, command = lambda: information_validation("signin", ent_username.get(), ent_password.get(), "none", lbl_signin_message))

      #Pack
  lbl_signin_page.pack()
  lbl_signin_message.pack(pady = 5)
  lbl_username.pack()
  ent_username.pack()
  lbl_password.pack()
  ent_password.pack()
  btn_signin.pack(pady = 4)

def start_and_end_sleep(file_name, option = 1):
  global btn_other_and_original_options, label_different_options_page, btn_option, btn_option_2, start_and_end_sleep_page, username
    #start_and_end_sleep_page
  start_and_end_sleep_page = tk.Frame(root)
  start_and_end_sleep_page.place(relx = 0.5, rely = 0.5, anchor = "center")
  root.wm_geometry("350x170")
  if option == 1:
    options.destroy()
    create_account_page.destroy()
    signin_page.destroy()
    account_created_page.destroy()
  
      #Labels
  lbl_start_and_end_sleep_page = tk.Label(start_and_end_sleep_page, text = "Welcome " + str(username) + "!", font = ("TkFixedFont", 13, "bold"))
  label_different_options_page = tk.Label(start_and_end_sleep_page, text = "Choose an option:\n1. \"Start Sleep\" to record the time you went to bed\n2. \"End Sleep\" to record the time you woke up\n* \"Options 3-4\" to choose from more options", font = ("TkFixedFont", 9, "italic"))

      #Buttons
  btn_option = tk.Button(start_and_end_sleep_page, text = "Start Sleep", bd = 3, command = lambda: start_sleep(file_name))
  btn_option_2 = tk.Button(start_and_end_sleep_page, text = " End Sleep " , bd = 3, command = lambda: end_sleep(file_name, label_different_options_page))
  btn_other_and_original_options = tk.Button(start_and_end_sleep_page, text = "Options 3-4", bd = 3, command = lambda: other_option_screen(username, 1))
  # btn_graph = tk.Button(start_and_end_sleep_page, text = "Graph Data", bd = 3, command = lambda: graph_data(csv_file))

      #Pack
  lbl_start_and_end_sleep_page.pack()
  label_different_options_page.pack()
  btn_option.pack(side = "left")
  btn_other_and_original_options.pack(side = "right")
  btn_option_2.pack()

def other_option_screen(option):
  global btn_other_and_original_options, label_different_options_page, btn_option, btn_option_2, file_name
  if option == 1:
    label_different_options_page.config(text = "Choose an option:\n3. \"Graph Data\" to visualize your sleep data history\n(Warning: this option will sign you out)\n4. \"Get Advice\" to get valid information for\nimproving your sleep\n* \"Options 1-2\" to choose from more options")
    btn_option.config(text = "Graph Data", command = lambda: graph_data())
    btn_option_2.config(text = "Get Advice", command = lambda: get_advice())
    btn_other_and_original_options.config(text = "Options 1-2", command = lambda: other_option_screen(2))
  if option == 2:
    label_different_options_page.config(text = "Choose an option:\n1. \"Start Sleep\" to record the time you went to bed\n2. \"End Sleep\" to record the time you woke up\n* \"Options 3-4\" to choose from more options")
    btn_option.config(text = "Start Sleep", command = lambda: start_sleep(file_name))
    btn_option_2.config(text = "End Sleep", command = lambda: end_sleep(file_name, label_different_options_page))
    btn_other_and_original_options.config(text = "Options 3-4", command = lambda: other_option_screen(1))

def start_sleep(file_name):
  with open(file_name, "w") as old_time:
    now = datetime.now()
    list_of_time_data = [now.year, now.month, now.day, now.hour, now.minute, now.second]
    for time_data in list_of_time_data:
      old_time.write(str(time_data) + "\n")
      
def end_sleep(file_name, label_different_options_page):
  global start_and_end_sleep_page, username, password
  try:
    with open(file_name, "r") as old_time:
      list_of_old_data = []
      for time in old_time:
        list_of_old_data.append(int(time[:-1]))
      old_data = datetime(list_of_old_data[0], list_of_old_data[1], list_of_old_data[2], list_of_old_data[3], list_of_old_data[4], list_of_old_data[5])
      current_time = datetime.now()
      time_difference = current_time - old_data
      print("You slept for " + str(time_difference))
      place_holder = ""
      which = 1
      for character in str(time_difference):
        if character != ":":
          place_holder += character
        else:
          if which == 1:
            hour = int(place_holder)
          elif which == 2:
            minute = int(place_holder)
          which += 1
          place_holder = ""
      second = float(place_holder)
      
    with open(csv_file, "r") as all_time:
      list_of_all_time = []
      for time in all_time:
        list_of_all_time.append(time)
    with open(csv_file, "a") as update_csv:
      decimal_time = ((hour * 3600) + (minute * 60) + (second))/3600
      update_csv.write(str(len(list_of_all_time)) + "," + str(decimal_time) + "\n")
    label_different_options_page.config(text = "Choose an option:\n1. \"Start Sleep\" to record the time you went to bed\n2. \"End Sleep\" to record the time you woke up\n* \"Options 3-4\" to choose from more options\nYou slept for: " + str(decimal_time) + " hours", font = ("TkFixedFont", 9))
  except IndexError:
    place_holder = 0
def graph_data():
  global username, password
  with open("user_and_age.txt", "r") as user_and_age:
    file_reference = username + password
    for username_and_password in user_and_age:
      index = username_and_password.index(",")
      if file_reference == username_and_password[:index]:
        csv_file = file_reference + "_" + str(username_and_password[index+1:])
      character += username_and_password
  #read file
  time_data = pd.read_csv(csv_file, header = 0)

  #plot
  plt.plot(time_data['day'], time_data['decimal_time'], color='gray')
  plt.ylabel('Hours')
  plt.xlabel('Days')
  plt.title(username + "\'s Sleep Pattern Change Over Time")
  plt.show()

def get_advice():
  decimal_time = pd.read_csv(csv_file, header = 0)['decimal_time']
  total = 0
  for time in decimal_time:
    total += time
  average_sleep_time = total / len(decimal_time)
  print(average_sleep_time)

# main window
root = tk.Tk()
root.wm_geometry("210x70")

# main window title
tk_title = root.title()
root.title("Sleep Deprivation Defeater")

#Frames
options = tk.Frame(root)
create_account_page = tk.Frame(root)
account_created_page = tk.Frame(root)
signin_page = tk.Frame(root)

  #option frame
options.place(relx = 0.5, rely = 0.5, anchor = "center")

    #label
lbl_which_option = tk.Label(options, text = "Choose an option:")

    #button
btn_create_account = tk.Button(options, text = "Sign Up", bd = 3, command = create_account)
btn_signin = tk.Button(options, text = "Sign In", bd = 3, command = signin)

    #pack
lbl_which_option.pack(pady = 2)
btn_create_account.pack(padx = 3, side = "left")
btn_signin.pack(padx = 3, side = "right")

root.mainloop()