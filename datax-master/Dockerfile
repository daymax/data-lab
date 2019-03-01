FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /datax
WORKDIR /datax
COPY . /datax/
RUN pip install --index-url https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

# ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000"]