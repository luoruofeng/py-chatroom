FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5555

CMD [ "python", "./wsserver.py", "--port", "5555", "--roomip", "im-room", "--roomport", "9000" ]