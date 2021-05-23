FROM ubuntu
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip

RUN python3 -m pip install grpcio
RUN python3 -m pip install grpcio-tools

COPY data.proto /ser/
COPY server.py /ser/

ENV PYTHONPATH /ser

ARG address=localhost:10000
ENV add ${address}

RUN cd ser && \
    python3 -m grpc_tools.protoc -I./. --python_out=. --grpc_python_out=. ./data.proto && \
    touch leaderboard.json

CMD cd ser && \
    python3 server.py $add