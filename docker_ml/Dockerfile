FROM python:3.7

# set work directory
WORKDIR /model

COPY analyzer.py .

# install dependencies
COPY * .
RUN pip install -r requirements.txt


CMD ["python", "analyzer.py"]