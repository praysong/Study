# #######하나의 엑셀파일을 csv로 변환
# import pandas as pd

# # 엑셀 파일 경로
# excel_file_path = "c:/_data/mini/sdf/버스 8월.xlsx"

# # CSV 파일 경로 (저장할 파일명과 경로)
# csv_file_path = "c:/_data/mini/버스8월.csv"

# # 엑셀 파일을 pandas DataFrame으로 읽기
# df = pd.read_excel(excel_file_path)

# # CSV 파일로 저장
# df.to_csv(csv_file_path)  # index=False로 설정하여 인덱스를 CSV 파일에 포함시키지 않음



# ### 여러개의 엑셀파일 하나의 csv로 변환
# import pandas as pd
# import glob

# # 엑셀 파일이 있는 디렉토리 경로
# excel_files_path = "c:/_data/mini/sdf/*.xlsx"  # '*.xlsx'는 해당 디렉토리의 모든 엑셀 파일을 의미

# # CSV 파일 경로 (저장할 파일명과 경로)
# csv_file_path = "c:/_data/mini/2023년 1~8월 이용인원.csv"

# # 모든 엑셀 파일 경로 가져오기
# excel_file_paths = glob.glob(excel_files_path)

# # 모든 엑셀 파일을 하나의 데이터프레임으로 결합
# dfs = []
# for file_path in excel_file_paths:
#     dfs.append(pd.read_excel(file_path))

# # 데이터프레임을 합치기
# combined_df = pd.concat(dfs, ignore_index=True)

# # CSV 파일로 저장
# combined_df.to_csv(csv_file_path, index=False)  # index=False로 설정하여 인덱스를 CSV 파일에 포함시키지 않음


#### 여러개의 csv를 하나의 csv로
import pandas as pd
import glob

# 합칠 CSV 파일들의 경로
file_paths = glob.glob("c:/_data/mini/fff/*.csv")

# 모든 CSV 파일을 하나의 데이터프레임으로 결합
dfs = []
for file_path in file_paths:
    df = pd.read_csv(file_path
                     #,encoding="EUC-KR"
                     )
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

# 결합된 데이터프레임을 CSV 파일로 저장
combined_df.to_csv("c:/_data/mini/2023년1~8월 일별 버스 이용객수.csv", index=False)

# # # '열이름' 열을 기준으로 오름차순으로 정렬
# # 버스 = df.sort_values(by=['년(YEAR)','월(MONTH)','일(DAY)','시간(HOUR)','분_30분단위(HALF_HOUR)'], ascending=False)

