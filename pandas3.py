import pandas as pd
import seaborn as sns
import os

tips = sns.load_dataset('tips')
# print(tips)
# tips.info()
# print(type(tips))
# print(tips['time'])
# print(type(tips['time']))
# print(tips.loc[3])
# print(type(tips.loc[3]))
# print(tips.loc[:3, ['total_bill', 'tip']])
# print(tips.iloc[:3, :2])
# # 기존 인덱스 삭제, 지정된 열이 인덱스
# tips = tips.set_index('day')
# print(tips.loc['Sun'])
# tips = tips.set_index('smoker')
# print(tips)
# # 기존 인덱스가 열이 되고 새로운 이련번호
# tips = tips.reset_index()
# print(tips)

# s1 = pd.Series(['사과', '배', '석류'])
# # print(s1)
# # print(type(s1))

# s2 = pd.Series(['홍길동', '한양', '20세',  '정의로움'], index=['이름', '주소', '나이', '성격'])
# print(s2)
# print(s2[1])

# movies = pd.read_csv(os.path.join('data','movie.csv'), header=None, names=['title', 'grade', 'rate'])
# # print(movies)
# # print(movies.columns)
# movies = movies.set_index('title')
# # print(movies)

# # loc
# movie10 = movies.head(10)
# # print(movie10)

# # # 인덱스값으로 접근
# # print(movie10.loc['극장판 바이올렛 에버가든'])
# # print(movie10.loc[['극장판 바이올렛 에버가든', '러브 액츄얼리']]) 

# # # 행번호값으로 접근
# # print(movie10.iloc[4])
# # print(movie10.iloc[[4, 5]])

# print(movie10.loc[['극장판 바이올렛 에버가든', '러브 액츄얼리'], ['rate']])
# print(movie10.iloc[[4, 5], [1]])

# 데이터프레임 생성
# person = pd.DataFrame({
#     'name': ['심슨', '둘리', '희동', '강가딘'],
#     'addr': ['뉴욕', '쌍문동', '구로동', '대전'],
#     'age': [10, 200, 5, 20],
#     'hobby': ['기타', '수영', '독서', '독서']
# }, columns=['addr', 'age', 'hobby', 'name'])
# 칼럼 순서 지정
# print(person)

# s1 = person['name']

# print(type(s1)) # 시리즈
# print(s1)
# 시리즈의 속성
# print(s1.index)
# print(s1.values)
# 시리즈의 메서드
# print(s1.keys()) #s1.index
# print(s1.keys()[0])
# print(s1.index[0])

# print('평균', person['age'].mean())
# print('최대값', person['age'].max())
# print('최소값', person['age'].min())
# print('표준편차', person['age'].std()) # 표준 편차
# print('합계', person['age'].sum())

# 불린 추출 : 참인 것만 추출
# ages = person['age']
# print(ages)
# print(ages.mean())
# print(ages>ages.mean())
# print('참인 것만 출력', ages[[False, False, True, False]])
# print('나이가 평균 이상 출력', ages[ages>ages.mean()])

# print(tips)
# tips10 = tips.tail(10)
# # print(tips10)
# s1 = tips10['tip']
# print('팁의 평균', s1.mean())
# print('팁의 평균이상인가?', s1>=s1.mean())
# print('팁의 평균이상인 것만 출력', s1[s1>=s1.mean()])

# 브로드캐스팅 : 시리즈나 데이터프레임에 있는 모든 데이터에 대해 한꺼번에 연산
# print(s1+s1)
# 백터 : 여러개의 값을 가진 데이터
# print(s1*s1) # 백터끼리 연산, 같은 인덱스끼리 연산
# print(s1+1000) # 모든 백터에 1000이 더해짐

# s2 = pd.Series([1, 2, 3, 4, 5])

# # print(s2)
# # print(s1+s2) #NaN

# s1.index = range(0, 10, 1) # 시리즈 인덱스 변경
# print(s1)
# print(s1+s2)

print(tips)

s3 = tips['total_bill'].head(10)

# print(s3)
# print(s3.index)
# print(s3.values)
# print('값 순서 정렬\n', s3.sort_values())
# print('값 순서 내림차순 정렬\n', s3.sort_values(ascending=False))
# print('인덱스 역순서 정렬\n', s3.sort_index(ascending=False))

# print(tips.tail(10))
tips2 = tips.sample(n = 10, random_state = 19)
print(tips2)
s4 = tips2['day']
print(s4)
s4.index=range(0, 10, 1)
print(s4)
print(s4.sort_values())

tips2 = tips2.set_index('day')
print(tips2)
print('식대 순 정렬\n', tips2.sort_values(by='total_bill'))
print('성별 순 정렬\n', tips2.sort_values(by='sex'))
print('성별, 식대순 정렬\n', tips2.sort_values(by=['sex', 'total_bill']))
print('인덱스순 정렬\n', tips2.sort_index())

# 컬럼 추가
tips2['tot']=tips2['total_bill']+tips2['tip']
print(tips2)
# 컬럼 삭제
print('성별열 삭제\n', tips2.drop('sex', axis=1))
# 데이터프레임 저장
tips2.to_csv('data\\tips2.csv')
tips2.to_pickle('data\\tips2.pickle')

# gap.tsv를 읽어 들여 데이터 프레임으로 변경
# 1) g1에 country, continent, year, lifeExp 칼럼만 추출하여 데이터 프레임으로 만드세요
# 2) g1의 열과 행의 갯수를 조회하세요
# 3) lifeExp 칼럼을 기준으로 내림차순 정렬하세요
# 4) lifeExp 열을 시리즈 s1으로 생성하세요
# 5) s1의 전체 평균 출력
# 6) s1이 40미만인 것만 출력