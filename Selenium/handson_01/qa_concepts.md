# QA Concepts, Functional Testing & Defect Lifecycle

**Name:** Nivetha S  
**Course:** Digital Nurture 5.0  
**Hands-on:** 01  
**Topic:** QA Concepts, Functional Testing & Defect Lifecycle

---

# Task 1: Map Testing Types to a Real System

## 1. Testing Types for the Course Management API

### 1.1 Unit Testing

**Description:**
Unit testing verifies a single function or module independently without interacting with other components.

**Test Case:**
Test the `validate_course_data()` function to ensure it accepts valid course details.

**Input**

```json
{
  "course_name": "Python Programming",
  "credits": 4
}
```

**Expected Result**

The validation function should return **Valid** and allow the request to proceed.

**Testing Category**

Functional Testing

---

### 1.2 Integration Testing

**Description**

Integration testing verifies whether two or more modules work correctly together.

**Test Case**

Verify that the POST `/api/courses/` endpoint correctly stores a course in the database.

**Steps**

1. Send a POST request.
2. API validates the request.
3. Database stores the record.
4. Retrieve the record using GET `/api/courses/`.

**Expected Result**

The new course is successfully stored and retrieved from the database.

**Testing Category**

Functional Testing

---

### 1.3 System Testing

**Description**

System testing validates the complete application from start to finish.

**Test Case**

1. Login as Admin.
2. Create a new course.
3. Save the course.
4. Search the course.
5. Edit the course.
6. Delete the course.

**Expected Result**

Every operation completes successfully without errors.

**Testing Category**

Functional Testing

---

### 1.4 User Acceptance Testing (UAT)

**Description**

User Acceptance Testing verifies whether the system satisfies business requirements.

**Test Case**

A College Administrator logs into the Course Management System and performs the following tasks:

- Add a new course
- Update course details
- Search available courses
- Delete a course

**Expected Result**

The administrator is able to complete all tasks successfully without technical knowledge.

**Testing Category**

Functional Testing

---

## 2. Functional vs Non-Functional Testing

### Functional Testing

Functional testing verifies **what the system does**.

**Example**

Verify that POST `/api/courses/` successfully creates a new course.

Expected Result

HTTP Status Code **201 Created**

---

### Non-Functional Testing

Non-functional testing verifies **how well the system performs**.

**Example: Performance Testing**

- Simulate 1000 simultaneous users accessing the Course Management API.
- Measure response time.

Expected Result

- Response time should be less than **2 seconds**
- No server crash
- API remains available

---

## 3. Black-Box Testing vs White-Box Testing

| Black-Box Testing | White-Box Testing |
|-------------------|------------------|
| Tests functionality without seeing the source code | Tests internal code structure and logic |
| Focuses on input and output | Focuses on code coverage and program flow |
| Performed by QA/Test Engineers | Performed by Developers |
| No programming knowledge required | Programming knowledge required |

**QA Tester typically performs:** Black-Box Testing

**Developer typically performs:** White-Box Testing

---

## 4. Formal Test Cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|---------------|------------|-----------------|--------------|-----------|
| TC001 | Create course with valid details | API server is running | Enter valid course data and click Execute | Course created successfully (201 Created) | | |
| TC002 | Create course with empty course name | API server is running | Leave Course Name empty and submit | Validation error (400 Bad Request) | | |
| TC003 | Create duplicate course | Course already exists | Submit same course details again | Duplicate course error displayed | | |

---

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

```
Defect Reported
       │
       ▼
      New
       │
       ▼
    Assigned
       │
       ▼
      Open
       │
       ▼
      Fixed
       │
       ▼
     Retest
       │
       ▼
    Verified
       │
       ▼
     Closed
```

### Rejected Path

```
New
 │
 ▼
Rejected
```

Reason:

- Not a bug
- Cannot reproduce
- Invalid defect

---

### Deferred Path

```
Open
 │
 ▼
Deferred
```

Reason:

- Fix postponed
- Low business priority
- Planned for future release

---

## 6. Severity and Priority Classification

### Bug A

**Issue**

POST `/api/courses/` returns 500 Internal Server Error.

**Severity:** Critical

**Priority:** P1

**Justification**

The main functionality is completely broken and users cannot create courses.

---

### Bug B

**Issue**

Course names longer than 150 characters are silently truncated.

**Severity:** Medium

**Priority:** P3

**Justification**

The application still works, but data loss occurs.

---

### Bug C

**Issue**

Swagger documentation contains a spelling mistake.

**Severity:** Low

**Priority:** P4

**Justification**

Cosmetic issue with no impact on functionality.

---

### Bug D

**Issue**

Correct login credentials occasionally return 401 Unauthorized.

**Severity:** High

**Priority:** P1

**Justification**

Intermittent authentication failures affect user trust and indicate system instability.

---

## 7. Defect Report

| Field | Details |
|--------|---------|
| Defect ID | BUG-001 |
| Title | POST `/api/courses/` returns 500 Internal Server Error |
| Environment | Windows 11, Python 3.12, FastAPI, Chrome Latest |
| Build Version | Version 1.0 |
| Severity | Critical |
| Priority | P1 |
| Steps to Reproduce | 1. Start FastAPI Server.<br>2. Open Swagger UI.<br>3. Select POST `/api/courses/`.<br>4. Enter valid course details.<br>5. Click Execute. |
| Expected Result | Course should be created successfully with HTTP 201 Created. |
| Actual Result | HTTP 500 Internal Server Error is displayed. |
| Attachments | Screenshot of 500 Error |

---

## 8. Difference Between Severity and Priority

### Severity

Severity indicates **how much impact** the defect has on the application.

### Priority

Priority indicates **how urgently** the defect should be fixed.

### Example

A spelling mistake on the CEO's dashboard before an important customer demonstration.

**Severity:** Low

Reason:

The application functions normally.

**Priority:** High

Reason:

The issue affects the company's professional image and must be fixed immediately.

---

# Conclusion

This hands-on covered the fundamental concepts of Software Quality Assurance, including testing levels, functional and non-functional testing, Black-Box and White-Box testing, defect lifecycle, severity and priority classification, and formal test case documentation. These concepts provide the foundation for manual testing and Selenium automation in subsequent hands-on exercises.