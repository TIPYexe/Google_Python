import tkinter as tk
from PIL import ImageTk, Image
import web_scrapper as cs_scrp
import Case_Skins as cls

def updateDisplay(myString):
    displayVar.set(displayVar.get() + '\n' + myString)

def log_viewer(event, p):
    displayLab.after(1000, updateDisplay(p))

def extract_skins(event):
    Cases = cs_scrp.extract_from_cases('https://csgostash.com/containers/skin-cases', displayVar)

def printCases(event):
    for case in Cases:
        for skin in case.Skins:
            print(case.name, skin.name, skin.weapon)

skin_names_file = 'Files/test4.txt'
skin_prices_file = 'Files/test5.txt'

window = tk.Tk()
window.title("CS:GO Trade-up Scrapper")

path_logo = 'Files/logo.png'

# Pregatesc variabile pentru textul din cele mai de sus butoane din meniu
# pentru ca vreau sa il pot schimba atunci cand operatia este finalizata
btn_load_names_txt = tk.StringVar()
btn_prices_txt = tk.StringVar()

frame1 = tk.Frame(master=window, height=300, bg='black')
frame1.pack(fill=tk.X, side=tk.TOP)

frame2 = tk.Frame(master=window, height=200, bg='white')
frame2.pack(fill=tk.Y, side=tk.LEFT)

image = Image.open(path_logo)
image = image.resize((300, 197))
logo = ImageTk.PhotoImage(image)

btn_load_names_txt.set("Load\nCases & Skins")
btn_prices_txt.set("Extract\nSkin Prices")

# este o carpeala de nedescris cu asezarea butoanelor astora
# nu te uita
logo_panel = tk.Label(frame1, image=logo, bd=0, highlightbackground='black')
logo_panel.grid(row=0, column=0, padx=(70, 70), pady=20)

btn_UpdateDB = tk.Button(frame1, textvariable=btn_load_names_txt, bd=2, background='cornflower blue')
btn_UpdateDB.grid(padx=(30, 250), pady=(0, 10), ipadx=50, ipady=10, row=1, column=0, sticky='W')

btn_UpdatePrices = tk.Button(frame1, textvariable=btn_prices_txt, bd=0)
btn_UpdatePrices.grid(padx=(250, 30), pady=(0, 10), ipadx=50, ipady=10, row=1, column=0, sticky='W')
# dada, vezi bine
# sunt pe aceeasi coloana 2 butoane

displayVar = tk.StringVar()
# justify = left (aliniez textul la stanga)
# anchor = 's' (ultimul text introdus ramane in josul paginii si oricum redimensionez Label-ul
#               el ramane jos de tot)
# height = 10 (inaltimea log viewer-ului sa fie de 10)
displayLab = tk.Label(frame2, textvariable=displayVar, justify='left', anchor='s', height=10)
displayLab.grid()

#btn_UpdatePrices.bind("<Button-1>", lambda event, p='TEXT NOU': log_viewer(event, p))
#btn_UpdateDB.bind("<Button-1>", lambda event, a='': displayVar.set(a))

Cases = []
btn_UpdateDB.bind("<Button-1>", extract_skins)

btn_UpdatePrices.bind("<Button-1>", printCases)


# TODO:
#   - la catergoria de get offer sa am 3-5 butoane care sa reprezinte
#   - gradul de risc pentru trade-ul care urmeaza sa pice
#    1 = spre 0 pierdere
#    3 = sanse la castiguri mari, dar si la pierderi mari


# TODO:
#   - sa incarc si texturile skin-urilor, iar atungi cand se alege o oferta, sa fie si afisata ca intr-un contract
#     pe CS:GO
#   - imi va trebui un webscrapper care sa caute rapid skin-urile (daca nu le are deja) din oferta pe csgo stash
#   si sa le descarce imaginile, iar apoi sa le foloseasca


window.mainloop()



