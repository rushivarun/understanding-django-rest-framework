FROM python:3.6.9-alpine3.9

RUN apk add --update
    
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
EXPOSE 8000
CMD ["python", "./drflearn/manage.py", "runserver", "0.0.0.0:8000"]

