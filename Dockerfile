FROM alpine:latest

MAINTAINER shimona prabhu <shimprab@cisco.com>

RUN apk add --no-cache python3-dev \
    && apk add --no-cache py-pip \
    && pip3 install --upgrade pip \
    && apk add python python-dev py-pip build-base libffi-dev openssl-dev libgcc 
    

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]