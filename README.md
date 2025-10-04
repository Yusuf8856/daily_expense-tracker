# 💰 Expense Tracker

A **personal expense tracker** built with **Django** to manage, track, and analyze your expenses efficiently.  
Users can **add, update, delete, and view expenses**, categorize them, and see visual summaries.

---

### Core Features
- Add expense (amount, date, note, category)
- View all expenses
- Update and delete expenses
- Save data in SQLite (or database)
- Basic validation & error handling

### Optional Features
- Expense categories (e.g., Food, Travel, Bills)
- Summary reports:
  - Total spent
  - Group by category
  - Group by month
- Filters by date or category
- Responsive, modern UI using Bootstrap
- Charts using Chart.js

---

## Tools & Technologies

- **Backend:** Django 4.x  
- **Database:** SQLite (default)  
- **Frontend:** HTML, CSS, Bootstrap 5, Chart.js  
- **Editor:** VS Code (optional)  
- **Version Control:** Git & GitHub  

---

### **Sample Inputs & Outputs**

#### **Add Expense**
| Field    | Input           |
|----------|----------------|
| Date     | 2025-10-04      |
| Amount   | 500             |
| Category | Food            |
| Note     | Grocery shopping|

**Output:** Dashboard shows the new expense and updates total spending.

---

#### **View Expenses**
| Date       | Amount | Category | Note              |
|------------|--------|----------|-----------------|
| 2025-10-04 | 500    | Food     | Grocery shopping|
| 2025-10-03 | 200    | Travel   | Cab fare        |

---

#### **Charts**
- **Category Chart:** Pie chart of total spending by category  
- **Monthly Chart:** Bar chart of expenses per month  

---

## Screenshots

<!-- Add screenshots in `screenshots/` folder -->
![Dashboard](screenshots/dashboard.png)  
![Add Expense](screenshots/add_expense.png)  
![Charts](screenshots/charts.png)

---

## Installation

```bash
git clone https://github.com/Yusuf8856/daily_expense-tracker.git
cd expense-tracker
python -m venv env
# Activate environment
# Windows: env\Scripts\activate
# macOS/Linux: source env/bin/activate
python manage.py migrate
python manage.py runserver
