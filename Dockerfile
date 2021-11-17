FROM python:3.7.4

WORKDIR /dockerized_app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/app.py"]