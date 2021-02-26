import tkinter as tk
from PIL import ImageTk, Image
from pylightxl import readxl

import price_scrapper as pricey
import Case_Skins as cls
import web_scrapper as cs_scrp
import get_offer_alg as alg
import save_to_db as save


def updateDisplay(myString):
    displayVar.set(displayVar.get() + '\n' + myString)


def extract_skins(event):
    # dezactivez butonul
    btn_UpdateDB['state'] = 'disabled'
    btn_UpdateDB.unbind("<Button-1>")
    # curat fereastra de log
    displayVar.set('')
    window.update()

    # functia propriu-zisa
    Cases = cs_scrp.extract_from_cases('https://csgostash.com/containers/skin-cases', displayVar, window)
    save.to_xlsx(Cases, 'Files/Skin_names.xlsx', False)

    # reactivez butonul
    btn_UpdateDB['state'] = 'active'
    btn_UpdateDB.bind("<Button-1>", extract_skins)


def extract_prices(event):
    # dezactivez butonul
    btn_UpdatePrices['state'] = 'disabled'
    btn_UpdatePrices.unbind("<Button-1>")
    # curat fereastra de log
    displayVar.set('')
    window.update()

    # functia propriu-zisa
    db = readxl('Files/Skin_names.xlsx')
    sheet_names = db.ws_names

    for sheet in sheet_names[1:]:
        ObjCase = cls.Case()
        ObjCase.name = sheet
        alg.read_xl(db, sheet, ObjCase)
        Cases.append(ObjCase)

    pricey.extract_prices('Files/Skin_names.xlsx', 'Files/Skin_prices.xlsx', displayVar, window)

    # reactivez butonul
    btn_UpdatePrices['state'] = 'active'
    btn_UpdatePrices.bind("<Button-1>", extract_prices)

# TODO:
#   - sa fac si eu un fisier pentru constante (nume de fisiere and shit)

window = tk.Tk()
window.geometry('825x733')
window.title("CS:GO Trade-up Scrapper")
window.resizable(False, False)

path_logo = 'Files/logo.png'

pixel = tk.PhotoImage(width=1, height=1)

frame = tk.Frame(bg='gray15', height=733, width=825)
frame.pack()

# log_viewer = tk.Frame(master=window, weight=354.49, height=160.93, bg='white')
# log_viewer.pack(fill=tk.Y, side=tk.RIGHT)

image = Image.open(path_logo)
#image = image.resize((300, 197))
logo = ImageTk.PhotoImage(image)

# este o carpeala de nedescris cu asezarea butoanelor astora
# nu te uita
logo_panel = tk.Label(frame, image=logo, bd=0)
logo_panel.place(x=258, y=13)

btn_UpdateDB = tk.Button(frame, text="EXTRACT\nNAMES", image=pixel, bd=0, background='gray63', fg='gray34', font=('Montserrat Black', 12), width=153, height=63, compound="c")
btn_UpdateDB.place(x=47, y=209)

btn_UpdatePrices = tk.Button(frame, text="EXTRACT\nPRICES", image=pixel, bd=0, background='gray63', fg='gray34', font=('Montserrat Black', 12), width=153, height=63, compound="c")
btn_UpdatePrices.place(x=47, y=289)
# dada, vezi bine
# sunt pe aceeasi coloana 2 butoane


displayVar = tk.StringVar()
# justify = left (aliniez textul la stanga)
# anchor = 's' (ultimul text introdus ramane in josul paginii si oricum redimensionez Label-ul
#               el ramane jos de tot)
# height = 10 (inaltimea log viewer-ului sa fie de 10)
# displayLab = tk.Label(window, textvariable=displayVar, height=161, width=355)
# displayLab.place(x=212, y=209)

# btn_UpdatePrices.bind("<Button-1>", lambda event, p='TEXT NOU': log_viewer(event, p))
# btn_UpdateDB.bind("<Button-1>", lambda event, a='': displayVar.set(a))

Cases = []
btn_UpdateDB.bind("<Button-1>", extract_skins)
btn_UpdatePrices.bind("<Button-1>", extract_prices)

# TODO:
#   - la catergoria de get offer sa am 3-5 butoane care sa reprezinte
#   - gradul de risc pentru trade-ul care urmeaza sa pice
#    1 = spre 0 pierdere
#    3 = sanse la castiguri mari, dar si la pierderi mari


# TODO:
#   - sa incarc si texturile skin-urilor, iar atungi cand se alege o oferta, sa fie si afisata ca intr-un contract
#     pe CS:GO


window.mainloop()
