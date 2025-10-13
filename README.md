# 🧪 Web Automation Project – POM (Page Object Model)

**Automated Form Submission Using Selenium, Python, and Page Object Model (POM)**  

This project automates filling and submitting a web form on [Test Automation Practice](https://testautomationpractice.blogspot.com/) using **Python Selenium WebDriver** with a **Page Object Model (POM) structure**.  

It demonstrates best practices in test automation, including **config-driven testing, reusable page objects, dropdowns, checkboxes, radio buttons, and screenshot capture**.  

---

## 🖥️ Project Description

The project is structured using **POM** to separate **page interactions** from **test logic**.  

- `pages/` folder contains **page classes** defining web elements and actions.  
- `tests/` folder contains **pytest test scripts** that call page methods.  
- `config/` folder stores `config.yaml` for test data and URLs.  
- `conftest.py` sets up **pytest fixtures** for WebDriver and config.  

This modular structure mimics real-world **corporate Python automation projects**.

---
## 📊 Page Object Model (POM) Structure & Test Flow

This diagram illustrates how the **test script**, **page objects**, and **browser interactions** work together:

```
        ┌──────────────────────────────────┐
        │   tests/test_form_submission.py  │
        │  (pytest test script)            │
        └─────────────┬────────────────────┘
                      │ uses
                      ▼
        ┌──────────────────────────────┐
        │       pages/form_page.py     │
        │  (FormPage class: locators   │
        │   and actions)               │
        └─────────────┬────────────────┘
                      │ inherits
                      ▼
        ┌────────────────────────────┐
        │       pages/base_page.py   │
        │  (BasePage class: generic  │
        │   reusable methods)        │
        └─────────────┬──────────────┘
                      │ interacts with
                      ▼
        ┌──────────────────────────────┐
        │       Selenium WebDriver     │
        │  (Browser automation engine) │
        └──────────────────────────────┘

```

**Flow Summary:**  
1. **Test script** loads **config.yaml** and initializes WebDriver fixture.  
2. **FormPage** exposes methods to fill fields, click buttons, handle alerts, and take screenshots.  
3. **BasePage** provides reusable Selenium methods (`click`, `type`, `scroll`, `select_dropdown`, `handle_alert`, `take_screenshot`).  
4. **Selenium WebDriver** executes all browser actions in Chrome.  
5. Test results are displayed via **pytest** and screenshots are saved in `screenshots/`.

---

## ⚡ Features

- Fill **text fields** (name, email, phone)  
- Select **radio buttons** and **checkboxes**  
- Handle **dropdown menus**  
- Select **dates** using date picker  
- Handle **browser alert pop-ups** (accept/dismiss)  
- Take **screenshots** for verification  
- Fully **config-driven** using `config.yaml`  
- **Reusable Page Object Model** for maintainable code  

---

## 🛠️ Technologies & Tools

- **Python 3.11**  
- **Selenium WebDriver**  
- **ChromeDriver**  
- **Pytest** (for test execution)  
- **VS Code** (development environment)  
- **Git & GitHub** (version control)  
- **PyYAML** (for reading configuration files)  

---

## 📂 Folder Structure & File Descriptions

```
Web_Automation_Project_POM/
│
├── pages/
│ ├── init.py # Makes pages folder a Python package
│ ├── base_page.py # BasePage class with reusable Selenium methods (click, type, scroll, select_dropdown, take_screenshot, handle_alert)
│ └── form_page.py # FormPage class representing the form page; defines locators and form-specific actions
│
├── tests/
│ ├── init.py
│ ├── test_form_submission.py # Pytest script: tests form submission using FormPage and config.yaml
│ └── conftest.py # Pytest fixtures: sets up WebDriver, loads config.yaml
│
├── config/
│ └── config.yaml # Stores URL, form data, and other configurable test settings
│
├── screenshots/ # Stores screenshots of submitted forms
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```


---

## 🚀 How to Run

**1. Clone the repository and navigate into the folder:**
```bash
git clone https://github.com/<your-username>/Web_Automation_Project_POM.git
cd Web_Automation_Project_POM

**2. Create a Python virtual environment and activate it:**
python -m venv .venv
# PowerShell
& ".\.venv\Scripts\Activate.ps1"
# or CMD
.venv\Scripts\activate.bat

**3. Install dependencies:**
pip install -r requirements.txt

**4. Run the automation test:**
pytest -v


## 🎯 Learning Outcomes

- Implement Page Object Model in Python
- Write config-driven tests using YAML
- Handle browser interactions including alerts, checkboxes, radio buttons, dropdowns, and dates
- Take screenshots for verification
- Use pytest fixtures for reusable setup and teardown
- Prepare Python automation code following corporate best practices

## 👤 Author

**Abhijeet Singh**
- LinkedIn: https://www.linkedin.com/in/abhijeetsingh95
- GitHub: https://github.com/95abhijeet