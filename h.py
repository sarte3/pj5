import pandas as pd
# 과제
#1) 아이티 지진시 휴대폰으로 응급사항등에 대한 전화내역 파일인
# h.csv를 읽어 데이터프레임생성,자료의 행과 열확인,자료형 확인
data = pd.read_csv('data/h.csv')
# print(data)
# print(data.shape)
# print(type(data))

# 2)메시지종류(CATEGORY)컬럼 10줄 확인
# print(data.columns)
# print(data['CATEGORY'].head(10))

# 3)CATEGORY가 널인 자료 제거,자료의 행과 열확인
data = data[pd.notnull(data['CATEGORY'])]
# print(data)
# print(data.shape)

# 4) CATEGORY를 코드번호, 코드명으로 분리
# print(data['CATEGORY'])
data['TEMP']= data['CATEGORY'].str.split(',')
data['CODENO']=data['TEMP'].str.get(0)
data['CODENAME']=data['TEMP'].str.get(1)
data = data.drop('TEMP', axis=1)
print(data)


import pandas as pd 
from numpy import NaN, nan, NAN
import numpy as np

# 과제
# 1) 아이티 지진시 휴대폰으로 응급사항등에 대한 전화내역 파일인
# h.csv를 읽어 데이터프레임생성,자료의 행과 열확인,자료형 확인
df = pd.read_csv('data/h.csv')
# print(df.columns)
# print(df.index)
# df.info()

# 2)메시지종류(CATEGORY)컬럼 10줄 확인
# print(df['CATEGORY'].head(10))

# 3)CATEGORY가 널인 자료 제거,자료의 행과 열확인
# print(df.shape[0]-df.count())
df = df[df['CATEGORY'].notnull()]
# print(df)

# 4)위치정보가 잘못된 자료 제거,자료의 행과 열확인
# 유효한 위치 : 18<LATITUDE<20, -75<LONGITUDE<-70
# df3 = df[(df['LATITUDE']>18)& (df['LATITUDE']<20)]
# df3 = df3[(df3['LONGITUDE']>-75) & (df3['LONGITUDE']<-70)]
# print(df3)

# 과제 2(20-12-31)
# CATEGORY를 코드번호, 코드명으로 분리
df = df.iloc[:-2, [0,5]]

df['CODE'] = df['CATEGORY'].str.findall('[1-9][a-z]?')
df['CODE'] = df['CODE'].apply(lambda x: ', '.join(map(str, x)))
# print(df.head(20))

dic = {
    '1':'Urgences | Emergency', 
    '1a': 'Highly vulnerable',
    '1b': 'Urgence medicale | Medical Emergency',
    '1c': 'Personnes prises au piege | People trapped',
    '1d': 'Incendie | Fire',
    '2': 'Urgences logistiques | Vital Lines',
    '2a': "Penurie d'aliments | Food Shortage",
    '2b': "Penurie d'eau | Water shortage",
    '2c': 'Probleme de securite | Security Concern',
    '2d': 'Refuge | Shelter needed',
    '2e': 'Penurie de carburant | Fuel shortage',
    '2f': 'Sans courant | Power Outage',
    '3': 'Public Health',
    '3a': 'Infectious human disease',
    '3b': 'Chronic care needs',
    '3c': 'Besoins en materiels et medicaments | Medical equipment and supply needs',
    '3d': "OBGYN/Women's Health",
    '3e': 'Psychiatric need',
    '4': 'Menaces | Security Threats',
    '4a': 'Pillage | Looting',
    '4c': 'Group violence',
    '4e': 'Assainissement eau et hygiene | Water sanitation and hygiene promotion',
    '5': 'Infrastructure Damage',
    '5a': 'Structure effondres | Collapsed structure',
    '5b': 'Structures a risque | Unstable Structure',
    '5c': 'Route barree | Road blocked',
    '5d': 'Compromised bridge',
    '5e': 'Communication lines down',
    '6': 'Natural Hazards',
    '6a': 'Deces | Deaths',
    '6b': 'Personnes Disparues | Missing Persons',
    '6c': 'Demandant de transmettre un message | Asking to forward a message',
    '6c': 'Seisme et repliques | Earthquake and aftershocks',
    '7': 'Secours | Services Available',
    '7a': "Distribution d'aliments | Food distribution point",
    '7b': "Distribution d'eau | Water distribution point",
    '7c': 'Denrees non alimentaires | Non-food aid distribution point',
    '7d': 'Services de sante | Hospital/Clinics Operating',
    '7g': 'Morgue | Human remains management',
    '7h': 'Deblayage de gravats | Rubble removal',
    '8': 'Autre | Other',
    '8a': 'IDP concentration',
    '8c': 'Price gouging',
    '8d': 'Recherche et sauvetage | Search and Rescue',
    '8e': 'Nouvelles de Personnes | Persons News',
    '8f': 'Other'
    }

list = ['1', '1a', '1b', '2', '2a', '2b','2c','2d','3']
def getCodename(x):
    x = x.split(",")
    cn = ''
    for i in range(len(x)):
        x[i]=x[i].strip()
        for j in range(len(list)):
            # print(list[j], x[i], list[j]==x[i])
            if list[j] == x[i]:
                cn = cn+''+ dic[x[i]]
    return cn

df['CODENAME'] = df['CODE'].apply(getCodename)
df = df.drop('CATEGORY', axis=1)
print(df)

df.to_csv('data/h2.csv')

# # 4) 위치정보가 잘못된 자료 제거,자료의 행과 열확인
# # 유효한 위치 : 18<LATITUDE<20, -75<LONGITUDE<-70
# #    (18보다크고) & (20보다 작다) 
# data = data[(((data['LATITUDE']>18)&(data['LATITUDE']<20))&((data['LONGITUDE']>-75)&(data['LONGITUDE']<-70)))]
# print(data)
# print(data.shape)