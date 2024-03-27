import customtkinter as ctk



calculater = ctk.CTk()
calculater.geometry("340x430")
calculater.title("Calculator")
calculater.resizable(False,False)


ctk.set_default_color_theme("Resources/yellow.json")
ctk.set_appearance_mode("dark")

mode = "dark"


def change_theme():
  global mode
  if mode == "dark":
    ctk.set_appearance_mode("light")
    mode = "light"
    theme_button.configure(text="Light Mode")
  elif mode == "light":
    ctk.set_appearance_mode("dark")
    mode = "dark"
    theme_button.configure(text="Dark Mode")


theme_button = ctk.CTkSwitch(calculater, text="Dark Mode", command=change_theme)


theme_button.place(x=220, y=370)

expression=""

def btn_press(item):
  global expression
  
  expression = expression + str(item)
  
  input_text.set(expression)
  
def equalpress():
  try:
    global expression
    total = str(eval(expression))
    input_text.set(total)
    expression = ""
  except:
    input_text.set("Error")
    expression = ""
      

def backspace():
    current = input_text.get()
    lenght = len(current)-1
    input_text.delete(lenght, END)
  



def clear(): 

    global expression 

    expression = "" 

    input_text.set("") 








input_text = ctk.StringVar()


one_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                              text="1",
                              command=lambda: btn_press(1)
                             )
two_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text="2",
                        command=lambda: btn_press(2)
                             )
three_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text="3",
                          command=lambda: btn_press(3)
                             )
four_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text="4",
                         command=lambda: btn_press(4)
                             )
five_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text="5",
                               command=lambda: btn_press(5)
                             )
six_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text="6",
                              command=lambda: btn_press(6)
                             )
seven_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text="7",
                                command=lambda: btn_press(7)
                             )
eight_btn = ctk.CTkButton(master=calculater,
                           height=60,
                             width=40,
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text="8",
                                command=lambda: btn_press(8)
                             )
nine_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text="9",
                               command=lambda: btn_press(9)      
                             )
zero_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text="0",
                               command=lambda: btn_press(0)
                             )
dot_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=75,
                             
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text=".",
                              command=lambda: btn_press('.')
                             )
                             
plus_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             text_color	="black",
                             fg_color = "red",
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text="+",
                               command=lambda: btn_press('+')
                             )
minus_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=77,
                             text_color	="black",
                             fg_color = "red",
                             font=(
                                "Ariel",
                                32,"bold"),
                             corner_radius=100000,
                             text="-",

                                command=lambda: btn_press('-')
                             )
division_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             text_color	="black",
                             fg_color = "red",
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text="/",
                                   command=lambda: btn_press('/')
                             )
multiply_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             text_color	="black",
                             fg_color = "red",
                             font=(
                                "Helvetica",
                                25,"bold"),
                             corner_radius=100000,
                             text="×",
                                   command=lambda: btn_press('*')
                             )
equal_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             text_color	="black",
                             fg_color = "red",
                             font=(
                                "Helvetica",
                                22,"bold"),
                             corner_radius=100000,
                             text="=",
                          command=equalpress
                             )
clear_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=40,
                             text_color	="black",
                             fg_color = "red",
                             font=(
                                "Helvetica",
                                25,"bold"),

corner_radius=100000,
                            
                             text="C",
                             command=lambda: clear()
                         )
delete_btn = ctk.CTkButton(master=calculater,
                             height=60,
                             width=20,
                             text_color	="black",
                             fg_color = "red",
                             font=(
                                "Helvetica",
                                25,"bold"),
                            corner_radius=100000,
                             text="←",
                                 command=lambda: backspace()
                             )
                             
one_btn.place(x=15,y=90)
two_btn.place(x=95,y=90)
three_btn.place(x=175,y=90)
plus_btn.place(x=255,y=90)
four_btn.place(x=15,y=160)
five_btn.place(x=95,y=160)
six_btn.place(x=175,y=160)
minus_btn.place(x=255,y=160)
seven_btn.place(x=15,y=230)
eight_btn.place(x=95,y=230)
nine_btn.place(x=175,y=230)
division_btn.place(x=255,y=230)
zero_btn.place(x=15,y=300)
dot_btn.place(x=95,y=300)



multiply_btn.place(x=175,y=300)
equal_btn.place(x=255,y=300)

clear_btn.place(x=15,y=370)
delete_btn.place(x=95,y=370)


input_frame = ctk.CTkFrame(calculater, width=320, height=70, border_width=0,)


input_frame.place(x=10,y=10)


input_field = ctk.CTkEntry(master=input_frame, width=320, height=70, textvariable=input_text ,border_width=2, font=(
                                "Helvetica",
                                25,"bold"),text_color="black",)



input_field.pack(side="left")

input_field.configure(textvariable=input_text)
                           

calculater.mainloop()
