FROM python:latest

WORKDIR /

COPY . /

RUN pip install openai requests 

# Run app.py when the container launches

CMD ["python", "linkedin_main.py"]
