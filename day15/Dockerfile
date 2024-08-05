ARG BASE_CONTAINER=python:3
FROM $BASE_CONTAINER

RUN pip install --upgrade pip && \
    pip install --no-cache-dir flask 

COPY ./my_flask.py /usr/src/myapp/

ENTRYPOINT ["python"]
CMD ["/usr/src/myapp/my_flask.py"]