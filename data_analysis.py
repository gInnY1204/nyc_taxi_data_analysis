import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import folium

#################################################################################################
#데이터 불러오기(한번에)
#################################################################################################
# file_paths = glob.glob('./nyc_taxi/*.csv')
#
# dataframes = []
#
# for file in file_paths:
#     df = pd.read_csv(file)
#     dataframes.append(df)
#
# data = pd.concat(dataframes, ignore_index=True)
# print("data.head(): ", data.head())
# print("data.shape: ",data.shape)
# print("data.info(): ",data.info())

#################################################################################################
#데이터 불러오기(2015-01)
#################################################################################################
# CSV 파일 로드
data = pd.read_csv("./nyc_taxi/yellow_tripdata_2015-01.csv")  # 파일 이름은 실제 파일명으로 변경
print(data.head())  # 데이터의 첫 5개 행 출력
print(data.info())  # 데이터 요약 정보 출력

print("data.head(): ", data.head())
print("data.shape: ",data.shape)
print("data.info(): ",data.info())

#################################################################################################
#데이터 탐색 : EDA - Exploratory Data Analysis
#################################################################################################
#기초 통계
print("data.describe(): ",data.describe())
#결측치 확인
print("data.isnull().sum(): ",data.isnull().sum())
#데이터 분포 확인

#Vendor ID
data['VendorID'].hist(bins=3, figsize=(7,5), color='#add8e6', edgecolor='white', linewidth=1)
plt.title('Vendor ID')
plt.xlabel('Type of Taxi dataset: CMT(1) or VeriFone Inc(2)')
plt.ylabel('The number of Taxi')
# 그래프 저장
plt.savefig('distribution_of_Vendor_id.png', dpi=300, bbox_inches='tight')
plt.show()

#tpep_pickup_datetime & dropoff_datetime
data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])

data['pick_date'] = data['tpep_pickup_datetime'].dt.date
data['dropoff_date'] = data['tpep_dropoff_datetime'].dt.date

# 날짜별 히스토그램 (빈도수 기준)
data['pick_date'].value_counts().sort_index().plot(kind='bar', figsize=(15, 10), color='#add8e6', edgecolor='white', linewidth=1)
plt.title('The date when the meter was engaged')
plt.xlabel('Date')
plt.ylabel('Number of Taxi')
plt.xticks(rotation=90) #xlabel 회전
# 그래프 저장
plt.savefig('distribution_of_pick_date.png', dpi=300, bbox_inches='tight')
plt.show()

# 날짜별 히스토그램 (빈도수 기준)
data['dropoff_date'].value_counts().sort_index().plot(kind='bar', figsize=(15, 10), color='#add8e6', edgecolor='white', linewidth=1)
plt.title('distribution_of_dropoff_date')
plt.xlabel('Date')
plt.ylabel('Number of Taxi')
plt.xticks(rotation=90) #xlabel 회전
# 그래프 저장
plt.savefig('distribution_of_dropoff_date.png', dpi=300, bbox_inches='tight')
plt.show()

#사용자 수
data['passenger_count'].hist(figsize=(10,7), color='#add8e6', edgecolor='white', linewidth=1)
plt.title('distribution of passenger_count')
plt.xlabel('The number of passengers')
plt.ylabel('Frequency')
# 그래프 저장
plt.savefig('distribution_of_passenger_count.png', dpi=300, bbox_inches='tight')
plt.show()

#trip distance
data['trip_distance'].hist(bins=range(0, 20, 1), figsize=(10,7), color='#add8e6', edgecolor='white', linewidth=1)
plt.title('Distribution of Trip Distance')
plt.xlabel('Trip Distance (miles)')
plt.ylabel('Frequency')
# 그래프 저장
plt.savefig('Distribution_of_Trip_Distance.png', dpi=300, bbox_inches='tight')
plt.show()

#Rate Code Id
data['RateCodeID'].hist(figsize=(10,7), color='#add8e6', edgecolor='white', linewidth=1)
plt.title('Distribution of RateCodeID')
plt.xlabel('RateCodeID')
plt.ylabel('Frequency')
# 그래프 저장
plt.savefig('Distribution_of_RateCodeID.png', dpi=300, bbox_inches='tight')
plt.show()

