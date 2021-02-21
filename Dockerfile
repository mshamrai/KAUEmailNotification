FROM python:3.8-slim

RUN pip3 install --upgrade pip

COPY ./ /app
RUN pip3 install --no-cache-dir -r app/requirements.txt

WORKDIR /app

CMD python ./src/main.py
