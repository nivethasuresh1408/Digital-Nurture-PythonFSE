"""
===========================================================
HANDS-ON 1
Task 1: Web Framework Foundations
===========================================================

1. REQUEST-RESPONSE CYCLE

When a user enters the URL:
GET /api/courses/

The request follows this path:

Browser
   ↓
URL Router (urls.py)
   ↓
View (views.py)
   ↓
Model (models.py)
   ↓
Database Query
   ↓
View Processes Data
   ↓
HttpResponse
   ↓
Browser

Explanation:
- The browser sends an HTTP GET request.
- Django's URL router matches the requested URL.
- The matched view function is executed.
- If data is required, the view communicates with the model.
- The model retrieves data from the database.
- The view prepares the response.
- Django sends the HTTP response back to the browser.


===========================================================

2. MIDDLEWARE

Middleware sits between the incoming request and the Django view.
It can process the request before it reaches the view and also
process the response before it is sent back to the browser.

Request
   ↓
Middleware
   ↓
View
   ↓
Middleware
   ↓
Response

Two built-in Django middleware classes:

1. SecurityMiddleware
   - Adds security features such as HTTPS redirects and security headers.

2. AuthenticationMiddleware
   - Associates the currently logged-in user with each request.

===========================================================

3. WSGI vs ASGI

WSGI (Web Server Gateway Interface)
- Supports synchronous applications.
- Handles one request at a time.
- Suitable for traditional Django applications.

ASGI (Asynchronous Server Gateway Interface)
- Supports asynchronous programming.
- Handles multiple requests efficiently.
- Supports WebSockets, chat applications and real-time notifications.

Django uses WSGI by default.

Use ASGI when building:
- Real-time chat applications
- Live notifications
- WebSocket applications
- High-concurrency asynchronous applications

===========================================================

4. MVC vs MVT

MVC Pattern

Model
- Manages application data and database.

View
- Displays data to the user.

Controller
- Handles user requests and business logic.


Django follows the MVT Pattern.

Model
- Handles database operations.

View
- Contains business logic and processes requests.
- Acts like the Controller in MVC.

Template
- Displays data to the user.
- Acts like the View in MVC.

MVC to MVT Mapping

MVC Model      → Django Model
MVC View       → Django Template
MVC Controller → Django View

===========================================================

Summary

Request Lifecycle:
Browser → URL → View → Model → Database → View → Response

Middleware:
Processes requests and responses before and after the view.

WSGI:
Used for synchronous Django applications.

ASGI:
Used for asynchronous and real-time applications.

Django Architecture:
Model → View → Template (MVT)

===========================================================
"""