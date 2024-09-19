From python:3.10.5

WORKDIR /app

COPY app.py /app

RUN pip3 install uvicorn openai pydantic fastapi dotenv

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]