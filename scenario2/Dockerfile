FROM alpine:3.23
RUN apk upgrade
RUN apk add curl
RUN apk add busybox-extras
RUN apk add --update python3
RUN apk add bash
COPY checkit3.py checkit3.py
CMD ["python3","-u","./checkit3.py"]

