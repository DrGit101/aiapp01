FROM python:3.7
EXPOSE 8501

WORKDIR /var/app

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD streamlit run aiapp01.py
