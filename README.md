# 💰 Expense Monitor

A full-stack **expense management web application** built with **Python, Django, and MySQL** that helps users manage their daily expenses, organize spending into categories, set monthly budgets, analyze spending patterns, and export expense reports.

The application provides a centralized dashboard with spending summaries, recent transactions, budget information, and visual analytics through interactive charts.

---

## 🚀 Features

### 🔐 User Authentication

* User registration
* User login and logout
* Django authentication system
* Protected application pages
* Session-based user authentication

### 🗂️ Category Management

* Create expense categories
* View all categories
* Update existing categories
* Delete categories

### 💸 Expense Management

* Add daily expenses
* View expense history
* Update expenses
* Delete expenses
* Search expenses by description
* Filter expenses by category
* Filter expenses by date
* Sort expenses by amount

### 📊 Dashboard & Analytics

* Total spending summary
* Recent expenses
* Category-wise spending analysis
* Monthly spending overview
* Interactive bar charts
* Interactive pie charts
* Budget utilization information

### 💰 Budget Management

* Set monthly budgets for categories
* View budget limits
* Monitor spending against budgets
* Generate budget reports

### 📄 Report Export

* Export expense reports as **PDF**
* Export expense reports as **Excel**
* Generate structured expense data for reporting

### 🔔 User Feedback

* Success messages
* Error messages
* Form validation feedback

---

## 🛠️ Technologies Used

| Technology     | Purpose                   |
| -------------- | ------------------------- |
| **Python**     | Backend programming       |
| **Django**     | Web framework             |
| **MySQL**      | Relational database       |
| **HTML5**      | Web page structure        |
| **CSS3**       | Styling                   |
| **Bootstrap**  | Responsive UI             |
| **JavaScript** | Client-side functionality |
| **Chart.js**   | Data visualization        |
| **ReportLab**  | PDF generation            |
| **OpenPyXL**   | Excel report generation   |

---

## 🏗️ Project Architecture

The application follows Django's **Model-View-Template (MVT)** architecture.

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Django Views      │
                    │ Authentication      │
                    │ Expenses            │
                    │ Categories          │
                    │ Budgets             │
                    │ Reports             │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │ Django Templates│        │ Django Models   │
        │ HTML/CSS/JS     │        │ ORM             │
        └─────────────────┘        └────────┬────────┘
                                             │
                                             ▼
                                    ┌─────────────────┐
                                    │      MySQL      │
                                    │    Database     │
                                    └─────────────────┘
```

---

## 📦 Project Modules

The application is divided into the following major modules:

### 1. User Authentication

Handles:

* User registration
* Login
* Logout
* Authentication
* Protected pages

### 2. Category Management

Handles:

* Category creation
* Category listing
* Category updates
* Category deletion

### 3. Expense Management

Handles:

* Expense creation
* Expense listing
* Expense updates
* Expense deletion
* Searching
* Filtering
* Sorting

### 4. Budget Management

Handles:

* Monthly budget creation
* Category-wise budget limits
* Budget tracking
* Budget utilization

### 5. Budget Reports

Provides:

* Budget limits
* Actual spending
* Budget utilization
* Category-wise comparisons

### 6. Dashboard & Analytics

Provides:

* Spending summaries
* Recent expenses
* Category-wise analysis
* Visual charts

### 7. Report Export

Supports:

* PDF expense reports
* Excel expense reports

---

# 🗄️ Database Design

The project uses **MySQL** as the relational database and Django ORM for database operations.

## Category

Stores information about expense categories.

| Field  | Description   |
| ------ | ------------- |
| `id`   | Primary key   |
| `name` | Category name |

Example categories:

```text
Food
Travel
Shopping
Entertainment
Education
Bills
Healthcare
```

---

## Expense

Stores individual expense records.

| Field          | Description                 |
| -------------- | --------------------------- |
| `id`           | Primary key                 |
| `category`     | Associated expense category |
| `amount`       | Expense amount              |
| `description`  | Expense description         |
| `expense_date` | Date of expense             |
| `created_at`   | Record creation timestamp   |

---

## Budget

Stores monthly budget limits for categories.

| Field           | Description            |
| --------------- | ---------------------- |
| `id`            | Primary key            |
| `category`      | Associated category    |
| `monthly_limit` | Monthly spending limit |

---

# 📁 Project Structure

A typical project structure is:

```text
Smart-Expense-Tracker/
│
├── ExpenseTracker/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── expenses.html
│   ├── categories.html
│   ├── budgets.html
│   └── reports.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── manage.py
├── requirements.txt
└── README.md
```

> The exact structure may vary depending on the Django app organization used in the repository.

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/gubbalasaimani/Smart-Expense-Tracker.git
```

