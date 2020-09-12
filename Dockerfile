FROM python:3.8.4-alpine3.12



WORKDIR /app-run

COPY requirements.txt /app-run/requirements.txt
RUN pip install -r /app-run/requirements.txt
COPY . /app-run

ENTRYPOINT ["python3.8", "run.py"]