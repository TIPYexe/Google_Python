import pylightxl as xl
import Case_Skins as cls


# skins = skin-uri care pot pica (cu duplicate)
# skins_set = skin-uri care pot pica (fara duplicate)
def calc_procent(skins, skins_set):
    # numar aparitiile fiecarui skin din skins_set in skins
    # (nu exista skin in skins_set care sa nu existe in skins, sau invers)
    nr = []
    for index, skin in enumerate(skins_set):
        nr_aux = 0
        for i in skins:
            if i == skin:
                nr_aux += 1

        nr[index] = nr_aux

    # atribui sansa pentru fiecare skin in parte
    for i, sansa in enumerate(nr):
        nr[i] = nr[i] / len(skins)

    return nr


# va fi apelata pentru fiecare cutie
def read_xl(db, sheet_name, Cases):
    Covert = []
    Classified = []
    Restricted = []
    Mil = []
    [roww, coll] = db.ws(sheet_name).size
    data = db.ws(sheet_name).range('A2:N' + str(roww))
    for row in data:
        ObjSkin = cls.Skin()
        ObjSkin.name = row[0]
        ObjSkin.weapon = row[1]
        ObjSkin.prices.append(row[4])
        ObjSkin.prices.append(row[5])
        ObjSkin.prices.append(row[6])
        ObjSkin.prices.append(row[7])
        ObjSkin.prices.append(row[8])
        ObjSkin.prices.append(row[9])
        ObjSkin.prices.append(row[10])
        ObjSkin.prices.append(row[11])
        ObjSkin.prices.append(row[12])
        ObjSkin.prices.append(row[13])

        if row[2] == 'Covert':
            Covert.append(ObjSkin)
        if row[2] == 'Classified':
            Classified.append(ObjSkin)
        if row[2] == 'Restricted':
            Restricted.append(ObjSkin)
        if row[2] == 'Mil-Spec':
            Mil.append(ObjSkin)

    Cases.byRarity.append(Covert)
    Cases.byRarity.append(Classified)
    Cases.byRarity.append(Restricted)
    Cases.byRarity.append(Mil)


def cheapest_skin(skin_list, i):
    minimum = 99999
    index = -1

    # cel mai ieftin din raritatea la care ne aflam la acest pas
    # index_2 = indicele skinului curent
    for index_2, skin in enumerate(skin_list):
        if skin.prices[i] != '':
            if float(skin.prices[i]) < minimum:
                minimum = float(skin.prices[i])
                index = index_2
    if index != -1:
        return skin_list[index]
    else:
        return -1


def generate_offer(Cases):
    best_deals = []
    for case in Cases:

        # luam calitatile pe rand (FN, MW, FT, ...)
        for i in range(0, 10):

            # pentru fiecare raritate de skin
            # index_0 = indecele raritatii cu 1 mai mic
            for index_0, skin_list in enumerate(case.byRarity[1:]):

                cheap_skin = cheapest_skin(skin_list, i)
                if cheap_skin != -1:
                    # floatr-un contract imi trebuie 10 skinuir
                    # adaug acest cel mai ieftin skin de 10 ori
                    trade_up = []

                    trade_price = 10 * float(cheap_skin.prices[i])

                    cheap_skin_2 = cheapest_skin(case.byRarity[index_0], i)
                    if cheap_skin_2 != -1:
                        if float(cheap_skin_2.prices[i]) >= trade_price*1:
                            best_deals.append([case.name, cheap_skin, i, case.byRarity[index_0]])

    return best_deals
    # for j in range(0, 10):
    #     # salvez in pereche, skin-ul cel mai ieftin, si lista de skin-uri care pot pica
    #     trade_up.append([skin_list[index], case.byRarity[index_0]])


Cases = []
db = xl.readxl('Case_data.xlsx')
sheet_names = db.ws_names

for sheet in sheet_names[1:]:
    ObjCase = cls.Case()
    ObjCase.name = sheet
    read_xl(db, sheet, ObjCase)
    Cases.append(ObjCase)

best_deals = generate_offer(Cases)
for deal in best_deals:
    index = -1
    for skin in deal[3]:
        if skin.prices[deal[2]] == '':
            index = 1

    if index == -1:
        print()
        print('Cutie: ' + deal[0])
        print('Skin to buy: ' + deal[1].name)
        print('Quality: ' + str(deal[2]))
        print('Skin cost: ' + str(deal[1].prices[deal[2]]) + '$')
        print('Total invest: ' + str(10 * deal[1].prices[deal[2]]) + '$')
        print('Skins to get:')

        for skin in deal[3]:
                print(skin.name + ' ' + str(skin.prices[deal[2]]) + '$')

# for skin in Cases[0].byRarity[0]:
#     print(skin.name)
