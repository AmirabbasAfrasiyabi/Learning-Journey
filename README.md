# 🚀 Learning Journey - Programming Courses Portfolio

![Progress](https://img.shields.io/badge/Courses-4-blue)
![Languages](https://img.shields.io/badge/Languages-Python%20|%20Go%20|%20SQL%20|%20JavaScript-green)
![Status](https://img.shields.io/badge/Status-Active%20Learning-orange)

## 📖 About This Repository

This repository contains my projects, exercises, and notes from various programming courses I'm currently taking. My goal is to build a comprehensive portfolio of programming skills and practical projects that demonstrate proficiency across multiple technologies and domains.

---

## 📚 Courses Overview

### 1️⃣ Python :
**🔗 Source:** [git.ir - 100 Days of Code](https://git.ir/udemy-100-days-of-code-the-complete-python-pro-bootcamp-for-2023/)

**🎯 Learning Objectives:**
- Master Python by building 100 projects in 100 days
- Learn automation, game development, app development, web development, data science, and machine learning
- Build professional-level Python programs
- Master libraries: Selenium, Beautiful Soup, Requests, Flask, Pandas, NumPy, Scikit-Learn, Plotly, Matplotlib
- Create a portfolio of 100 Python projects for job applications
- Build complete websites and web applications with Python
- Use Python for data science and machine learning

**📁 Directory:** `/python/`

---

### 2️⃣ Go (Golang) :
**🔗 Source:** [git.ir - Go Complete Guide](https://git.ir/udemy-go-the-complete-developers-guide-golang/)

**🎯 Learning Objectives:**
- Build concurrent programs with Go Routines and Channels
- Learn advanced Go features
- Understand differences between common data structures
- Prove your knowledge with dozens of included quiz questions
- Use interfaces to dramatically simplify complex programs
- Use types to future-proof programs and reduce difficulty of refactors

**📁 Directory:** `/golang/`

---

### 3️⃣ SQL & PostgreSQL:
**🔗 Source:** [git.ir - SQL Bootcamp](https://git.ir/udemy-the-complete-sql-bootcamp-go-from-zero-to-hero-2/)

**🎯 Learning Objectives:**
- Use SQL to query databases
- Use SQL to perform data analysis
- Confidently add SQL and PostgreSQL to your resume
- Learn to execute GROUP BY statements
- Replicate real-world situations and query reports

**📁 Directory:** `/sql-postgresql/`

---

### 4️⃣ JavaScript:
**🔗 Source:** [git.ir - Complete JavaScript](https://git.ir/udemy-the-complete-javascript-course-2025-from-zero-to-expert2/)

**🎯 Learning Objectives:**
- Become an advanced, confident, and modern JavaScript developer from scratch
- Build 6 beautiful real-world projects for your portfolio (not boring toy apps!)
- Become job-ready by understanding how JavaScript really works behind the scenes
- How to think and work like a developer: problem-solving, researching, workflows
- JavaScript fundamentals: variables, if/else, operators, boolean logic, functions, arrays, objects, loops, strings, etc.
- Modern ES6+ from the beginning: arrow functions, destructuring, spread operator, optional chaining (ES2020), etc.
- Modern OOP: Classes, constructors, prototypal inheritance, encapsulation, etc.
- Complex concepts like the 'this' keyword, higher-order functions, closures, etc.
- Asynchronous JavaScript: Event loop, promises, async/await, AJAX calls and APIs
- How to architect your code using flowcharts and common patterns
- Modern tools for 2022 and beyond: NPM, Parcel, Babel, and ES6 modules
- Practice your skills with 50+ challenges and assignments (solutions included)
- Get fast and friendly support in the Q&A area
- Course pathways: design your unique learning path according to your goals!

**📁 Directory:** `/javascript/`

---

## 🗂️ Repository Structure

```
learning-journey/
├── python/
│   ├── days1/         
│   │   ├── day-001/
│   ├── days2/          
│   ├── days3/          
│   ├── day4/          
│   ├── requirements.txt

│
├── golang-complete/
│   ├── basics/
│   │   ├── hello-world/
│   │   ├── data-types/
│   │   └── control-structures/
│   ├── advanced/
│   │   ├── goroutines/
│   │   ├── channels/
│   │   └── interfaces/
│   ├── projects/
│   ├── go.mod
│   ├── go.sum

│
├── sql-postgresql/
│   ├── queries/
│   │   ├── basic-queries.sql
│   │   ├── joins.sql
│   │   └── aggregations.sql
│   ├── exercises/
│   ├── real-world-scenarios/
│   ├── database-setup.sql
│   └── README.md
│
├── javascript-2025/
│   ├── fundamentals/
│   │   ├── 01-variables/
│   │   ├── 02-functions/
│   │   └── 03-arrays-objects/
│   ├── modern-js/
│   │   ├── es6-features/
│   │   ├── oop/
│   │   └── modules/
│   ├── async-js/
│   │   ├── promises/
│   │   ├── async-await/
│   │   └── ajax-apis/
│   ├── projects/
│   │   ├── project-01/
│   │   ├── project-02/
│   │   └── ...
│   ├── package.json
│   ├── package-lock.json
│   └── README.md
│
└── README.md (this file)
```

---

## 🚀 Setup & Installation

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8+**
- **Go 1.20+**
- **Node.js 18+**
- **PostgreSQL 14+**
- **Git**

---

## 💻 Running the Projects

### Python Projects

```bash
# Verify Python installation
python --version
# or
python3 --version

# Clone the repository
git clone https://github.com/AmirabbasAfrasiyabi/Learning-Journey
cd learning-journey/python 

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Run a specific day's project
cd days1
python days1.py

# Deactivate virtual environment when done
deactivate
```

---

### Go (Golang) Projects

```bash
# Verify Go installation
go version

# Navigate to Go project directory
cd learning-journey/golang-complete

# Initialize Go module (first time only)
go mod init golang-complete

# Download dependencies
go mod tidy

# Run a specific program
go run main.go

# Run programs in subdirectories
cd basics/hello-world
go run main.go

# Build executable
go build -o app main.go
./app

# Run with live reload (install air first)
go install github.com/cosmtrek/air@latest
air

# Run tests
go test ./...

# Format code
go fmt ./...
```

**Common Go Commands:**
- `go get <package>` - Download a package
- `go mod vendor` - Create vendor directory
- `go clean` - Remove build artifacts
- `go doc <package>` - View package documentation

---

### SQL & PostgreSQL Projects

```bash
# Install PostgreSQL
# Windows: Download from postgresql.org
# Mac: brew install postgresql
# Linux: sudo apt-get install postgresql postgresql-contrib

# Start PostgreSQL service
# Mac: brew services start postgresql
# Linux: sudo service postgresql start
# Windows: Use Services app

# Access PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE learning_db;

# Connect to database
\c learning_db

# Run SQL scripts from psql
\i /path/to/sql-postgresql/database-setup.sql
\i /path/to/sql-postgresql/queries/basic-queries.sql

# Run SQL script from command line
psql -U postgres -d learning_db -f queries/basic-queries.sql

# Export query results to CSV
\copy (SELECT * FROM table_name) TO 'output.csv' CSV HEADER

# Common psql commands
\l                  # List all databases
\dt                 # List all tables
\d table_name       # Describe table structure
\q                  # Quit psql
```

**Recommended Tools:**
- **pgAdmin 4** - GUI for PostgreSQL
- **DBeaver** - Universal database manager
- **VS Code** with PostgreSQL extension
- **DataGrip** - JetBrains database IDE

**Database Setup:**
```sql
-- Run this first to set up the database
CREATE DATABASE learning_db;
\c learning_db

-- Create sample tables
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    enrollment_date DATE
);
```

---

### JavaScript Projects

```bash
# Verify Node.js and npm installation
node --version
npm --version

# Navigate to JavaScript project directory
cd learning-journey/javascript-2025

# Install dependencies
npm install

# Run development server
npm start
# or
npm run dev

# Build for production
npm run build

# Run tests
npm test

# Lint code
npm run lint

# Format code
npm run format
```

**package.json Example:**
```json
{
  "name": "javascript-2025",
  "version": "1.0.0",
  "description": "Complete JavaScript Course Projects",
  "scripts": {
    "start": "parcel index.html",
    "dev": "parcel index.html --open",
    "build": "parcel build index.html",
    "test": "jest",
    "lint": "eslint .",
    "format": "prettier --write ."
  },
  "devDependencies": {
    "parcel": "^2.10.0",
    "@babel/core": "^7.23.0",
    "eslint": "^8.50.0",
    "prettier": "^3.0.0",
    "jest": "^29.7.0"
  },
  "dependencies": {
    "axios": "^1.5.0"
  }
}
```

**Running Simple HTML/JS Files:**
```bash
# Option 1: Use Live Server extension in VS Code
# Right-click on HTML file → Open with Live Server

# Option 2: Use Python's built-in server
python -m http.server 8000
# Then open: http://localhost:8000

# Option 3: Use Node.js http-server
npx http-server -p 8000
```

**Each Project Contains:**
- `index.html` - Main HTML file
- `script.js` - JavaScript code
- `style.css` - Styling
- `README.md` - Project instructions
- `package.json` - Dependencies (if applicable)

---

## 🎯 Overall Goals

- ✅ Master **Full-Stack Development** skills
- ✅ Prepare for job market and interviews
- ✅ Create a strong, diverse portfolio
- ✅ Learn industry best practices and design patterns
- ✅ Develop problem-solving and debugging skills
- ✅ Understand how to architect and scale applications

---

## 📚 Resources

### Official Documentation
- [Python Docs](https://docs.python.org/3/)
- [Go Documentation](https://go.dev/doc/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

### Helpful Tools
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Regex101](https://regex101.com/) - Regular expression tester
- [JSON Formatter](https://jsonformatter.org/)
- [SQL Fiddle](http://sqlfiddle.com/) - Test SQL queries online

---

## 📞 Contact & Social

Feel free to reach out if you have questions or want to connect:

- 💼 [LinkedIn:](www.linkedin.com/in/amirabbas-afrasiyabi-a6a230259)]
- 🐙 [Github](https://github.com/AmirabbasAfrasiyabi)]
- 📧 Email: [abb.afrasiyabi@gmail.com]

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

Special thanks to:
- All the instructors and course creators
- The developer communities on Stack Overflow, Reddit, and Discord
- Open source contributors whose tools make learning easier

---

## 🗓️ Timeline

**Started:** December 2025  
**Expected Completion:** December 2026  
**Last Updated:** December 26, 2025


