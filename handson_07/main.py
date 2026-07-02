from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import List
from contextlib import asynccontextmanager

from database import engine, Base, get_db
import models
import schemas


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Course Management System API",
    description="FastAPI CRUD API with SQLAlchemy Async ORM",
    version="2.0",
    lifespan=lifespan
)


# -----------------------------
# Background Task
# -----------------------------

def send_confirmation_email(student_email: str, course_name: str):
    import time

    time.sleep(2)

    print(
        f"\nConfirmation email sent to {student_email} "
        f"for enrolling in {course_name}\n"
    )


# ==========================================================
# DEPARTMENT APIs
# ==========================================================

@app.post(
    "/api/departments/",
    response_model=schemas.DepartmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Departments"]
)
async def create_department(
    dept: schemas.DepartmentCreate,
    db: AsyncSession = Depends(get_db)
):

    department = models.Department(
        name=dept.name,
        head_of_dept=dept.head_of_dept,
        budget=dept.budget
    )

    db.add(department)

    await db.commit()
    await db.refresh(department)

    result = await db.execute(
        select(models.Department)
        .options(selectinload(models.Department.courses))
        .where(models.Department.id == department.id)
    )

    return result.scalar_one()


# ==========================================================
# COURSE APIs
# ==========================================================

@app.post(
    "/api/courses/",
    response_model=schemas.CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create Course",
    response_description="Course created successfully"
)
async def create_course(
    course: schemas.CourseCreate,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(models.Department).where(
            models.Department.id == course.department_id
        )
    )

    department = result.scalar_one_or_none()

    if department is None:
        raise HTTPException(
            status_code=400,
            detail="Department not found"
        )

    result = await db.execute(
        select(models.Course).where(
            models.Course.code == course.code
        )
    )

    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=400,
            detail="Course code already exists"
        )

    db_course = models.Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(db_course)

    await db.commit()
    await db.refresh(db_course)

    return db_course


@app.get(
    "/api/courses/",
    response_model=List[schemas.CourseResponse],
    tags=["Courses"]
)
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(models.Course)
        .offset(skip)
        .limit(limit)
    )

    return result.scalars().all()


@app.get(
    "/api/courses/{id}",
    response_model=schemas.CourseResponse,
    tags=["Courses"]
)
async def get_course(
    id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(models.Course).where(
            models.Course.id == id
        )
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@app.put(
    "/api/courses/{id}",
    response_model=schemas.CourseResponse,
    tags=["Courses"]
)
async def update_course(
    id: int,
    updated: schemas.CourseCreate,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(models.Course).where(
            models.Course.id == id
        )
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    course.name = updated.name
    course.code = updated.code
    course.credits = updated.credits
    course.department_id = updated.department_id

    await db.commit()
    await db.refresh(course)

    return course


@app.delete(
    "/api/courses/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"]
)
async def delete_course(
    id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(models.Course).where(
            models.Course.id == id
        )
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    await db.delete(course)
    await db.commit()
    # ==========================================================
# STUDENT APIs
# ==========================================================

@app.post(
    "/api/students/",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"]
)
async def create_student(
    student: schemas.StudentCreate,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(models.Student).where(
            models.Student.email == student.email
        )
    )

    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=400,
            detail="Student email already exists"
        )

    department = await db.execute(
        select(models.Department).where(
            models.Department.id == student.department_id
        )
    )

    if department.scalar_one_or_none() is None:
        raise HTTPException(
            status_code=400,
            detail="Department not found"
        )

    db_student = models.Student(
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email,
        department_id=student.department_id,
        enrollment_year=student.enrollment_year
    )

    db.add(db_student)

    await db.commit()
    await db.refresh(db_student)

    return db_student


@app.get(
    "/api/students/",
    response_model=List[schemas.StudentResponse],
    tags=["Students"]
)
async def get_students(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(models.Student)
    )

    return result.scalars().all()


# ==========================================================
# ENROLLMENT APIs
# ==========================================================

@app.post(
    "/api/enrollments/",
    response_model=schemas.EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Enrollments"]
)
async def create_enrollment(
    enrollment: schemas.EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(models.Student).where(
            models.Student.id == enrollment.student_id
        )
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    result = await db.execute(
        select(models.Course).where(
            models.Course.id == enrollment.course_id
        )
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db_enrollment = models.Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )

    db.add(db_enrollment)

    await db.commit()
    await db.refresh(db_enrollment)

    background_tasks.add_task(
        send_confirmation_email,
        student.email,
        course.name
    )

    return db_enrollment


@app.get(
    "/api/courses/{course_id}/students/",
    tags=["Courses"]
)
async def get_course_students(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(models.Enrollment).where(
            models.Enrollment.course_id == course_id
        )
    )

    enrollments = result.scalars().all()

    students = []

    for enrollment in enrollments:

        result = await db.execute(
            select(models.Student).where(
                models.Student.id == enrollment.student_id
            )
        )

        student = result.scalar_one()

        students.append(
            {
                "id": student.id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "email": student.email,
                "department_id": student.department_id,
                "enrollment_year": student.enrollment_year
            }
        )

    return students