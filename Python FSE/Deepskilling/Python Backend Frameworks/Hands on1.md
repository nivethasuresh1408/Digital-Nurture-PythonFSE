NIVETHA S
## Task 1
## Django Core Architecture## 1. Request Response Cycle
Browser sends GET request
↓
URL Router (urls.py)
↓
View (views.py)
↓
Model (models.py queries database)
↓
Database
↓
Model returns data
↓
View prepares response
↓
HttpResponse sent back to Browser [1, 2, 3, 4, 5] 
## 2. Middleware
Middleware sits between the request and the view.
It processes every incoming request before the view
and every outgoing response after the view. [6, 7] 
Example Middleware
AuthenticationMiddleware
Identifies logged-in users.
SessionMiddleware
Manages user sessions. [8] 
## 3. WSGI vs ASGI
WSGI (Web Server Gateway Interface)
Handles synchronous applications.
Suitable for traditional Django applications. [9] 
ASGI (Asynchronous Server Gateway Interface)
Supports asynchronous programming,
WebSockets,
real-time chat,
long-lived connections. [10] 
Django uses WSGI by default.
Use ASGI when building asynchronous or real-time applications.
## 4. MVC vs MVT
MVC
Model -> Database
View -> User Interface
Controller -> Business Logic [11] 
Django follows MVT
Model -> Model
View -> Controller
Template -> View
------------------------------


## Task 2
<img width="1917" height="1020" alt="image" src="https://github.com/user-attachments/assets/6bed7c95-2b4f-4f87-b34b-0df644b95989" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/66fea547-29a3-4de8-b411-e04e97dd7d0d" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/bb427557-69c6-490d-bf2c-9b34bf924c6d" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/3be29469-ad93-4861-baea-500ecbaf7264" />
