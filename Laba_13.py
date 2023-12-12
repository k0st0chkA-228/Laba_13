# Определить количество мужчин и женщин,
# севших в порту Квинстаун, и сколько из них выжило.

import csv


man_count = 0
women_count = 0
survived_man = 0
survived_woman = 0
with open('titanic.csv', newline='') as File:
    reader = csv.reader(File)
    for r in reader:
        if r[4] == 'male' and r[11] == 'Q':
            man_count += 1
            if r[1] == '1':
                survived_man += 1
        elif r[4] == 'female' and r[11] == 'Q':
            women_count += 1
            if r[1] == '1':
                survived_woman += 1

print('количество мужчин, севших в порту Квинстаун: ' + str(man_count),
      '\nколичество женщин, севших в порту Квинстаун: ' + str(women_count))
print('количество выживших мужчин, севших в порту Квинстаун: ' + str(survived_man),
      '\nколичество выживших женщин, севших в порту Квинстаун: ' + str(survived_woman))
