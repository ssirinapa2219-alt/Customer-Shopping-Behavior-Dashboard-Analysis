import pandas as pd
import numpy as np

# โหลดข้อมูล
df = pd.read_csv(
    r"E:\Sirinapa\DataProject\customer_shopping_behavior-clean.csv"
)

# ---------------------------
# 1. ลบข้อมูลซ้ำ
# ---------------------------
df = df.drop_duplicates()

# ---------------------------
# 2. แปลงวันที่
# ---------------------------
df["Purchase Date"] = pd.to_datetime(
df["Purchase Date"],
errors="coerce"
)

# ---------------------------
# 3. จัดการ Missing Values
# ---------------------------
# ตัวเลข
numeric_cols = [
"Age",
"Quantity",
"Purchase Amount ()",
"Discount (%)",
"Shipping Charge ()",
"Delivery Time (Days)",
"Review Rating",
"Previous Purchases"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

# ข้อความ
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna("Unknown")

# ---------------------------
# 4. Clean ข้อความ
# ---------------------------
text_cols = df.select_dtypes(include="object").columns

for col in text_cols:
    df[col] = (
df[col]
.astype(str)
.str.strip()
)

# ---------------------------
# 5. แปลง Yes/No เป็น 1/0
# ---------------------------
binary_map = {
"Yes": 1,
"No": 0
}

binary_cols = [
"Subscription Status"
]

for col in binary_cols:
    if col in df.columns:
        df[col] = df[col].map(binary_map)

# Return Status
if "Return Status" in df.columns:
    df["Return Status"] = df["Return Status"].map({
"Returned": 1,
"Not Returned": 0
})

# ---------------------------
# 6. จัดการ Outliers ด้วย IQR
# ---------------------------
outlier_cols = [
"Age",
"Purchase Amount (₹)",
"Quantity",
"Review Rating"
]

for col in outlier_cols:
    if col in df.columns:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df[col] = np.where(
df[col] < lower,
lower,
np.where(df[col] > upper, upper, df[col])
)

# ---------------------------
# 7. สร้างฟีเจอร์เพิ่มเติม
# ---------------------------
df["Purchase_Year"] = df["Purchase Date"].dt.year
df["Purchase_Month"] = df["Purchase Date"].dt.month

# ---------------------------
# 8. ตรวจสอบผลลัพธ์
# ---------------------------
print(df.info())
print(df.isnull().sum())

# ---------------------------
# 9. บันทึกไฟล์ใหม่
# ---------------------------
df.to_csv(
"customer_shopping_behavior_cleaned.csv",
index=False
)

print("Data Cleaning Complete!")

print(df.info())
print(df.isnull().sum())

