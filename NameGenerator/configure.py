from names_controller import NamesController

from file_handler import open_basic_files, open_language_files

# FIRST NAMES

# In this case the files/first_names/south_american_names.csv
#                & files/first_names/asian_names.csv
#                & files/last_names/south_american_names.csv
# Have two columns: name and language.

names_controller = NamesController()

print("Insert first names")

# Insert basic files from first names
br_names = open_basic_files('first_names','brazilian_names')
names_controller.insert_first_names(br_names, 'portuguese br')

# European first names 
euro_names = open_basic_files('first_names','european_names')
names_controller.insert_first_names(euro_names, 'european')

# EUA first names
eua_names = open_basic_files('first_names','european_names')
names_controller.insert_first_names(eua_names, 'english us')

# Now the language files
# Asian first names
asian_names = open_language_files('first_names','asian_names')

china = [ name[0] for name in asian_names if name[-1] == 'chinese' ]
japan = [ name[0] for name in asian_names if name[-1] == 'japanase' ]
korea = [ name[0] for name in asian_names if name[-1] == 'korean' ]

names_controller.insert_first_names(china, 'chinese')
names_controller.insert_first_names(japan, 'japanse')
names_controller.insert_first_names(korea, 'korean')

# South american first names
south_american_names = open_language_files('first_names', 'south_american_names')

brazil = [ name[0] for name in south_american_names if name[-1] == 'portuguese' ]
spanish = [ name[0] for name in south_american_names if name[-1] == 'spanish' ]

names_controller.insert_first_names(brazil, 'portuguese br')
names_controller.insert_first_names(spanish, 'spanish')

# LAST NAMES

print("Insert last names")

# Asian Last Names
asian_names = open_basic_files('last_names', 'asian_names')
names_controller.insert_last_names(asian_names, None)

# English names
eng_names = open_basic_files('last_names', 'english_names')
names_controller.insert_last_names(eng_names, 'english')

# European names
euro_names = open_basic_files('last_names', 'european_names')
names_controller.insert_last_names(euro_names, 'european')

# Hispanic names
hispanic_names = open_basic_files('last_names', 'hispanic_names')
names_controller.insert_last_names(hispanic_names, 'hispanic')

# Spanish names
spanish_names = open_basic_files('last_names', 'spanish_names')
names_controller.insert_last_names(spanish_names, 'spanish')

# Language file
south_american_names = open_language_files('last_names','south_american_names')

brazilian = [ name[0] for name in south_american_names if name[-1] == 'portuguese' ]
spanish = [ name[0] for name in south_american_names if name[-1] == 'spanish' ]

# South American last names
names_controller.insert_last_names(brazilian, 'portuguese br')
names_controller.insert_last_names(spanish, 'spanish')