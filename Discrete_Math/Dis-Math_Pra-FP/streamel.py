import streamlit as st
import pandas as sk

def soal_1():
    table = []
    for uno in [True, False]:
        for dos in [True, False]:
            for tres in [True, False]:
                for cuatro in [True, False]:
                    for cinco in [True, False]:
                        for seis in [True, False]:
                            for siete in [True, False]:
                                for ocho in [True, False]:
                                    red_1 = uno or dos
                                    green_1 = tres ^ cuatro
                                    blue_1 = cinco and seis
                                    red_2 = red_1 or green_1
                                    red_3 = siete or red_2
                                    blue_3 = red_2 and ocho
                                    green_3 = blue_1
                                    red_4 = red_3 or blue_3
                                    blue_4 = blue_3 and green_3
                                    red_5 = red_4 or blue_4
                                    light_on = red_5
                                    table.append(sk.DataFrame({'1': [uno],
                                                                '2': [dos],
                                                                '3': [tres],
                                                                '4': [cuatro],
                                                                '5': [cinco],
                                                                '6': [seis],
                                                                '7': [siete],
                                                                '8': [ocho],
                                                                'Light': [light_on]}))
    truthTable = sk.concat(table, ignore_index=True)
    return truthTable

def check_first(dist):
    vlue = []
    for i in dist:
        if i == '-':
            vlue.append('Salah')
        else:
            vlue.append('Benar')
    
    a = [i for i in set(vlue)]

    if len(a) > 1:
        return 'Salah'
    elif a[0] == 'Benar':
        return 'Benar'
    elif a[0] == 'Salah':
        return 'Salah'

def check_second(dist):
    moms = []
    for i in dist:
        for j in range(len(dist[i])):
            if i != '-':
                if dist[i][j]!= '-':
                    moms.append(dist[i][j])

    null = 0
    for i in dist:
        if i == '-':
            null += 1
            
    mom = [i for i in set(moms)]

    counts = []
    for i in mom:
        count = []
        for j in dist:
            for k in range(len(dist[j])):
                if j != '-':
                    if dist[j][k] == i:
                        count.append('1')
        if len(count) == len(dist) - null:
            counts.append('1')

    if len(counts) >= 1:
        return 'Benar'
    else:
        return 'Salah'

def check_third(dist):
    rest = []
    for i in dist:
        for j in dist:
            for k in range(len(dist[j])):
                if i == dist[j][k]:
                    if dist[j][k] != '-': 
                        rest.append(1)
                else:
                    if dist[j][k] != '-':
                        rest.append(0)
                    
    a = set(rest)
    b = len(a) - 1

    binr = [i for i in a]

    if binr[b] == 1:
        return 'Benar'
    elif binr[0] == 1:
        return 'Benar'
    else:
        return 'Salah'


st.title("Soal Pertama")

user_input = st.selectbox("Tampilkan tabel :", ["Ya", "Tidak"])
if user_input == "Ya":
    st.table(soal_1())

true_lamp = st.selectbox("Tampilkan lampu yang menyala(true):", ["Ya", "Tidak"])
if true_lamp == "Ya":
    st.table(soal_1()[soal_1()['Light'] == True])
    st.write("240 rows x 9 colums")

st.title("Soal Kedua")
n = st.text_input("Masukkan jumlah orang (n):")
n = int(n)

list = []
for i in range(n):
    key = st.text_input(f"Masukkan nama anak ke {i+1} :")
    value = st.text_input(f"Masukkan nama ibu ke {i+1} :")
    list.append((key, value))

dist = {}
for key, value in list:
    if key in dist:
        dist[key].append(value)
    else:
        dist[key] = [value]

st.write("Kasus pertama ∀𝑥∃𝑦(𝑚𝑜𝑡ℎ𝑒𝑟(𝑥, 𝑦)) :", check_first(dist))
st.write("Kasus kedua ∃𝑥∀𝑦(𝑚𝑜𝑡ℎ𝑒𝑟(𝑥, 𝑦)) :", check_second(dist))
st.write("Kasus ketiga ∃𝑥∃𝑦∃𝑧(𝑚𝑜𝑡ℎ𝑒𝑟(𝑥, 𝑚𝑜𝑡ℎ𝑒𝑟(𝑦, 𝑧))) :", check_third(dist))
