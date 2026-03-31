FROM alpine:3.23
RUN apk upgrade
RUN apk add bash
RUN apk add curl
RUN apk add busybox-extras
RUN apk add --update python3
RUN apk add py-pip
RUN apk add openssl
RUN apk add nslookup
RUN apk add jq
COPY checkit3.py checkit3.py
CMD ["python3","-u","./checkit3.py"]

