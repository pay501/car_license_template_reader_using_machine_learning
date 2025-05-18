
import pandas as pd
from datetime import datetime

# 1. โหลด whitelist
whitelist_df = pd.read_csv('./database/white_list.csv')

# 2. ฟังก์ชันตรวจสอบป้ายทะเบียน
def check_access(predicted_plate):
  # ตรวจสอบว่าทะเบียนอยู่ใน whitelist หรือไม่
  if predicted_plate in whitelist_df['license_plate'].values:
      return "allowed"
  else:
      return "denied"

# 3. ฟังก์ชันบันทึก log
def log_entry(plate, status):
  # สร้างข้อมูล log ใหม่
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  new_log = pd.DataFrame([[timestamp, status, plate]], columns=["timestamp", "status", "license_plate"])
  
  # เพิ่มลงไฟล์ log.csv (append)
  try:
      existing_log = pd.read_csv("./database/log.csv")
      updated_log = pd.concat([existing_log, new_log], ignore_index=True)
  except FileNotFoundError:
      updated_log = new_log
  
  updated_log.to_csv("./database/log.csv", index=False)
  #print(f"LOGGED: {timestamp}, {status}, {plate}")


