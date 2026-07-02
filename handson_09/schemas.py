from pydantic import BaseModel, EmailStr
from typing import Optional, List

# ==========================
# USER SCHEMAS
# ==========================

from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True

# ----------------------------
# Department Schemas
# ----------------------------

class DepartmentCreate(BaseModel):
    name: str
    head_of_dept: str
    budget: float


class DepartmentResponse(BaseModel):
    id: int
    name: str
    head_of_dept: str
    budget: float
    courses: List["CourseResponse"] = []

    class Config:
        from_attributes = True


# ----------------------------
# Course Schemas
# ----------------------------

class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int
    department_id: int

    class Config:
        from_attributes = True


# ----------------------------
# Student Schemas
# ----------------------------

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    department_id: int
    enrollment_year: int


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    department_id: Optional[int] = None
    enrollment_year: Optional[int] = None


class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    department_id: int
    enrollment_year: int

    class Config:
        from_attributes = True


# ----------------------------
# Enrollment Schemas
# ----------------------------

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int


class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int

    class Config:
        from_attributes = True


DepartmentResponse.model_rebuild()

class Token(BaseModel):
    access_token: str
    token_type: str