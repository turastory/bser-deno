FROM python:3.9

EXPOSE 5000

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

ADD . .

ENV FLASK_APP=app.py
CMD ["python", "-m", "flask", "run"]