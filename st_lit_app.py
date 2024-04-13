import pandas as pd
import numpy as np
import streamlit as st
from matplotlib import pyplot as plt
from PIL import Image

file1 = pd.read_csv("https://raw.githubusercontent.com/Mushkat/DsCourseProject/main/profes16.csv", delimiter=';', on_bad_lines='skip')
file2 = pd.read_csv("https://raw.githubusercontent.com/Mushkat/DsCourseProject/main/profes23.csv", delimiter=';', on_bad_lines='skip')
years1 = file1.columns[1:].astype(str)
sal1 = file1[file1['Отрасль'] == 'Строительство'].values[0][1:]
years2 = file2.columns[1:-1].astype(str)
sal2 = file2[file2['Отрасль'] == 'строительство'].values[0][1:-1]
sal_all_build = np.concatenate((sal1, sal2))
years = np.concatenate((years1, years2))
sal_all_build = np.concatenate((sal1, sal2))
years = np.concatenate((years1, years2))
sal_all_build = np.concatenate((sal1, sal2))
years = np.concatenate((years1, years2))
fig1, ax1 = plt.subplots()
ax1.set_title('Изменение среднемесячной номинальной заработной платы в сфере строительства')
ax1.set_xlabel('Год, начиная с 2000')
ax1.set_ylabel('Среднемесячная номинальная зп')
ax1.plot(sal_all_build, '-')
ax1.grid(True)


sal1_ts = file1[file1['Отрасль'] == 'производство транспортных средств и оборудования'].values[0][1:]
sal2_ts = file2[file2['Отрасль'] == 'производство прочих транспортных средств и оборудования'].values[0][1:-1]
sal2_ts[0] = int(sal2_ts[0])
sal_all_ts = np.concatenate((sal1_ts, sal2_ts))
fig2, ax2 = plt.subplots()
ax2.set_title('Изменение среднемесячной номинальной заработной платы в сфере производства тс')
ax2.set_xlabel('Год, начиная с 2000')
ax2.set_ylabel('Среднемесячная номинальная зп')
ax2.plot(sal_all_ts, '-')
ax2.grid(True)

real_sal_build = []
for i in range((len(sal_all_build)-2)):
    t = ((int(sal_all_build[i+1]) - int(sal_all_build[i]))/ int(sal_all_build[i]))*100
    real_sal_build.append(t)
file_infl = pd.read_csv("https://raw.githubusercontent.com/Mushkat/DsCourseProject/main/inflation.csv", delimiter=';', on_bad_lines='skip')
infl = file_infl[file_infl['Год'] == 'Всего'].values[0][1:]

fig3, plt1 = plt.subplots()
plt2 = plt1.twinx()
plt1.set_title("Изменение зп в сфере строительства и изменение инфляции")
plt1.set_xlabel('Год, начиная с 2000')
plt1.set_ylabel('Процент')
plt1.plot(real_sal_build, "-", color = 'b', label = 'Изменение средней зп                                ' )
plt2.plot(infl[1:-1], "-", color = 'r', label = 'Инфляция' )
plt1.legend()
plt2.legend()
plt1.grid(True)


real_sal_ts = []
for i in range((len(sal_all_ts)-2)):
    t = ((int(sal_all_ts[i+1]) - int(sal_all_ts[i]))/ int(sal_all_ts[i]))*100
    real_sal_ts.append(t)
fig4, plt1 = plt.subplots()
plt2 = plt1.twinx()
plt1.set_title("Изменение зп в сфере производства тс и изменение инфляции")
plt1.set_ylabel('Процент')
plt1.plot(real_sal_ts, "-", color = 'b', label = 'Изменение средней зп                                ' )
plt2.plot(infl[1:-1], "-", color = 'r', label = 'Инфляция' )
plt1.legend()
plt2.legend()
plt1.grid(True)


change_infl = []
for i in range(len(infl)):
    infl[i] = (infl[i]+100)/100
    change_infl.append(infl[i])
real_sal = []
for a in range(len(sal_all_build)):
    real_sal.append(int(sal_all_build[a])/change_infl[a])
