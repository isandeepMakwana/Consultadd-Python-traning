FROM python:3.8.9
RUN mkdir app
WORKDIR /app
COPY requirments.txt /app/
RUN pip install -r requirments.txt
COPY . /app/
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
