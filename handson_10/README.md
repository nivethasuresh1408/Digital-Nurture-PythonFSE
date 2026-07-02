# Microservices Decomposition

| Service | Responsibility | Endpoints | Database |
|----------|---------------|-----------|----------|
| Course Service | Course CRUD | /api/courses/* | courses.db |
| Student Service | Student Enrollment | /api/students/* | students.db |
| Auth Service | Login & JWT | /api/auth/* | auth.db |
| Notification Service | Email | Internal | notification.db |

## HTTP vs Message Queue

HTTP:
- Immediate response
- Tight coupling
- Service dependency

Message Queue:
- Asynchronous
- Loose coupling
- Better scalability

RabbitMQ and Kafka are preferred for background processing and high-volume event-driven systems.