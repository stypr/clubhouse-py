#  run it:
#  docker run -it -v ${PWD}:/usr/src/app clubhouse /bin/bash
FROM python:3
WORKDIR /root


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt




WORKDIR /usr/src/app
CMD [ "/bin/bash"]


