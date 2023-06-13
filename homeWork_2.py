# HomeWork_2
# ________________________________________________________
# The English language has five vowels: A, E, I, O, and U
# Please count each vowel occurence in text bellow
# ( sum of lower and capital cases)
# and write output as table smth like this
# -----------------
# | vowel | count |
# -----------------
# |   a   |  11   |
# |   e   |  23   |
#   ...
# -----------------

poem_text = (f"""I wandered lonely as a cloud
That floats on  high o'er vales and hills,"""f"""
When all at once I saw a crowd,
A host, of golden daffodils;"""f"""
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze. """f"""

Continuous as the stars that shine
And twinkle on the Milky Way,"""f"""
They stretched in never-ending line
Along the margin of a bay:"""f"""
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance.""")
# _____________________________________________________
# The vowels counting by string method .count:

print("-" * 17)
print(f"| {'Vowel':^5} | {'Count':^5} |")
print("-" * 17)
print(f"| {'a':^5} | {poem_text.count('a') + poem_text.count('A'):^5} |")
print(f"| {'e':^5} | {poem_text.count('e') + poem_text.count('E'):^5} |")
print(f"| {'i':^5} | {poem_text.count('i') + poem_text.count('I'):^5} |")
print(f"| {'o':^5} | {poem_text.count('o') + poem_text.count('O'):^5} |")
print(f"| {'u':^5} | {poem_text.count('u') + poem_text.count('U'):^5} |")
print("-" * 17)

# The counting by iteration:
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

print("-" * 17)
print(f"| {'Vowel':^5} | {'Count':^5} |")
print("-" * 17)
for x in poem_text:
    if x == 'A' or x == 'a':
        count_a += 1
    if x == 'E' or x == 'e':
        count_e += 1
    if x == 'I' or x == 'i':
        count_i += 1
    if x == 'O' or x == 'o':
        count_o += 1
    if x == 'U' or x == 'u':
        count_u += 1
print(f"| {'a':^5} | {count_a:^5} |")
print(f"| {'e':^5} | {count_e:^5} |")
print(f"| {'i':^5} | {count_i:^5} |")
print(f"| {'o':^5} | {count_o:^5} |")
print(f"| {'u':^5} | {count_u:^5} |")
print("-" * 17)
# ______________________________________________________

# then modify text where each vowel replaced with
# A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
# ex. "Í wàndéréd lónély...."   and print it

# The text changing by string method .replace:
new_string = poem_text.replace('A', 'À').replace('a', 'à').replace('E', 'É').replace('e', 'é').replace('I', 'Í').replace('i', 'í').replace('O', 'Ó').replace('o', 'ó').replace('U', 'Ú').replace('u', 'ú')
print(new_string)

print("-" * 30)  # the  block divider

# The text changing by iteration:
replacements = {'A': 'À', 'a': 'à', 'E': 'É', 'e': 'é', 'I': 'Í',
                'i': 'í', 'O': 'Ó', 'o': 'ó', 'U': 'Ú', 'u': 'ú'}
new_string_2 = ""
for char in poem_text:
    if char in replacements:
        new_string_2 += replacements[char]
    else:
        new_string_2 += char
print(new_string_2)
# _______________________________________











