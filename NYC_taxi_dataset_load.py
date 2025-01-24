import shutil
import os
import kagglehub

# Kaggle dataset 다운로드
path = kagglehub.dataset_download("elemento/nyc-yellow-taxi-trip-data")
print("Path to dataset files:", path)

# 데이터를 저장할 경로 설정
save_directory = "./nyc_taxi"  # 원하는 저장 경로
os.makedirs(save_directory, exist_ok=True)  # 디렉토리 생성

# 다운로드된 파일을 저장 경로로 복사
for file_name in os.listdir(path):
    source_file = os.path.join(path, file_name)
    destination_file = os.path.join(save_directory, file_name)
    shutil.copy(source_file, destination_file)

print(f"Dataset has been saved to: {save_directory}")
