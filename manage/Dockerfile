FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9000

CMD [ "python", "./roomsrv.py", "--port", "9000"]