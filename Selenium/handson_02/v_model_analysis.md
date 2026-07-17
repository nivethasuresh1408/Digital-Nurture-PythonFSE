# SDLC vs TDLC – V-Model & Agile QA Integration

**Name:** Nivetha S

**Course:** Digital Nurture 5.0

**Hands-on:** 02

**Topic:** SDLC vs TDLC – V-Model & Agile QA Integration

---

# Objective

The objective of this hands-on is to understand the Software Development Life Cycle (SDLC), Test Development Life Cycle (TDLC), V-Model, Agile QA integration, Entry and Exit Criteria, and the Shift-Left Testing principle.

# Task 1

## 9. V-Model Mapping

```text
                  SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)

Requirements
      │
      ▼
System Design
      │
      ▼
Architecture Design
      │
      ▼
Module Design
      │
      ▼
     Coding
      ▲
      │
Unit Testing
      ▲
      │
Integration Testing
      ▲
      │
System Testing
      ▲
      │
Acceptance Testing

             TEST DEVELOPMENT LIFE CYCLE (TDLC)
```
## 10. SDLC and TDLC Mapping

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|-------------|--------------------------|------------------------|
| Requirements Gathering | Acceptance Testing | Acceptance Test Plan |
| System Design | System Testing | System Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan |
| Module Design | Unit Testing | Unit Test Cases |
| Coding | Execution of all planned tests | Source Code |

## 11. Entry and Exit Criteria

### Unit Testing

**Entry Criteria**

- Module coding is completed.
- Unit test cases are prepared.

**Exit Criteria**

- All unit test cases executed.
- No critical defects remain.

---

### Integration Testing

**Entry Criteria**

- Individual modules pass unit testing.
- Integration environment is ready.

**Exit Criteria**

- Module interaction works correctly.
- Major integration defects resolved.

---

### System Testing

**Entry Criteria**

- Complete application is deployed.
- System test cases are available.

**Exit Criteria**

- All functional test cases executed.
- No Critical or High severity defects.

---

### Acceptance Testing

**Entry Criteria**

- System testing completed successfully.
- Client receives the application.

**Exit Criteria**

- Customer accepts the software.
- Business requirements are satisfied.

## 12. Early QA Engagement

### Point 1

QA participates during the Requirements Gathering phase to identify unclear or incomplete requirements.

### Point 2

QA reviews the System Design documents to prepare test scenarios before development begins.

# Task 2

## 13. Problems with Waterfall Model

### Problem 1

Testing begins only after development is completed, causing late defect detection.

### Problem 2

Fixing defects becomes expensive because many modules may already depend on the faulty code.

### Problem 3

Customer feedback is received very late, making requirement changes difficult.

## 14. QA Role in Agile Ceremonies

### Sprint Planning

QA reviews user stories and defines acceptance criteria.

---

### Daily Stand-up

QA discusses testing progress, blockers, and defects.

---

### Sprint Review

QA validates completed features before demonstrating them to stakeholders.

---

### Sprint Retrospective

QA suggests improvements to the testing process for future sprints.

## 15. Shift-Left Testing Practices

| Shift-Left Practice | Application to Course Management API |
|----------------------|--------------------------------------|
| Requirement Review | QA reviews requirements to identify ambiguities before coding begins. |
| Test Cases Before Coding | QA prepares test cases before developers implement the API. |
| Static Code Analysis | Developers analyze code quality using static analysis tools before execution. |
| API Contract Testing | Validate API request and response formats before integrating with other modules. |

## 16. Acceptance Criteria (Given-When-Then)

### Scenario 1 – Happy Path

```gherkin
Given the College Admin is logged in

When the Admin enters valid course details and clicks Save

Then the course should be created successfully.
```

---

### Scenario 2 – Duplicate Course Code

```gherkin
Given a course with the same course code already exists

When the Admin submits the course

Then the system should display "Course Code Already Exists".
```

---

### Scenario 3 – Missing Required Fields

```gherkin
Given the Admin leaves the Course Name blank

When the Admin clicks Save

Then the system should display "Course Name is Required".
```

# Conclusion

This hands-on helped in understanding the relationship between SDLC and TDLC through the V-Model. It also explained Entry and Exit Criteria, Agile QA practices, Shift-Left Testing, and writing Acceptance Criteria using Gherkin format. These concepts form the foundation of effective software testing and quality assurance.