FROM python:3.10-slim-bullseye
EXPOSE 8000

WORKDIR /app
COPY . .

RUN pip install fastapi "uvicorn[standard]"
RUN pip install -q transformers
RUN pip install torch torchvision

RUN echo "loaded"


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
