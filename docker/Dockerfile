FROM python:3.6.8-jessie

# Cài code
RUN mkdir -p /code
RUN mkdir /log

RUN pip install gunicorn futures

COPY ./requirements.txt /code
RUN pip install -r /code/requirements.txt

COPY ./ /code

WORKDIR /code

ENTRYPOINT ["python", "/code/detailed_example.py"]

CMD []
