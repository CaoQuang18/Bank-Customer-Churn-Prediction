import pandas as pd

# Đọc file
df = pd.read_csv("data/bank.csv")   # đổi tên file CSV của bạn

print("📌 Dữ liệu ban đầu:")
print(df.head())
print(df.info())
print("===================================")

# =====================================================
# 1. XOÁ DỮ LIỆU TRÙNG
# =====================================================
df.drop_duplicates(inplace=True)

# =====================================================
# 2. CHUẨN HOÁ TÊN CỘT (lowercase + không dấu cách)
# =====================================================
df.columns = df.columns.str.lower().str.replace(" ", "_")

# =====================================================
# 3. CHUYỂN KIỂU DỮ LIỆU PHÙ HỢP (nếu cần)
# =====================================================
df["gender"] = df["gender"].astype("category")
df["country"] = df["country"].astype("category")
df["churn"] = df["churn"].astype(int)

# =====================================================
# 4. PHÁT HIỆN OUTLIERS CHO CÁC CỘT SỐ (IQR)
# =====================================================
num_cols = ["credit_score", "age", "tenure", "balance",
            "products_number", "estimated_salary"]

Q1 = df[num_cols].quantile(0.25)
Q3 = df[num_cols].quantile(0.75)
IQR = Q3 - Q1

outlier_condition = (
    (df[num_cols] < (Q1 - 1.5 * IQR)) |
    (df[num_cols] > (Q3 + 1.5 * IQR))
).any(axis=1)

df = df[~outlier_condition]

# =====================================================
# 5. LƯU FILE LÀM SẠCH
# =====================================================
df.to_csv("data/newbank.csv", index=False)

print("🎉 Làm sạch xong! File mới: newbank.csv")
print(df.head())
