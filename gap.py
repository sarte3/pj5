import pandas as pd

# gap.tsv를 읽어 들여 데이터 프레임으로 변경
gap = pd.read_csv('data/gap.tsv', sep='\t')

# 1) g1에 country, continent, year, lifeExp 칼럼만 추출하여 데이터 프레임으로 만드세요
g1 = gap[['country', 'continent', 'year', 'lifeExp']]

# 2) g1의 열과 행의 갯수를 조회하세요
print(g1.shape)

# 3) lifeExp 칼럼을 기준으로 내림차순 정렬하세요
print(g1.sort_values(by='lifeExp', ascending=False))

# 4) lifeExp 열을 시리즈 s1으로 생성하세요
s1 = g1['lifeExp']

# 5) s1의 전체 평균 출력
print(s1.mean())

# 6) s1이 40미만인 것만 출력
print(s1[s1<40])