
FROM python:3.9-slim


RUN pip install flask requests


COPY ./front.py /app/front.py
COPY ./templates /app/templates


WORKDIR /app


CMD ["python", "front.py"]