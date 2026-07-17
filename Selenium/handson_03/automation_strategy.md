# Test Automation Process, Lifecycle & Framework Types

**Name:** Nivetha S  
**Course:** Digital Nurture 5.0  
**Hands-on:** 03  
**Topic:** Test Automation Process, Lifecycle & Framework Types

---

# Objective

The objective of this hands-on is to understand the automation testing process, identify suitable test cases for automation, evaluate automation ROI, analyze flaky tests, compare automation framework types, and recommend the most appropriate framework for the Course Management System.

---

# Task 1: Automation Decision and Test Case Selection

## 17. Criteria for Deciding Whether a Test Case Should Be Automated

### 1. Frequency of Execution

Tests that are executed repeatedly are ideal candidates for automation because automation saves time and effort.

**Application**

The POST `/api/courses/` endpoint is executed frequently during regression testing, making it a good automation candidate.

---

### 2. Regression Testing

Regression tests verify that existing functionality continues to work after code changes.

**Application**

Every code update requires verification that course creation still returns HTTP Status Code 201.

---

### 3. Repetitive Manual Effort

Tasks requiring repetitive execution should be automated to reduce manual effort.

**Application**

Creating a course with different datasets repeatedly is tedious manually and can be automated.

---

### 4. Stable Functionality

Stable features with minimal UI or API changes are good candidates for automation.

**Application**

The POST `/api/courses/` API is a core feature and changes infrequently.

---

### 5. Data-Driven Testing

Tests requiring multiple input combinations benefit greatly from automation.

**Application**

Testing different course names, course codes, and credit values is easier using automated data-driven tests.

---

# 18. Manual vs Automation Decision

| Test Case | Decision | Justification |
|------------|----------|---------------|
| Regression testing for all CRUD endpoints after every code change | Automate | Executed frequently and suitable for regression automation. |
| Exploratory testing of a new search feature | Manual | Requires human observation and creativity. |
| Performance testing with 100 concurrent users | Automate | Performance testing requires automation tools. |
| UI testing of the login page | Automate | Login is executed frequently and remains relatively stable. |
| Verify Swagger API documentation | Manual | Documentation changes infrequently and requires visual verification. |
| Smoke test after deployment | Automate | Smoke tests are executed after every deployment and should be fast. |

---

# 19. Test Automation ROI

### Definition

Return on Investment (ROI) measures whether the time and cost invested in automation are justified compared to manual testing.

### Given

Automation Development Time = 4 hours

Manual Execution Time = 30 minutes

### Calculation

4 hours = 240 minutes

240 ÷ 30 = **8 executions**

Therefore, automation pays for itself after approximately **8 executions**.

### Maintenance Overhead

After the 10th execution, assume a maintenance effort equal to 20% of the manual execution time.

Manual execution = 30 minutes

20% maintenance = 6 minutes

Effective automation maintenance = 6 minutes per run after the 10th execution.

Even with maintenance, automation remains more cost-effective than manual execution over time.

---

# 20. Flaky Tests

### Definition

A flaky test is a test that sometimes passes and sometimes fails without any changes to the application code.

### Example

A Selenium login test occasionally fails because the Login button loads slowly and the script attempts to click it before it becomes clickable.

### Strategies to Prevent Flaky Tests

1. Use Explicit Waits instead of Thread.sleep().
2. Use stable locators such as ID or Name instead of dynamic XPath.
3. Ensure proper test data and independent test execution.

---

# Task 2: Compare Automation Framework Types

## 21. Comparison of Automation Frameworks

### Linear Framework

**Description**

The Linear Framework executes test scripts sequentially without code reuse.

**Advantage**

Simple to understand and implement.

**Disadvantage**

High maintenance due to duplicated code.

**Example**

Testing a single Course Creation workflow.

---

### Modular Framework

**Description**

The application is divided into independent modules with reusable scripts.

**Advantage**

Improves code reusability.

**Disadvantage**

Requires additional planning.

**Example**

Separate modules for Login, Course Management, and Student Management.

---

### Data-Driven Framework

**Description**

Test data is stored externally in Excel, CSV, or JSON files while scripts remain unchanged.

**Advantage**

Supports testing multiple datasets.

**Disadvantage**

Managing external data files increases complexity.

**Example**

Testing course creation with multiple course names and credit values.

---

### Keyword-Driven Framework

**Description**

Test cases are created using keywords such as Click, Enter Text, and Verify.

**Advantage**

Allows non-technical testers to create test cases.

**Disadvantage**

Framework development is time-consuming.

**Example**

Business users prepare keyword-based login tests.

---

### Hybrid Framework

**Description**

Combines Modular, Data-Driven, and Keyword-Driven frameworks.

**Advantage**

Highly reusable, scalable, and flexible.

**Disadvantage**

Initial framework setup is complex.

**Example**

Complete Course Management Automation Suite.

---

# 22. Recommended Framework

### Recommendation

A **Hybrid Framework** is recommended.

### Justification

The Hybrid Framework provides:

- Reusable login components across multiple test cases.
- Data-Driven testing for 50 user/password combinations.
- Support for both technical and non-technical team members.
- Easy maintenance and scalability.

This framework combines the advantages of Modular, Data-Driven, and Keyword-Driven approaches, making it ideal for enterprise Selenium projects.

---

# 23. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/

│

├── config/
│      config.py
│      settings.json
│
├── data/
│      login_data.xlsx
│      course_data.xlsx
│
├── pages/
│      login_page.py
│      dashboard_page.py
│      course_page.py
│
├── tests/
│      test_login.py
│      test_course.py
│
├── utilities/
│      browser_utils.py
│      excel_utils.py
│      logger.py
│
├── reports/
│      HTML Reports
│
├── screenshots/
│      Failure Screenshots
│
├── requirements.txt
│
└── README.md
```

### Folder Description

| Folder | Purpose |
|----------|----------|
| config | Stores configuration files. |
| data | Stores Excel or CSV test data. |
| pages | Contains Page Object Model classes. |
| tests | Contains Selenium test scripts. |
| utilities | Helper functions such as browser utilities and logging. |
| reports | Stores HTML execution reports. |
| screenshots | Stores failure screenshots. |
| requirements.txt | Python package dependencies. |
| README.md | Project documentation. |

---

# Conclusion

This hands-on provided an understanding of automation planning before implementation. It covered automation decision criteria, automation ROI, flaky tests, and different automation framework architectures. Among the available frameworks, the Hybrid Framework offers the best balance of maintainability, reusability, scalability, and flexibility for enterprise-level Selenium automation projects such as the Course Management System.
