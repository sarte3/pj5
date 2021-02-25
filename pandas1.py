import pandas as pd
import seaborn as sns

# -- 오류시
# pip uninstall matplotlib
# pip install matplotlib==3.2
# pip install numpy==1.19.3

movies = pd.read_csv('data/movie.csv', header=None)
# print(movies)
# print(movies[0])
# print(movies.loc[0])
# print(movies.loc[[0,2]])

# movies.set_index()

# data = pd.read_csv('data/gap.tsv', sep='\t')
# print(data)

# tips = sns.load_dataset('tips')
# print(tips)