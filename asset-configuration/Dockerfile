FROM python:3.8-slim-buster as asset-configuration

ARG platform=aws

WORKDIR /src

COPY . .

ENV ENVIRONMENT production

RUN pip install pandas==1.5.2

RUN pandas config virtualenvs.create false
RUN pandas install --no-interaction --no-ansi --no-dev

ENV PYTHONPATH="$PYTHONPATH:/app"

EXPOSE 5000

WORKDIR /app/packages/$platform/src

RUN mv main_$platform.py main.py

RUN ls -la

CMD [ "python", "main.py"]
