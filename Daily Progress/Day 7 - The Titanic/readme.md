# Titanic Data Analysis – Summary & Key Takeaways

---

## 🔧 Data Prep

- Data was taken from [Kaggle - Titanic - Machine Learning from Disaster](<https://www.kaggle.com/competitions/titanic/data>)
- Dropped unnecessary columns like `PassengerId`, `Ticket`, and `Cabin` (too empty or just not useful).
- Filled missing `Age` values with the average and used the most common value for missing `Embarked` entries.
- Converted `Sex` and `Embarked` into numbers so plots and models can understand them.
- Extracted passengers' first names (just for fun or future use).

---

## 📈 Visual Insights

### 1. **How many survived?**

- Around **one-third** survived, and **two-thirds** didn’t.
- Not surprising given the chaos during the disaster, but still hits hard when visualized.

### 2. **Survival by Gender**

- **Women had a much better chance of survival** than men.
- Seems like “ladies first” was followed seriously here.

### 3. **Age Distribution – Survivors vs Non-Survivors**

- Kids under 10 had slightly better odds.
- A lot of people aged 20–40 didn’t make it.
- Elderly passengers also had low survival — maybe due to slower mobility during evacuation?

### 4. **Did paying more help? (Fare vs Survival)**

- Yep. People who paid more were more likely to survive.
- Higher fare = usually 1st class = more access to lifeboats and help.
- A few high-paying passengers didn’t survive, though — outliers exist.

### 5. **Survival by Class**

- 1st class had the highest survival rate by far.
- 3rd class had the lowest — unfortunately, privilege was literally life-saving here.

### 6. **Where people boarded from (Heatmap)**

- Most survivors were from **1st class** regardless of where they boarded, but interesting patterns show up per port.
- Slightly more survivors boarded from Cherbourg (`C`), which had more wealthy passengers.

### 7. **Family Matters? (Siblings/Spouses)**

- Passengers with **0–1 siblings/spouses** had better odds.
- Those with large families aboard had lower survival — maybe harder to coordinate during panic?

---

## 🧠 Final Thoughts

The Titanic dataset really shows how **age**, **gender**, **class**, and even **ticket price** affected someone's chance of survival. It’s a mix of social class differences, emergency response, and pure luck — but analyzing it like this helps us understand the human stories behind the numbers.
