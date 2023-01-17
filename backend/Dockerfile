FROM python
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR ./
# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
# Copy project
COPY . /

EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
