import re
def formatWellName(well_name):
    # Remove all non-alphanumeric chars except for '-', '(', and ')', then strip().
    new_name = well_name.strip()
    new_name = re.sub('[.] *', '', new_name)
    new_name = re.sub('[^a-zA-Z0-9-()]', '', new_name)
    new_name = re.sub('[+-/]', '', new_name)
    # new_name = re.sub(' -', ' ', new_name)
    return new_name


def flattenWellName(well_name, rep={"#": "", "'": "", ",": "", "\"": "", "-": "",
                                    "_": "","@":"","*":"","$":"",".":"","&":"","%":"", }):
    # Flattern the well names, and remove redundant substrings like: north, south, allocation, etc.
    # 'Cenizo A 101H' -> 'cenizoa101h', 'Martinez South A 103H' -> 'martineza103h'

    # rep defines desired replacement substrings
    rep = dict((re.escape(k), v) for k, v in rep.items())

    pattern = re.compile("|".join(rep.keys()))
    flatten_name = pattern.sub(
        lambda m: rep[re.escape(m.group(0))], well_name.lower())

    return flatten_name

print(flattenWellName("dfna_df@# dfsfkj_- make"))
print(formatWellName("dfna_df@# dfsfkj_- make"))