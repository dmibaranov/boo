FROM python:3.7-rc-alpine

COPY b.py /usr/local/share/

WORKDIR /usr/local/share

CMD ["python"]