fig5, ax5 = plt.subplots()
ax5.plot(real_sal, '-', color = 'r',label = 'Реальная зп' )
ax5.plot(sal_all_build, '-', color = 'b',label = 'Номинальная зп')
ax5.legend()
ax5.set_title('График номинальной и реальной зарплатой в сфере строительства')
ax5.set_xlabel('Год, начиная с 2000')
ax5.set_ylabel('Средняя зп')
ax5.grid(True)


real_sal2 = []
for a in range(len(sal_all_ts)):
    real_sal2.append(int(sal_all_ts[a])/change_infl[a])
fig6, ax6 = plt.subplots()
ax6.plot(real_sal2, '-', color = 'r',label = 'Реальная зп')
ax6.plot(sal_all_ts, '-', color = 'b', label = 'Номинальная зп')
ax6.legend()
ax6.set_title('График номинальной и реальной зарплатой в сфере производства тс')
ax6.set_xlabel('Год, начиная с 2000')
ax6.set_ylabel('Средняя зп')
ax6.grid(True)


dis_build = []
dis_ts = []
for i in range(len(sal_all_ts)):
    dis_build.append(int(sal_all_ts[i])-real_sal2[i])
for j in range(len(sal_all_build)):
    dis_ts.append(int(sal_all_build[j])-real_sal[j])
n = len(sal_all_build)
r = np.arange(n)
fig7, ax7 = plt.subplots()
ax7.bar(r, dis_build, color = 'r', width = 0.25, edgecolor = 'black', label='Строительство')
ax7.bar(r+0.5, dis_ts, color = 'g', width = 0.25, edgecolor = 'black', label='Производство тс')
ax7.set_xlabel("Год, начиная с 2000")
ax7.set_ylabel("Разница в рублях")
ax7.set_title("Разница между реальными и номинальными зарплатами")
ax7.legend()
ax7.grid(True)


st.title('Анализ изменения зарплат в России с 2000 по 2023 год:cactus:')

st.markdown('Для этого проекта я выбрал две сферы: производство транспортных средств и строительство. Используя данные  '
' Росстата о среднемесячной начинасленной заработной плате 2000-2023г., изучил то, как менялись зарплаты за последние 23 года'
' и сделал выводы об оплате труда в России.')

st.markdown('Вот как менялась средняя номинальная заработная плата в обеих сферах с 2000 по 2023 год:')
st.pyplot(fig1)
st.pyplot(fig2)

st.warning('На графиках виден постепенный рост с незначительными спадами, можно сказать, что зарплаты в сфере производства транспортных'
' средств и строительства своевременно индексируются, номинальный доход увеличивается')

st.markdown('После я решил узнать, как изменение заработных плат(в процентах, к пред.году) соотносится с уровнем инфляции в России в этот год.')
st.pyplot(fig3)
st.pyplot(fig4)

st.warning('В случае со строительством, изменение средней заработной платы в некторые годы превышает инфляцию,'
' значит, работники действительно получают больше, а для занятых в сфере производства транспортных средств, '
' повышение зарплаты чаще ниже, чем уровень  инфляции,  вероятно их реальных доход практически не растет.')

st.markdown(' Я решил проверить эту гипотезу и подсчитал реальные зп для обеих сфер, сравнив их с номинальными.')


st.pyplot(fig5)
st.pyplot(fig6)

st.warning('Оказалось, что реальный доход работников в отрасли строительства и производства траснпортных средств всегда ниже номинального.')

st.markdown('Таким образом, несмотря на повышение заработных плат в обеих сферах, реально финансовое положение людей вряд ли меняется. '
'Я также подсчитал разницу между реальным и номинальным доходом и решил сравнить отрасли между собой. ')

st.pyplot(fig7)

st.warning('На графике видно, что разница между номинальным и реальным доходом в сфере строительства выше, на пике достигает более семи тысяч рублей.'
' В случае с производством транспортных средств наибольшая разница составила более шести тысяч. В обоих случаях пик пришелся на 2022 год. '
' Я считаю, что проблема разницы между номинальными и реальными доходами населения весома и значима, '
'так как мы можем наблюдать ее на протяжении всего времени, охватываемого собранными данными, тем не менее, не сложно догадаться, что она может '
'объяснятся, в том числе, политическими факторами.  ')

image = Image.open('mem.jpg')
st.image(image)