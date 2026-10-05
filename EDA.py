import pandas as pd

df = pd.read_csv("customer_shopping_behavior_cleaned.csv")

import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูล
df = pd.read_csv("customer_shopping_behavior_cleaned.csv")

# ดูข้อมูลเพศ
print(df["Gender"].value_counts())

# ดูหมวดสินค้า
print(df["Category"].value_counts())

# กราฟ
df["Category"].value_counts().plot(kind="bar")
plt.show()

print(df["Gender"].value_counts())
import matplotlib.pyplot as plt

df["Gender"].value_counts().plot(
    kind="bar",
    color=["skyblue", "pink"]
)

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

print(df["Category"].value_counts())
df["Category"].value_counts().plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

df["Age"].hist(
    bins=10,
    edgecolor="black"
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
df["Payment Method"].value_counts().plot(
    kind="bar"
)

plt.title("Payment Method")
plt.show()

print(df["Purchase Amount (₹)"].describe())