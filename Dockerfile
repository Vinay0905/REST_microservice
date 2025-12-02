FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file
# COPY [requirements.txt](http://_vscodecontentref_/0) .
COPY requirements.txt .
# Install Python dependencies
# RUN pip install --no-cache-dir -r [requirements.txt](http://_vscodecontentref_/1)
RUN pip install --no-cache-dir -r requirements.txt
# Copy all application code
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=run.py
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "run.py"]