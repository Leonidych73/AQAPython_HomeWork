# homeWork_1
# we have norway text in old style formatting
# re-write the same text as:
# #1 string with format() call
# #2 f-string
# use linter(https://github.com/wemake-services/wemake-python-styleguide)
# to check your new created python module for possible linter errors
# try to run code from pycharm/command line
# __________________________________________

# Old format
norway_text = 'Automatisering akselererer %syeblikket da roboter vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')
print(norway_text)

# python 2-3 format
norway_text2 = 'Automatisering akselererer {}yeblikket da roboter vil erobre planeten v{}r. ({})'.format('ø', 'å', 'Æ')
print(norway_text2)

# f-strings format
a = 'ø'
b = 'å'
c = 'Æ'
norway_text3 = f'Automatisering akselererer {a}yeblikket da roboter vil erobre planeten v{b}r. ({c})'
print(norway_text3)

# to check your new created python module for possible linter errors using command: flake8 homeWork_1.py

# to run from command line using the command: python homeWork_1.py
