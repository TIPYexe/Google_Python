def extract_case_name(data):
    return data.find('img').get('alt')

def extract_case_link(data):
    return data.find('a').get('href')


# pastrez doar diviziunile cu date despre cutii
# adica fara datele extrase gresit
def filter_cases(case_text):

    img_stat = case_text.find('img') is not None
    if not img_stat:
        return False

    case_name = case_text.find('img').get('alt')
    except_1 = case_name != 'All Skin Cases'
    except_2 = case_name != 'Souvenir Packages'
    except_3 = case_name != 'Gift Packages'

    if except_1 and except_2 and except_3:
        return True

def extract_data(data):
    #cols = ['Name', 'Link', 'Convert', 'Classified', 'Restricted', 'Mil-Spec']
    data_filtered = set(filter(filter_cases, data))
    cases_names = set(map(extract_case_name, data_filtered))
    cases_links = set(map(extract_case_link, data_filtered))

    return (cases_names, cases_links)
