# Определить количество мужчин и женщин,
# севших в порту Квинстаун, и сколько из них выжило.

import csv


m_and_w = []
with open('test.csv', newline='') as File:
    reader = csv.reader(File)
    for r in reader:
        if (r[3] == 'female' or r[3] == 'male') and r[10] == 'Q':
            m_and_w.append(r[0])

survived = 0
with open('gender_submission.csv', newline='') as File:
    reader = csv.reader(File)
    for r in reader:
        for i in m_and_w:
            if r[0] == i and r[1] == '1':
                survived += 1

print('количество мужчин и женщин, севших в порту Квинстаун: ' + str(len(m_and_w)))
print('количество выживших мужчин и женщин, севших в порту Квинстаун: ' + str(survived))
