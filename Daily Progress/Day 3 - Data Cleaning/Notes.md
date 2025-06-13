
# 🧼 Handling Missing Data in Pandas

I refered Kaggle's Data cleaning Course too - (<https://www.kaggle.com/learn/data-cleaning>)

## 📌 1. `fillna()` – Fill Missing Values

Fills `NaN` values with a specified value, method, or strategy.

### 🔧 Key Parameters

| Parameter     | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `value`       | Scalar, dict, Series, or DataFrame used to replace NaNs                    |
| `method`      | `'ffill'` (forward fill) or `'bfill'` (backward fill)                       |
| `axis`        | `0` for column-wise (default), `1` for row-wise                             |
| `inplace`     | If `True`, changes are made directly on the object                          |
| `limit`       | Max number of consecutive NaNs to fill                                      |

### ✅ Examples

```python
# Fill NaNs with 0
df.fillna(0)

# Forward fill
df.fillna(method='ffill')

# Backward fill
df.fillna(method='bfill')

# Fill using a dictionary (column-wise)
df.fillna({'col1': 0, 'col2': 99})

# In-place fill
df.fillna(0, inplace=True)
```

## 📌 2. `dropna()` – Drop Rows or Columns with Missing Data

### 🔧 Key Parameters for `dropna()`

| Parameter | Description                                                    |
| --------- | -------------------------------------------------------------- |
| `axis`    | `0` = drop rows, `1` = drop columns                            |
| `how`     | `'any'` = drop if *any* NaN; `'all'` = drop only if *all* NaNs |
| `thresh`  | Require a minimum number of non-NaN values to keep             |
| `subset`  | Subset of columns to check                                     |
| `inplace` | Modifies the DataFrame directly                                |

### ✅ Examples for `dropna()`

```python
# Drop rows with any NaN
df.dropna()

# Drop columns with all NaNs
df.dropna(axis=1, how='all')

# Drop rows with < 3 non-NaN values
df.dropna(thresh=3)
```

---

## 📌 3. `isna()` / `isnull()` – Check for NaNs

Returns a DataFrame of boolean values showing where `NaN`s are.

```python
df.isna()       # same as df.isnull()
```

## 📌 4. `notna()` / `notnull()` – Opposite of `isna()`

Returns `True` for non-NaN values.

```python
df.notna()      # same as df.notnull()
```

---

## 🧠 Real Example

```python
# Fill backward, then remaining NaNs with 0
subset_nfl_data.fillna(method='bfill', axis=0).fillna(0)
```

* First fills NaNs with the next available value in the column (`bfill`)
* Then fills any still-missing values with `0`

---

Gotcha Dart 😎 — here’s the clean, no-markdown version you can read or paste wherever:

---

## 🔡 What’s Encoding and Decoding?

### ✅ Encoding

It’s the process of converting a **string** (text) into **bytes** so a computer can store or transmit it.

Example:

```python
"hello".encode('utf-8')  
# Output: b'hello'
```

### ✅ Decoding

This is the reverse: converting **bytes** back into a human-readable **string**.

Example:

```python
b'hello'.decode('utf-8')  
# Output: "hello"
```

---

### 🧠 What is UTF-8?

* It’s the most popular encoding on the web.
* Can represent **every Unicode character** (like emojis, foreign scripts, etc.).
* It’s variable-length (1 to 4 bytes per character).
* Used by default in most tools and APIs.

---

### 🧩 Common Encodings

| Encoding  | What it supports                       |
| --------- | -------------------------------------- |
| `utf-8`   | All characters, emoji, universal       |
| `ascii`   | Only English characters (0–127)        |
| `utf-16`  | Unicode using 2 or 4 bytes per char    |
| `latin-1` | Western Europe characters (1 byte)     |
| `cp1252`  | Windows encoding, extension of latin-1 |

---

### ⚙️ String `encode()` – Attributes

```python
string.encode(encoding='utf-8', errors='strict')
```

* `encoding`: `'utf-8'`, `'ascii'`, `'latin-1'`, etc.
* `errors`: What to do if it finds a character it can’t encode

| Option               | Meaning                          |
| -------------------- | -------------------------------- |
| `'strict'`           | (default) Raise error            |
| `'ignore'`           | Skip the bad character           |
| `'replace'`          | Replace with `?`                 |
| `'backslashreplace'` | Replace with Unicode escape code |

Example:

```python
"café".encode('ascii', errors='replace')  # b'caf?'
```

---

### ⚙️ Bytes `decode()` – Attributes

```python
bytes.decode(encoding='utf-8', errors='strict')
```

Same as `encode()` but used to get strings back from bytes.

Example:

```python
b'caf\xc3\xa9'.decode('utf-8')  # "café"
```

---
