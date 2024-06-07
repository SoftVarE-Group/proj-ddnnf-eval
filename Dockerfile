FROM python:3.9.18-slim

WORKDIR /benchmark

RUN apt-get update -y
RUN apt-get install libgmp-dev libmpfr-dev libmpc-dev libc6 libstdc++6 glibc-source -y

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

ENTRYPOINT ["python3", "./run.py"]
