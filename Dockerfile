FROM python:3.10-slim

RUN mkdir -p /app
COPY ./main.py /app/
COPY ./Credit.pickle4 /app/
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]