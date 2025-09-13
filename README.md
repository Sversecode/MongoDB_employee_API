Employee Management API (Django + MongoDB)

A RESTful API built with Django REST Framework and MongoDB for managing employees.
It supports CRUD operations, department-based filtering, average salary aggregation, and skill-based search.



🚀 Features

Create, Read, Update, Delete Employees

Filter employees by department

Get average salary grouped by department

Search employees by skill

Aggregation using MongoDB

JSON-based skills field


📌Sample Document Structure
{
"employee_id": "E123",
"name": "John Doe",
"department": "Engineering",
"salary": 75000,
"joining_date": "2023-01-15",
"skills": ["Python", "MongoDB", "APIs"]
}


📌 A ready-to-use Postman collection is included in this repo:
Import it into Postman to test all endpoints easily.
