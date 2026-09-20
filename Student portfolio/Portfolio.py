from tkinter import *
window = Tk()
window.geometry("900x800")
window.config(bg='white')
window.title("Student Portfolio")
window.resizable(width=FALSE, height=FALSE)

title = Label(window, text="STUDENT PORTFOLIO", font=("Cosmic sans", 20, "bold"), bg="white", fg="black")
title.pack(pady=20)

profileFrame = Frame(window, bg='white')
profileFrame.pack(padx=20, pady=10, fill='x')

picture = PhotoImage(file="picture.gif")
picture = picture.subsample(15, 15)
canvas = Canvas(profileFrame, width=150, height=150, bg='white', highlightthickness=0)
canvas.pack(side="left", padx=15, pady=15)
canvas.create_image(75, 75, image=picture)
canvas.image = picture 

infoFrame = Frame(profileFrame, bg='white')
infoFrame.pack(side="left", padx=20, pady=15, fill="both", expand=True)

info_list = [
    ("Full Name:", "Justin Lee C. Bernardo"),
    ("Age:", "19 years old"),
    ("Gender:", "Male"),
    ("Course:", "Information Technology"),
    ("College:", "College of Computer Studies"),
    ("Contact:", "justinleecabanero.bernardo@my.smciligan.edu.ph"),
    ("Hobbies:", "Gaming, Reading manhwas, Watching animes"),
    ("Interests:", "AI, Programming, ")
]

for label_text, value_text in info_list:
    row = Frame(infoFrame, bg='white')
    row.pack(fill="x", pady=2)
    
    label = Label(row, text=label_text, font=("Arial", 10, "bold"), bg='white', fg='#666', width=12, anchor="w")
    label.pack(side="left")
    
    value = Label(row, text=value_text, font=("Arial", 10), bg='white', fg='black')
    value.pack(side="left", fill="x", expand=True)

about_frame = Frame(window, bg='white')
about_frame.pack(padx=20, pady=10, fill="both")

aboutTitle = Label(about_frame, text="About me: ", bg='white', font=("Cosmic sans", 15))
aboutTitle.pack(padx=10, pady=(10, 5), anchor= W)

about_text = Label(about_frame, text="I'm a Information Technology student who loves to learn more about programming, AI web development etc. When I'm not tackling complex coding problems or exploring new tech, you'll usually find me gaming or catching up on my favorite manhwas.", 
                   font=("Arial", 11), 
                   bg='white', fg='#666', 
                   wraplength=750, 
                   justify="left")
about_text.pack(anchor="w", padx=10, pady=(0, 10))

hobbies_frame = Frame(window, bg='white')
hobbies_frame.pack(padx=20, pady=10, fill="both")


hobbies_title = Label(hobbies_frame, text="My Hobbies & Interests", font=("Arial", 11, "bold"), bg='white', fg='#333')
hobbies_title.pack(anchor="w", padx=10, pady=(10, 15))


cards_frame = Frame(hobbies_frame, bg='white')
cards_frame.pack(fill="x", padx=10, pady=(0, 10))


card = Frame(cards_frame, highlightthickness=2,)
card.pack(side="left", padx=5, pady=5, fill="both", expand=True)

image_frame = Frame(card, bg='white', height=100)
image_frame.pack(fill="both", expand=True)

windbreaker = PhotoImage(file="windbreaker.gif")
windbreaker = windbreaker.subsample(4, 5)
canvas = Canvas(image_frame, width=150, height=150, bg='white', highlightthickness=0)
canvas.pack(side="left", padx=27, pady=15)
canvas.create_image(75, 75, image=windbreaker)
canvas.image = windbreaker


guitar = PhotoImage(file="guitar.gif")
guitar = guitar.subsample(4, 3)
canvas = Canvas(image_frame, width=150, height=150, bg='white', highlightthickness=0)
canvas.pack(side="left", padx=27, pady=15)
canvas.create_image(75, 75, image=guitar)
canvas.image = guitar

gaming = PhotoImage(file="gaming.gif")
gaming = gaming.subsample(4, 3)
canvas = Canvas(image_frame, width=150, height=150, bg='white', highlightthickness=0)
canvas.pack(side="left", padx=27, pady=15)
canvas.create_image(75, 75, image=gaming)
canvas.image = gaming


gym = PhotoImage(file="gym.gif")
gym = gym.subsample(4, 3)
canvas = Canvas(image_frame, width=150, height=150, bg='white', highlightthickness=0)
canvas.pack(side="left", padx=27, pady=15)
canvas.create_image(75, 75, image=gym)
canvas.image = gym


text_frame = Frame(card, height=50)
text_frame.pack(fill="x")
hobbies_text = Label(text_frame, text="Reading Manhwas", font=("Arial", 12, "bold"))
hobbies_text.pack(side="left", padx=20, pady=15)

hobbies_text = Label(text_frame, text="Playing Guitar", font=("Arial", 12, "bold"))
hobbies_text.pack(side="left", padx=56, pady=15)

hobbies_text = Label(text_frame, text="Playing Games", font=("Arial", 12, "bold"))
hobbies_text.pack(side="left", padx=27, pady=15)

hobbies_text = Label(text_frame, text="Going to the Gym", font=("Arial", 12, "bold"))
hobbies_text.pack(side="left", padx=54, pady=15)
window.mainloop()