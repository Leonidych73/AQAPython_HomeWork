#Old format
norway_text = 'Automatisering akselererer %syeblikket da roboter vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')
print(norway_text)

# python 2-3
norway_text2 = 'Automatisering akselererer {}yeblikket da roboter vil erobre planeten v{}r. ({})'.format('ø', 'å', 'Æ')
print(norway_text2)

#f-strings
a = 'ø'
b = 'å'
c = 'Æ'
norway_text3 = f'Automatisering akselererer {a}yeblikket da roboter vil erobre planeten v{b}r. ({c})'
print(norway_text3)




