FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 8080

# Run Flask with gunicorn (production WSGI server)
CMD ["gunicorn", "-b", ":8080", "app:app"]
