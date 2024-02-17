FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

#ENV FLASK_ENV=production

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
