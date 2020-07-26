FROM python:3.7.3-stretch

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY app.py /app/
COPY requirements.txt /app/
COPY tic_tac_toe_engine.py /app/
RUN mkdir /app/templates
COPY templates/play.html /app/templates/

# Install packages from requirements.txt
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Run app.py at container launch
CMD ["python", "app.py"]