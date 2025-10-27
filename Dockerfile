FROM python:3.13-slim
COPY requirements.txt .
RUN pip install  -r requirements.txt
WORKDIR /bot
COPY . .
CMD ["python","bot_main.py"]