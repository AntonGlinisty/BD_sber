FROM redis

RUN apt-get -y update && apt-get install -y vim
RUN apt install -y python3 && apt-get install -y pip

COPY ./volumes /volumes

RUN pip install -r /volumes/requirements.txt --break-system-packages
