import pandas as pd

data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

stats = ['H', 'avg', 'HR', 'OBP']
positions = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
data_df_2018 = data_df[data_df['year'] == 2018]

for year in [2015, 2016, 2017, 2018]:
    for stat in stats:
        print(f'\n"{year}" Top 10 player in "{stat}":')
        top_players = data_df[data_df['year'] == year].nlargest(10, stat)[['batter_name', stat]]
        print(top_players)

for position in positions:
    top_player = data_df_2018[data_df_2018['cp'] == position].nlargest(1, 'war')[['batter_name', 'war']]
    print(f'\n Top "{position}" in 2018:')
    print(top_player)

cor_stats = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']
cor = data_df[cor_stats + ['salary']].corr()['salary'].drop('salary')

highest_stat = cor.idxmax()
print(f"\n[Highest correlation Salary: '{highest_stat}', correlation: '{cor[highest_stat]}']")