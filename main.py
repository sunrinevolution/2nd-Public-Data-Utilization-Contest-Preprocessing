import pandas as pd

# 책 데이터가 구로, 광주, 하남, 이천, 의정부, 양주가 있으므로, 이 지역의 투표 값을 가져옴

# 거소·선상투표, 관외사전투표, 국외부재자투표 수는 지역 도서량에 따른 투표에 연관되어있지 않기 때문에 드랍

# pd.read_excel('./data/지역구/9경기/개표상황(투표구별)')

# 구로
gr_gab = pd.read_excel('./data/지역구/1서울/개표상황(투표구별)_구로구갑.xlsx')
gr_uel = pd.read_excel('./data/지역구/1서울/개표상황(투표구별)_구로구을.xlsx')

# gr_dataframe = pd.concat([gr_gab, gr_uel])

gr_gab = gr_gab.drop(index=[0, 1, 4, len(gr_gab)-1], columns=['개표상황(투표구별)'])

gr_gab_member_df = gr_gab.loc[3]
gr_gab_member_df = gr_gab_member_df.dropna()


gr_gab_member_list = list()

for i in list(gr_gab_member_df):
  if '\n' in i:
    temp_text = i.split('\n')
    if temp_text[0]:
      gr_gab_member_list.append(temp_text[0])

  if '계' in i:
    gr_gab_member_list.append('계')

gr_gab_column_pre = gr_gab.loc[2]

gr_gab_column_pre = gr_gab_column_pre.drop(gr_gab_column_pre.tail(2).index)

gr_gab_column_pre = gr_gab_column_pre.dropna()

gr_gab_column = pd.concat([gr_gab_column_pre, pd.DataFrame(gr_gab_member_list)])

# gr_gab.columns[0][0:len(gr_gab_column)]  = list(gr_gab_column[0])

# print(list(gr_gab_column[0]))

gr_gab = gr_gab.drop(index=[2, 3])

print(gr_gab.head)

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