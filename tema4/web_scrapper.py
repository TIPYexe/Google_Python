def extract_cases(case_text):
    img_stat = case_text.find('img') is not None
    if not img_stat:
        return

    case_name = case_text.find('img').get('alt')
    except_1 = case_name != 'All Skin Cases'
    except_2 = case_name != 'Souvenir Packages'
    except_3 = case_name != 'Gift Packages'

    if except_1 and except_2 and except_3:
        return case_text.find('img').get('alt')

