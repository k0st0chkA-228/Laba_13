# Определить количество мужчин и женщин,
# севших в порту Квинстаун, и сколько из них выжило.

import csv


m_and_w = 0
survived = 0
with open('titanic.csv', newline='') as File:
    reader = csv.reader(File)
    for r in reader:
        if (r[4] == 'female' or r[4] == 'male') and r[11] == 'Q':
            m_and_w += 1
            if r[1] == '1':
                survived += 1

print('количество мужчин и женщин, севших в порту Квинстаун: ' + str(m_and_w))
print('количество выживших мужчин и женщин, севших в порту Квинстаун: ' + str(survived))
