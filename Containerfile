FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN media_wizard create-db
RUN media_wizard populate-db
RUN media_wizard add-user -u admin -p admin
EXPOSE 5000
CMD ["media_wizard", "run"]
