FROM python:alpine3.18
COPY . /inicio_5_9
WORKDIR /inicio_5_9

RUN pip install -r requirements.txt
#exponemos en el puerto 5005 del contenedor
EXPOSE 5005

ENTRYPOINT [ "python3"]
CMD ["app/__init__.py"]