'''
store_and_fwd_flag는 뉴욕시 택시 데이터에서 여행 기록이 차량의 메모리에 일시적으로 저장되었는지 여부를 나타내는 플래그

Y: store and forward trip
여행 기록이 차량의 메모리에 저장되었다가, 나중에 공급자에게 전송되었음을 의미

N: not a store and forward trip
여행 기록이 실시간으로 공급자에게 전송되었음을 의미

'''
# 값 분포 계산
flag_counts = data['store_and_fwd_flag'].value_counts()

# 원그래프 시각화
colors = ['#add8e6', '#ffc0cb']  # 색상 지정
explode = (0.1, 0)  # 강조 (Y를 약간 분리)

plt.pie(flag_counts,
        labels=flag_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        explode=explode)

# 그래프 제목
plt.title('Store and Forward Flag Distribution')
# 그래프 저장
plt.savefig('store_and_fwd_flag_distribution.png', dpi=300, bbox_inches='tight')

plt.show()

#payment_type
data['payment_type'].hist(figsize=(10,7), color='#add8e6', edgecolor='white', linewidth=1)
plt.title('Distribution of payment_type')
plt.xlabel('payment_type')
plt.ylabel('Frequency')
# 그래프 저장
plt.savefig('Distribution_of_payment_type.png', dpi=300, bbox_inches='tight')
plt.show()

# fare_amount
data['fare_amount'].hist(bins=range(0, 65, 5), color='#add8e6', edgecolor='white', linewidth=1)
plt.title('Fare Amount Distribution')
plt.xlabel('Fare Amount ($)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Distribution_of_Fare_Amount.png', dpi=300, bbox_inches='tight')
plt.show()

# extra
data['extra'].hist(color='#add8e6', edgecolor='white', linewidth=1)
plt.title('extra Distribution')
plt.xlabel('extra ($)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Distribution_of_extra.png', dpi=300, bbox_inches='tight')
plt.show()

# mta_tax
data['mta_tax'].hist(color='#add8e6', edgecolor='white', linewidth=1)
plt.title('mta_tax Distribution')
plt.xlabel('mta_tax ($)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Distribution_of_mta_tax.png', dpi=300, bbox_inches='tight')
plt.show()

# tip amount
data['tip_amount'].hist(bins=range(0, 13, 1), color='#add8e6', edgecolor='white', linewidth=1)
plt.title('tip amount Distribution')
plt.xlabel('tip amount ($)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Distribution_of_tip_amount.png', dpi=300, bbox_inches='tight')
plt.show()

# tolls_amount
data['tolls_amount'].hist(bins=range(0, 8, 2), color='#add8e6', edgecolor='white', linewidth=1)
plt.title('tolls_amount Distribution')
plt.xlabel('tolls_amount ($)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Distribution_of_tolls_amount.png', dpi=300, bbox_inches='tight')
plt.show()

# improvement_charge
data['improvement_surcharge'].hist(color='#add8e6', edgecolor='white', linewidth=1)
plt.title('improvement_surcharge Distribution')
plt.xlabel('improvement_surcharge ($)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Distribution_of_improvement_surcharge.png', dpi=300, bbox_inches='tight')
plt.show()

# total_amount
data['total_amount'].hist(bins=range(0, 80, 5), color='#add8e6', edgecolor='white', linewidth=1)
plt.title('total_amount Distribution')
plt.xlabel('total_amount ($)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Distribution_of_total_amount.png', dpi=300, bbox_inches='tight')
plt.show()


#pickup_longitude & latitude

lat = 40.7388
lon = -73.9944

pickup_map = folium.Map(location=[lat, lon], zoom_start=12)

for _, row in data.head(50).iterrows():
    folium.Marker([row['pickup_latitude'], row['pickup_longitude']],
                  popup=f"Pickup Location",
                  icon=folium.Icon(color='blue')
                  ).add_to(pickup_map)

pickup_map.save("./nyc_taxi/pickup_map.html")

dropoff_map = folium.Map(location=[lat, lon], zoom_start=12)

for _, row in data.head(50).iterrows():
    folium.Marker([row['dropoff_latitude'], row['dropoff_longitude']],
                  popup=f"Dropoff Location",
                  icon=folium.Icon(color='red')
                  ).add_to(dropoff_map)

dropoff_map.save("./nyc_taxi/dropoff_map.html")

