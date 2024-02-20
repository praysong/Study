# import pandas as pd
# import calendar
# path = "c:/_data/mini/"
# df = pd.read_csv(path + "버스 데이터 많음.csv",encoding='EUC-KR')
# df['사용일자'] = df['사용일자'].astype(str)

# # # df = df.iloc[0:100,:]

# # # print(df.describe())
# # # print(df)
# # # df = df.describe()
# # df['사용년월'] = df['사용년월'].astype(str)
# # df = df.drop_duplicates('사용일자')
# df = df.drop(["노선번호","노선명","표준버스정류장ID","버스정류장ARS번호","역명","등록일자"],axis=1)

# # '컬럼명' 열에서 '원하는단어'를 포함하는 행 선택
# selected_rows = df[df['사용일자'].str.contains('20230101')]
# # selected_rows = df[df['사용년월'].str.contains('20230102')]
# # selected_rows = df[df['사용년월'].str.contains('20230103')]
# # selected_rows = df[df['사용년월'].str.contains('20230104')]
# # selected_rows = df[df['사용년월'].str.contains('20230105')]
# # selected_rows = df[df['사용년월'].str.contains('20230106')]
# # selected_rows = df[df['사용년월'].str.contains('20230107')]
# # selected_rows = df[df['사용년월'].str.contains('20230108')]

# # # 선택한 행들을 합침
# # # selected_rows = selected_rows[0:1]
# combined_row = selected_rows.sum()
# combined_row = pd.DataFrame(combined_row).transpose()
# combined_row['사용일자'] = "20230101"

# print(combined_row)


# # print("원하는 단어가 들어간 행을 합친 결과:", combined_row)
# # combined_row_transposed = pd.DataFrame(combined_row).transpose()
# # combined_row_transposed.to_csv(path + "1월1일.csv")

# import pandas as pd
# import calendar
# path = "c:/_data/mini/"
# df = pd.read_csv(path + "버스 데이터 많음.csv",encoding='EUC-KR')
# df['사용일자'] = df['사용일자'].astype(str)
# df = df.drop_duplicates('사용일자')
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
# # 리스트에 있는 DataFrame들을 합쳐서 최종 결과를 얻음
# result = pd.concat(daily_combined_rows)
# # 결과를 CSV 파일로 저장
# result.to_csv(path + "1월_일별_결과.csv")
# print("결과를 저장했습니다.")


# import pandas as pd
# import calendar
# path = "c:/_data/mini/"
# df = pd.read_csv(path + "1월_일별_결과.csv")
# # df = pd.DataFrame(df).transpose()
# df = df[1:]
# df.to_csv(path + "aaa.csv")

# import pandas as pd
# import calendar

# path = "c:/_data/mini/"
# df = pd.read_csv(path + "버스 데이터 많음.csv", encoding='EUC-KR')
# df['사용일자'] = df['사용일자'].astype(str)
# df = df.drop_duplicates('사용일자')
# df = df.drop(["노선번호", "노선명", "표준버스정류장ID", "버스정류장ARS번호", "역명", "등록일자"], axis=1)

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

# # 리스트에 있는 DataFrame들을 합쳐서 최종 결과를 얻음
# result = pd.concat(daily_combined_rows, axis=1)

# # 결과를 CSV 파일로 저장
# result.to_csv(path + "1월_일별_결과.csv")
# print("결과를 저장했습니다.")

import pandas as pd
import calendar
from datetime import datetime, timedelta

import pandas as pd

path = "c:/_data/mini/"

# # 컬럼 이름 문자열
# columns_str = '사용일자,"노선번호","노선명","표준버스정류장ID","버스정류장ARS번호","역명","승차총승객수","하차총승객수","등록일자"'

# # CSV 파일을 읽을 때 컬럼 이름으로 사용하고자 하는 리스트로 설정하여 데이터프레임 생성
# df = pd.read_csv(path + "BUS_STATION_BOARDING_MONTH_202306.csv", encoding='EUC-KR', delimiter=';',
#                  names=columns_str.split(",")
#                  )
# # 필요없는 열 삭제
# df = df.drop(['"노선번호"', '"노선명"', '"표준버스정류장ID"', '"버스정류장ARS번호"', '"역명"','"등록일자"'], axis=1)
# # df = df[['사용일자']]

# print(df['사용일자'])
# # print(df.columns)
import pandas as pd
from datetime import datetime, timedelta

path = "c:/_data/mini/"

# CSV 파일을 읽을 때 컬럼 이름으로 사용하고자 하는 리스트로 설정하여 데이터프레임 생성
columns_str = '사용일자,"노선번호","노선명","표준버스정류장ID","버스정류장ARS번호","역명","승차총승객수","하차총승객수","등록일자"'
df = pd.read_csv(path + "BUS_STATION_BOARDING_MONTH_202306.csv", encoding='EUC-KR', delimiter=';', names=columns_str.split(','), dtype={'사용일자': str})
df = df.drop(['"노선번호"', '"노선명"', '"표준버스정류장ID"', '"버스정류장ARS번호"', '"역명"','"등록일자"'], axis=1)

# NaN 값이 있는 행 제거
df = df.dropna(subset=['사용일자'])

# '사용일자' 열의 이름을 "Date"로 변경
df = df.rename(columns={"사용일자": "Date"})

# 시작일과 종료일 설정
start_date = datetime(2023, 6, 27)
end_date = datetime(2023, 6, 30)

# 시작일부터 종료일까지의 모든 날짜 생성
dates_to_process = [(start_date + timedelta(days=i)).strftime('%Y%m%d') for i in range((end_date - start_date).days + 1)]

for date in dates_to_process:
    selected_rows = df[df['Date'].str.contains(date)]
    combined_row = selected_rows.sum()
    combined_row = pd.DataFrame(combined_row).transpose()
    combined_row['Date'] = date
    
    # CSV 파일로 저장
    combined_row.to_csv(path + f"fff/{date}_결과2.csv", index=False)

    print(f"{date} 결과를 저장했습니다.")
