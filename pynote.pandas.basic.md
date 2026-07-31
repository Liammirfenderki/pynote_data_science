
## Read / Write Data

### CSV and Excel

```python
df = pd.read_csv("data.csv")               # read
df.to_csv("data_out.csv", index=False)     # write

df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
df.to_excel("data_out.xlsx", index=False)

df = pd.read_parquet("data.parquet")
df.to_parquet("data_out.parquet")

```

## Create DataFrame

### From dict

```python
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["Tehran", "Shiraz", "Tabriz"],
}

df = pd.DataFrame(data)
```

### From list of dicts

```python
rows = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
]

df = pd.DataFrame(rows)
```

---

## Inspect Data

```python
df.head()          # first 5 rows
df.head(10)       # first 10 rows
df.tail()         # last 5 rows
df.info()         # dtypes + nulls
df.describe()     # numeric summary
df.shape          # (rows, columns)
df.columns        # column names
```

---

## Select Columns & Rows

### Column(s)

```python
df["age"]             # one column (Series)
df[["name", "age"]]   # multiple columns (DataFrame)
```

### Rows by position (`iloc`)

```python
df.iloc[0]        # first row
df.iloc[0:5]      # rows 0–4
```

### Rows by label (`loc`)

```python
df.loc[0]                 # row with index label 0
df.loc[0:10, ["name"]]    # rows 0–10, only "name"
```

---

## Filter (Boolean Indexing)

```python
young = df[df["age"] < 30]

tehran_or_shiraz = df[df["city"].isin(["Tehran", "Shiraz"])]

no_null_age = df[df["age"].notna()]
```

Multiple conditions:

```python
mask = (df["age"] > 20) & (df["city"] == "Tehran")
df_filtered = df[mask]
```

---

## Add / Modify Columns

```python
df["age_plus_10"] = df["age"] + 10

df["age_group"] = df["age"].apply(
    lambda x: "young" if x < 30 else "old"
)
```

Vectorized operations:

```python
df["bmi"] = df["weight_kg"] / (df["height_m"] ** 2)
```

---

## Drop Columns / Rows

```python
df_no_age = df.drop(columns=["age"])

df_no_first_row = df.drop(index=0)
```

In‑place:

```python
df.drop(columns=["age"], inplace=True)
```

---

## Handle Missing Values

```python
df.isna().sum()              # count nulls per column

df_filled = df.fillna(0)     # fill all nulls with 0

df["age"] = df["age"].fillna(df["age"].mean())  # per column

df_clean = df.dropna()       # drop rows with any null
```

---

## Sort

```python
df_sorted = df.sort_values("age")  # ascending

df_sorted_desc = df.sort_values("age", ascending=False)

df_sorted_multi = df.sort_values(
    ["city", "age"], ascending=[True, False]
)
```

---

## GroupBy & Aggregation

```python
grouped = df.groupby("city")["age"].mean()
# Series: mean age per city

agg_df = df.groupby("city").agg({
    "age": ["mean", "max", "count"],
    "salary": "sum",
})
```

Reset index:

```python
agg_df = agg_df.reset_index()
```

---

## Rename Columns

```python
df_renamed = df.rename(
    columns={"name": "Name", "age": "Age"}
)
```

---

## Change Data Types

```python
df["age"] = df["age"].astype(int)
df["date"] = pd.to_datetime(df["date"])
```

---

## Merge / Join

```python
merged = pd.merge(
    df_users, df_orders,
    on="user_id",
    how="inner"       # "left", "right", "outer"
)
```

---

## Concatenate

```python
combined = pd.concat([df1, df2], axis=0)   # stack rows
wide     = pd.concat([df1, df2], axis=1)   # add columns
```

---

## Pivot Table

```python
pivot = pd.pivot_table(
    df,
    values="salary",
    index="city",
    columns="gender",
    aggfunc="mean",
)
```

---

## Apply on Rows / Columns

```python
# column-wise
df["age_sq"] = df["age"].apply(lambda x: x ** 2)

# row-wise
def full_name(row):
    return f"{row['first']} {row['last']}"

df["full_name"] = df.apply(full_name, axis=1)
```

---

## Simple Plot (if using matplotlib)

```python
import matplotlib.pyplot as plt

df["age"].hist()
plt.show()

df.plot(x="age", y="salary", kind="scatter")
plt.show()
```

---

## Index Operations

```python
df = df.set_index("id")   # set index to column "id"
df = df.reset_index()     # back to default integer index
```

---

## Quick Pattern: Clean + Analyze

```python
import pandas as pd

df = pd.read_csv("data.csv")

# basic cleaning
df = df.drop_duplicates()
df = df.dropna(subset=["age"])
df["age"] = df["age"].astype(int)

# simple stats
print(df["age"].describe())
print(df.groupby("city")["age"].mean())
```

---

If you want, I can also make:
- an **ultra‑minimal version** (10 lines only)  
- a **bioinformatics‑oriented version** (CSV, TSV, big files, memory tricks) tailored to your genomics workflows.
[[pynote.pandas.1]]