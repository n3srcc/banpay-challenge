challenge

## Use
 Set environment variables, copy .env.example to .env

- for startup
  ```
  make run
  ```
- for stop
  ```
  make stop
  ```
- for cleanup
  ```
  make clean
  ```

# Create user
```
curl --location 'http://localhost:5000/api/users' \
--header 'Content-Type: application/json' \
--data '{
  "password": "342323sx.-a#",
  "username": "admin",
  "rol": "admin"
}'
```
# Login
```
curl --location 'http://localhost:5000/api/login' \
--header 'Content-Type: application/json' \
--data '{
  "password": "123456",
  "username": "emondragon2"
}'
```
# Get
```
curl --location 'http://localhost:5000/api/films' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwODEyOTA1MSwianRpIjoiZGEzYzM2ZDAtMDExYi00NDBjLWJlODUtZGI0MjJkMjViYzNmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX2lkIjoiNjVjZmZiMTMzYWE5OWNhMzdhNDI1MjZjIiwicm9sIjoidmVoaWNsZXMifSwibmJmIjoxNzA4MTI5MDUxLCJjc3JmIjoiN2I1MjRjMGQtMjI3NC00NmNhLTk3ZWUtMjcxMjI0YjM2NjkyIiwiZXhwIjoxNzA4MTI5OTUxfQ.csE_w4dGLBkajGnWwji9H-DBdGfZvV-OXg4IvDuow60'
```
## Directory Hierarchy
```
|—— .env
|—— .env.example
|—— .gitignore
|—— app
|    |—— database.py
|    |—— models.py
|    |—— routes
|        |—— services.py
|        |—— swagger_docs
|            |—— api_docs.yaml
|        |—— users.py
|        |—— utils.py
|        |—— __init__.py
|    |—— services
|        |—— consumer.py
|        |—— __init__.py
|    |—— __init__.py
|—— app.py
|—— config.py
|—— docker-compose.yml
|—— Dockerfile
|—— entrypoint.sh
|—— Makefile
|—— requirements.txt
```
