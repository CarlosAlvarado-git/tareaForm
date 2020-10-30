FROM python:3.8.5

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /OndaJson .

CMD ["python", "formulario.py"]