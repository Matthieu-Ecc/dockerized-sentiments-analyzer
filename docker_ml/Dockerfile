FROM python:3.7

# set work directory
WORKDIR /model

COPY analyzer.py .
COPY vader_API.py .

ENV FLASK_APP=vader_API.py
ENV FLASK_RUN_HOST=0.0.0.0

# install dependencies
COPY * .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]