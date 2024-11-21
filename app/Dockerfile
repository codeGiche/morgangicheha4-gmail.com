
FROM python:3.8-slim

WORKDIR /app

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python","main.py"]