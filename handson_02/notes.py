"""
===========================
TASK 1
===========================

1. REQUEST-RESPONSE CYCLE

Browser
   |
GET /api/courses/
   |
URL Router (urls.py)
   |
View (views.py)
   |
Model (models.py)
   |
Database Query
   |
View Processes Data
   |
HttpResponse
   |
Browser


---------------------------------------

2. MIDDLEWARE

Middleware sits between the request and the view.

Request
   |
Middleware
   |
View
   |
Middleware
   |
Response

Example Middleware:

1. SecurityMiddleware
   - Protects against security vulnerabilities.

2. AuthenticationMiddleware
   - Identifies the logged-in user.

---------------------------------------

3. WSGI vs ASGI

WSGI
----
Supports synchronous applications.

Used for traditional Django applications.

ASGI
----
Supports asynchronous applications.

Supports:
- WebSockets
- Async Views
- Real-time Chat
- Notifications

Django uses WSGI by default.

Use ASGI when:
- Real-time communication is needed
- Async tasks are used
- High concurrency applications

---------------------------------------

4. MVC vs MVT

MVC

Model
View
Controller

Django follows MVT

Model
↓

Model

View (MVC)
↓

Template

Controller (MVC)
↓

View (Django)

Therefore,

MVC Model → Django Model

MVC View → Django Template

MVC Controller → Django View

"""