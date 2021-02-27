import tkinter as tk
from PIL import ImageTk, Image
from pylightxl import readxl
import copy

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

def get_n_resize(skin_name):
    skin_mare = Image.open('Files/Skins/' + skin_name + '.png')
    skin_mare = skin_mare.resize((94, 71), Image.ANTIALIAS)
    skin_in = ImageTk.PhotoImage(skin_mare)
    return skin_in


def print_trade_in(skin_in):

    x = 24
    y = 390

    for i in range(0, 10):
        skin_in_label = tk.Label(frame, image=skin_in, background='gray63', width=108, height=108)

        if i == 5:
            y = 505
            x = 24

        skin_in_label.place(x=x, y=y)
        x += 115

    window.update()


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
logo = ImageTk.PhotoImage(image)

# este o carpeala de nedescris cu asezarea butoanelor astora
# nu te uita
logo_panel = tk.Label(frame, image=logo, bd=0)
logo_panel.place(x=258, y=13)

btn_UpdateDB = tk.Button(frame, text="EXTRACT\nNAMES", image=pixel, bd=0, background='gray63', fg='gray15',
                         font=('Montserrat Black', 12), width=153, height=63, compound="c")
btn_UpdateDB.place(x=12, y=208)

btn_UpdatePrices = tk.Button(frame, text="EXTRACT\nPRICES", image=pixel, bd=0, background='gray63', fg='gray15',
                             font=('Montserrat Black', 12), width=153, height=63, compound="c")
btn_UpdatePrices.place(x=12, y=284)
# dada, vezi bine
# sunt pe aceeasi coloana 2 butoane


displayVar = tk.StringVar()
# justify = left (aliniez textul la stanga)
# anchor = 'sw' (ultimul text introdus ramane in josul paginii si oricum redimensionez Label-ul
#               el ramane jos de tot, fara a da resize la fereastra)
displayLab = tk.Label(frame, textvariable=displayVar, height=10, width=55, justify='left', anchor='sw')
displayLab.place(x=178, y=208)


# region Select Risk Level.txt

select_risk = tk.Text(frame, font=('Montserrat Black', 22), bd=0, fg='tan2', bg='gray15', width=10, height=2)
select_risk.tag_configure('center', justify='center')
select_risk.insert('1.0', 'SELECT\nRISK LEVEL')
select_risk.tag_add('center', '1.0', 'end')
select_risk.place(x=590, y=225)

# endregion


# region Butoane Risk

btn_risk1 = tk.Button(frame, text="1", image=pixel, relief='solid', bd=0, background='gold', fg='tan2',
                      font=('Montserrat Black', 19), width=35, height=35, compound="c")
btn_risk1.place(x=610, y=320)
btn_risk2 = tk.Button(frame, text="2", image=pixel, relief='solid', bd=0, background='gold', fg='tan2',
                      font=('Montserrat Black', 19), width=35, height=35, compound="c")
btn_risk2.place(x=670, y=320)
btn_risk3 = tk.Button(frame, text="3", image=pixel, relief='solid', bd=0, background='gold', fg='tan2',
                      font=('Montserrat Black', 19), width=35, height=35, compound="c")
btn_risk3.place(x=730, y=320)

# endregion


bg_trade_up = tk.Label(frame, image=pixel, background='gray80', width=800, height=345)
bg_trade_up.place(x=12, y=379)

skin_in = get_n_resize('AK-47 Aquamarine Revenge')
print_trade_in(skin_in)

# skin_in = get_n_resize('AK-47 Aquamarine Revenge')
# skin_in_label = tk.Label(frame, image=skin_in, background='gray63', width=108, height=108)
# skin_in_label.place(x=24, y=400)

# TODO:
#   - la catergoria de get offer sa am 3 butoane care sa reprezinte
#   - gradul de risc pentru trade-ul care urmeaza sa pice
#    1 = spre 0 pierdere
#    3 = sanse la castiguri mari, dar si la pierderi mari


Cases = []
btn_UpdateDB.bind("<Button-1>", extract_skins)
btn_UpdatePrices.bind("<Button-1>", extract_prices)

# TODO:
#   - sa incarc si texturile skin-urilor, iar atungi cand se alege o oferta, sa fie si afisata ca intr-un contract
#     pe CS:GO
#   - pana nu exista fisierul Skin_names.xlsx sa nu fie valabil butonul Extract Prices


window.mainloop()
