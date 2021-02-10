import xlsxwriter

def to_xlsx(Cases):

    # Generez fisierul Excel
    wb = xlsxwriter.Workbook('Case_data.xlsx')

    # region Sheet Cases

    # Generez sheet pentru Cutii
    sheet_cases = wb.add_worksheet('Cases')

    # Adaug numele coloanelor: Case Name, Link
    sheet_cases.write(0, 0, 'Case Name')
    sheet_cases.write(0, 1, 'Link')

    # Adaug datele in coloane
    for index, case in enumerate(Cases):
        sheet_cases.write(index + 1, 0, case.name)
        sheet_cases.write(index + 1, 1, case.link)
    #endregion

    # Generez sheet pentru fiecare Cutie in care salvez toate skin-urile din ea
    for case in Cases:
        # sheet_SingleCase
        sheet_scase = wb.add_worksheet(case.name.replace(':', ''))

        # adaug numele coloanelor
        sheet_scase.write(0, 0, 'Skin')
        sheet_scase.write(0, 1, 'Weapon')
        sheet_scase.write(0, 2, 'Rarity')

        # Fara ST
        sheet_scase.write(0, 3, 'FN')
        sheet_scase.write(0, 4, 'MW')
        sheet_scase.write(0, 5, 'FT')
        sheet_scase.write(0, 6, 'WW')
        sheet_scase.write(0, 7, 'BS')

        # Cu ST
        sheet_scase.write(0, 8, 'SFT')
        sheet_scase.write(0, 9, 'SMW')
        sheet_scase.write(0, 10, 'SFT')
        sheet_scase.write(0, 11, 'SWW')
        sheet_scase.write(0, 12, 'SBS')

        # adaug numele si datele despre skin-uri
        for index, skin in enumerate(case.Skins):
            sheet_scase.write(index + 1, 0, skin.name)
            sheet_scase.write(index + 1, 1, skin.weapon)
            sheet_scase.write(index + 1, 2, skin.rarity)

            # adaug preturile pt fiecare calitate a armei
            if skin.extra.FN != -1:
                sheet_scase.write(index + 1, 3, skin.extra.FN)
            if skin.extra.WW != -1:
                sheet_scase.write(index + 1, 4, skin.extra.MW)
            if skin.extra.FT != -1:
                sheet_scase.write(index + 1, 5, skin.extra.FT)
            if skin.extra.WW != -1:
                sheet_scase.write(index + 1, 6, skin.extra.WW)
            if skin.extra.BS != -1:
                sheet_scase.write(index + 1, 7, skin.extra.BS)

            if skin.extra.SFN != -1:
                sheet_scase.write(index + 1, 8, skin.extra.SFN)
            if skin.extra.SMW != -1:
                sheet_scase.write(index + 1, 9, skin.extra.SMW)
            if skin.extra.SFT != -1:
                sheet_scase.write(index + 1, 10, skin.extra.SFT)
            if skin.extra.SWW != -1:
                sheet_scase.write(index + 1, 11, skin.extra.SWW)
            if skin.extra.SBS != -1:
                sheet_scase.write(index + 1, 12, skin.extra.SBS)

    # Salvez Fisierul
    wb.close()