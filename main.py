import pandas as pd
from pandas.core.frame import DataFrame as DataFrame

# 책 데이터가 구로, 광주, 하남, 이천, 의정부, 양주가 있으므로, 이 지역의 투표 값을 가져옴

# 거소·선상투표, 관외사전투표, 국외부재자투표 수는 지역 도서량에 따른 투표에 연관되어있지 않기 때문에 드랍

# pd.read_excel('./data/지역구/9경기/개표상황(투표구별)')

def process_dataframe(df: DataFrame) -> DataFrame:
  df = df.drop(index=[0, 1, 4, len(df)-1], columns=['개표상황(투표구별)'])

  df_member_df = df.loc[3]
  df_member_df = df_member_df.dropna()


  df_member_list = list()

  for i in list(df_member_df):
    if '\n' in i:
      temp_text = i.split('\n')
      if temp_text[0]:
        df_member_list.append(temp_text[0])

  df_column_pre = df.loc[2]

  df_column_pre = df_column_pre.drop(df_column_pre.tail(2).index)

  df_column_pre = df_column_pre.dropna()

  df_column = pd.concat([df_column_pre, pd.DataFrame(df_member_list)])

  df_column = df_column[~df_column[0].str.contains("후보자별 득표수")]

  df = df.drop(index=[2, 3])

  df_left = df[df.columns[: len(df_column)]]
  df_left = df_left.reset_index(drop=True)
  df_right = df[df.columns[-2: ]]
  df_right = df_right.reset_index(drop=True)

  df_dataset = pd.merge(df_left, df_right, how='outer', left_index=True, right_index=True)

  df_column = pd.concat([df_column, pd.DataFrame(["무효 투표수", "기권수"])])

  df_dataset.columns = df_column

  print(df_dataset.head(10))

  return df_dataset

# 구로
gr_gab = pd.read_excel('./data/지역구/1서울/개표상황(투표구별)_구로구갑.xlsx')
gr_uel = pd.read_excel('./data/지역구/1서울/개표상황(투표구별)_구로구을.xlsx')

# gr_gab_dataset = process_dataframe(gr_gab)
gr_uel_dataset = process_dataframe(gr_uel)

# gj_dataframe = gr_gab_dataset.add(gr_uel_dataset)

# print(gj_dataframe.head(10))

# # 광주
# gj_gab = pd.read_excel('./data/지역구/9경기/개표상황(투표구별)_광주시갑.xlsx')
# gj_uel = pd.read_excel('./data/지역구/9경기/개표상황(투표구별)_광주시을.xlsx')

# gj_dataframe = pd.concat([gj_gab, gj_uel])

# # 하남

# hn_dataframe = pd.read_excel('./data/지역구/9경기/개표상황(투표구별)_하남시.xlsx')

# # 이천

# ic_dataframe = pd.read_excel('./data/지역구/9경기/개표상황(투표구별)_이천시.xlsx')

# # 의정부

# ijb_gab = pd.read_excel('./data/지역구/9경기/개표상황(투표구별)_의정부시갑.xlsx')
# ijb_uel = pd.read_excel('./data/지역구/9경기/개표상황(투표구별)_의정부시을.xlsx')

# ijb_dataframe = pd.concat([ijb_gab, ijb_uel])

# # 양주

# yj_dataframe = pd.read_excel('./data/지역구/9경기/개표상황(투표구별)_양주시.xlsx')

# # save to csv

# gr_dataframe.to_csv('./data/vote_preprocessed/vote_guro.csv')
# gj_dataframe.to_csv('./data/vote_preprocessed/vote_gwangju.csv')
# hn_dataframe.to_csv('./data/vote_preprocessed/vote_hanam.csv')
# ic_dataframe.to_csv('./data/vote_preprocessed/vote_icheon.csv')
# ijb_dataframe.to_csv('./data/vote_preprocessed/vote_uijeongbu.csv')
# yj_dataframe.to_csv('./data/vote_preprocessed/vote_yangju.csv')