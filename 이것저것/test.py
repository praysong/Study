# import pandas as pd
# path = "c:/_data/mini/"
# df = pd.read_csv(path+"2023년1~8월 버스 이용객수.csv")
# # df = df.iloc[0:100,:]

# # print(df.describe())
# # print(df)
# # df = df.describe()
# df['사용년월'] = df['사용년월'].astype(str)

# df = df.drop(['노선번호','노선명','표준버스정류장ID','버스정류장ARS번호','역명','00시승차총승객수','00시하차총승객수','1시승차총승객수',
#               '1시하차총승객수','2시승차총승객수','2시하차총승객수','3시승차총승객수','3시하차총승객수','4시승차총승객수','4시하차총승객수','5시승차총승객수',
#               '5시하차총승객수','6시승차총승객수','6시하차총승객수','23시승차총승객수','23시하차총승객수','교통수단타입코드','교통수단타입명','등록일자'],axis=1)

# # '컬럼명' 열에서 '원하는단어'를 포함하는 행 선택
# selected_rows = df[df['사용년월'].str.contains('20230101')]
# selected_rows = df[df['사용년월'].str.contains('20230102')]
# selected_rows = df[df['사용년월'].str.contains('20230103')]
# selected_rows = df[df['사용년월'].str.contains('20230104')]
# selected_rows = df[df['사용년월'].str.contains('20230105')]
# selected_rows = df[df['사용년월'].str.contains('20230106')]
# selected_rows = df[df['사용년월'].str.contains('20230107')]
# selected_rows = df[df['사용년월'].str.contains('20230108')]
# # print(selected_rows)
# # 선택한 행들을 합침
# combined_row = selected_rows.sum().T

# print("원하는 단어가 들어간 행을 합친 결과:", combined_row)
# combined_row_transposed = pd.DataFrame(combined_row).transpose()
# combined_row_transposed.to_csv(path + "8월.csv")

# import pandas as pd
# import calendar
# path = "c:/_data/mini/"
# df = pd.read_csv(path + "버스 데이터 많음.csv",encoding='EUC-KR')
# df['사용일자'] = df['사용일자'].astype(str)

# df = df.drop(["노선번호","노선명","표준버스정류장ID","버스정류장ARS번호","역명","등록일자"], axis=1)

# # 일별로 선택한 행을 저장할 리스트
# daily_combined_rows = []

# # 각 월별 일 수를 고려하여 일별로 선택하고 합침
# for month in range(1, 9):
#     # 각 월의 일수를 가져옴
#     num_days_in_month = calendar.monthrange(2023, month)[1]
#     for day in range(1, num_days_in_month + 1):
#         selected_rows = df[df['사용일자'].str.contains(f'202301{day:02d}')]  # 일별로 선택
#         combined_row = selected_rows.sum().T  # 선택한 행들을 합침
#         daily_combined_rows.append(combined_row)
# combined_row_transposed = pd.DataFrame(combined_row).transpose()
# # 리스트에 있는 DataFrame들을 합쳐서 최종 결과를 얻음
# result = pd.concat(daily_combined_rows)
# # 결과를 CSV 파일로 저장
# result.to_csv(path + "1월_일별_결과.csv")
# print("결과를 저장했습니다.")

import pandas as pdccc
import calendar
path = "c:/_data/mini/"
df = pd.read_csv(path + "1월_일별_결과.csv")
# df = pd.DataFrame(df).transpose()
df = df[1:]
df.to_csv(path + "aaa.csv")

print(df)