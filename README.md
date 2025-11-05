# AI-machinelearning-week4
AI applications in software engineering

## Table of Contents  
1. [Project Title](#project-title)  
2. [Project Description](#project-description)  
3. [Features](#features)  
4. [Documentation of Thinking Process](#documentation-of-thinking-process)  
5. [What It Does & Objective](#what-it-does--objective)  
6. [How It’s Useful](#how-its-useful)  
7. [How to Run the Project Locally](#how-to-run-the-project-locally)  
8. [Technologies Used & Why](#technologies-used--why)  
9. [Challenges Faced](#challenges-faced)  
10. [Future Features / Enhancements](#future-features--enhancements)  
---

## Project Title  
**AI Applications in Software Engineering** (Week 4)

---

## Project Description  
This project is the Week 4 assignment for the AI for sotware development module in PLP. It explores how artificial intelligence (AI) can be applied in the software engineering lifecycle, specifically in code generation, automated testing, and predictive analytics. The repository contains code, notebooks, test scripts, documentation and reflections that align with the assignment’s theoretical, practical and ethical components.

---

## Features  
- **AI-Powered Code Completion**: A comparison between an AI-generated Python function (via tools like GitHub Copilot / Tabnine) and a manual implementation.  
- **Automated Testing with AI**: Test script for login page with valid and invalid credentials (using Selenium or Testim.io) capturing success/failure rates.  
- **Predictive Analytics for Resource Allocation**: A Jupyter notebook using the Breast Cancer Wisconsin (Diagnostic) Dataset (from Kaggle) to train a model (e.g., Random Forest) to predict issue priority.  
- **Ethical Reflection & Bonus Proposal**: Written reflections on bias/fairness and a bonus AI tool proposal for software engineering.

---

## Documentation of Thinking Process  
1. **Understanding the assignment structure**: The assignment is divided into three parts — theoretical (short-answer & case study), practical (3 tasks) and ethical reflection plus bonus.  
2. **Selecting tools and data**: Chose GitHub Copilot for code generation, Selenium/Testim.io for AI-driven tests, and the breast cancer dataset from Kaggle for predictive analytics (mapped to issue priority).  
3. **Implementation path**:  
   - Task 1: Use Copilot to generate code, also write manual code, then compare.  
   - Task 2: Build a simple login page test script, run valid/invalid cases, capture results.  
   - Task 3: Preprocess data, map categories to priorities, train RandomForest, evaluate accuracy and F1-score.  
4. **Ethical & Bonus considerations**: Reflect on dataset bias, use of fairness tools (e.g., IBM AI Fairness 360) and propose an AI tool (DocuMind) for documentation automation.  
5. **Reporting & sharing**: Prepare well-commented code, screenshots, a PDF report, and a 3-minute video demo (per submission guidelines).

---

## What It Does & Objective  
### Objective  
To demonstrate how AI can automate and improve software engineering tasks — such as code generation, testing and resource allocation — while also reflecting on ethical considerations and suggesting forward-looking innovations.

### What It Does  
- Sorts and compares code implementations for the same problem (Task 1).  
- Automates UI login testing with AI-enhanced tools (Task 2).  
- Builds a predictive model to classify priorities (Task 3).  
- Provides theoretical analysis and ethical reflection.  
- Proposes a novel AI tool for future software engineering workflows.

---

## How It’s Useful  
- **For developers**: Shows practical use-cases of AI in everyday software engineering tasks.  
- **For teams**: Demonstrates how AI tools reduce manual effort, increase accuracy, and accelerate workflows.  
- **For educators/students**: Serves as a structured assignment example that combines theory, practice and ethics.  
- **For future projects**: The predictive analytics approach and tool proposal can be extended to real-world issue-tracking systems.

---

## How to Run the Project Locally  
### Prerequisites  
- Python 3.8+ installed  
- `pip` for package installation  
- ChromeDriver (if using Selenium with Chrome) or corresponding WebDriver  

### Setup  
```bash
git clone https://github.com/makxxic/AI-machinelearning-week4.git
cd AI-machinelearning-week4
pip install -r requirements.txt
```
Task 1: Code Comparison
Run the manual and AI-generated function scripts (manual.py, ai1.py or ai2.py) in a Python shell or script runner.

Task 2: Automated Testing
Ensure WebDriver is installed and in your PATH. Then run:

```bash
python test_login.py
```
Check output for pass/fail messages and view screenshots if captured.

Task 3: Predictive Analytics
Open the Jupyter notebook (e.g., ai_model.ipynb or similar). In Google Colab or locally:

```bash
jupyter notebook
# then open the notebook file
```
Execute the cells to preprocess data, train the model, and review performance metrics (accuracy, F1-score, confusion matrix).

## Viewing Results
Check console output for pass/fail tests.
Review notebook results (metrics and confusion matrix).
Screenshots and analysis are documented in the report file (AI applications in software engineering.docx / PDF).

## Technologies Used & Why
Python – Versatile, widely used in AI/ML and scripting.
Scikit-learn – For model training and evaluation (RandomForestClassifier, metrics).
Pandas – Data loading and preprocessing.
Selenium / Testim.io – Automates browser testing to simulate real-life UI flows and evaluate AI-assisted testing.
GitHub Copilot – Demonstrates AI-powered code completion and coding assistance.
Google Colab – Interactive environment for predictive analytics and visualizations.

## Challenges Faced
Mapping the breast cancer dataset to a “High/Medium/Low” priority classification required creative reinterpretation and careful label mapping.
Ensuring the Selenium WebDriver setup works across different machines/browsers posed compatibility issues.
Managing and comparing AI-generated code vs manual code in a fair and meaningful way required defining consistent criteria (efficiency, readability, maintainability).
Documenting the full workflow (theoretical, practical and ethical) while staying aligned with submission guidelines and time constraints.

## Future Features / Enhancements
Extend the predictive analytics task to a real software-engineering dataset (e.g., issues from GitHub) and multi-class (High/Medium/Low) priority prediction rather than binary.
Integrate a CI/CD pipeline that automatically triggers the AI-test suite and predictive model upon pull requests.
Develop a dashboard to visualise test results, model performance and bias/fairness metrics in real-time.

Expand the AI tool proposal (DocuMind) into a working prototype plugin or web-app with live repository integration.

Incorporate additional fairness tools and automated bias mitigation into the modelling workflow.