---

## 2. Navigate to the Project Directory

```bash
cd Smart-Expense-Tracker
```

---

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate the Virtual Environment

### Windows CMD

```bash
venv\Scripts\activate
```

### Windows PowerShell

```bash
venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ MySQL Database Configuration

Make sure **MySQL Server** is installed and running.

Create a database:

```sql
CREATE DATABASE expense_tracker;
```

Open:

```text
ExpenseTracker/settings.py
```

Configure the database settings according to your local MySQL configuration.

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'expense_tracker',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

> Replace `your_password` with your MySQL password.

---

# 🔄 Run Database Migrations

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

---

# 👤 Create an Admin User

Create a Django superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter:

```text
Username
Email
Password
```

---

# ▶️ Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

# 📊 Application Workflow

```text
User Registration
       │
       ▼
     Login
       │
       ▼
   Dashboard
       │
       ├───────────────┐
       ▼               ▼
 Categories         Expenses
       │               │
       │               ├── Add Expense
       │               ├── Update Expense
       │               ├── Delete Expense
       │               ├── Search
       │               ├── Filter
       │               └── Sort
       │
       ▼
    Budgets
       │
       ▼
 Budget Analysis
       │
       ▼
 Reports & Analytics
       │
       ├── PDF Export
       └── Excel Export
```

---

# 📈 Analytics

The dashboard uses **Chart.js** to provide visual insights into spending.

### Pie Chart

Used for:

```text
Category-wise Expense Distribution
```

Example:

```text
Food          → 30%
Travel        → 20%
Shopping      → 25%
Entertainment → 15%
Others        → 10%
```

### Bar Chart

Used to visualize spending amounts across categories or time periods.

---

# 📄 Report Generation

The application supports two export formats.

### PDF

PDF reports are generated using:

```text
ReportLab
```

The generated report can contain:

* Expense details
* Categories
* Amounts
* Dates
* Descriptions
* Expense summaries

### Excel

Excel reports are generated using:

```text
OpenPyXL
```

This allows users to download and further analyze their expense data in Microsoft Excel or compatible spreadsheet applications.

---

# 🔒 Security

The application uses Django's built-in security and authentication mechanisms, including:

* Django authentication
* Session management
* CSRF protection
* Password hashing
* Authentication-based page protection
* Django ORM for database interaction

---

# 🔮 Future Enhancements

The following features can be added in future versions:

* [ ] User-specific expenses, categories, and budgets
* [ ] Password reset functionality
* [ ] Budget limit notifications
* [ ] Monthly and yearly reports
* [ ] Expense receipt image upload
* [ ] Advanced spending analytics
* [ ] Django REST Framework API
* [ ] Mobile application
* [ ] Machine learning-based expense prediction
* [ ] Recurring expenses
* [ ] Email notifications
* [ ] Multiple currency support
* [ ] Dark mode
* [ ] Interactive financial insights

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Python web development
* Django framework
* Django MVT architecture
* Django ORM
* MySQL database integration
* CRUD operations
* User authentication
* Form handling
* Database relationships
* Filtering and searching
* Data visualization
* PDF generation
* Excel automation
* Responsive web design
* Backend and frontend integration

---

# 👨‍💻 Developer

**Hrishi Suhas Dahake**

B.E – Computer Science and Engineering

---

# 📌 Project Status

**Completed and Tested**

---

## ⭐ Contributing

Contributions are welcome.

To contribute:

```bash
# Fork the repository

# Create a new branch
git checkout -b feature/your-feature

# Make your changes

# Commit your changes
git commit -m "Add new feature"

# Push the branch
git push origin feature/your-feature
```

Then create a Pull Request.

---

## 📜 License

This project is intended for educational and development purposes.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Repository:**

