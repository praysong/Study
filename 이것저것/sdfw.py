import pandas as pd

# CSV 파일 읽기
path = pd.read_csv("c:/_data/mini/2023년1~8월 일별 버스 이용객수.csv")
path['승차총승객수'] = path['승차총승객수'].astype(int)
path['하차총승객수'] = path['하차총승객수'].astype(int)
print(path.head())
path.to_csv("c:/_data/mini/2023년1~8월 일별 버스 이용객수2.csv")