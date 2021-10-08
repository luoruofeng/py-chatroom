FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "python", "./httpserver.py", "--port", "80", "--roomip", "im-room", "--roomport", "9000", "--wsip", "127.0.0.1", "--wsport", "5555" ]