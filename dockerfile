FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8501


CMD ["streamlit", "run", "app_streamlit/app.py"]