FROM python:3.11-slim

WORKDIR /workspace

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy function source
COPY . .

# Configure the Functions Framework for an event-triggered function
ENV PORT=8080

CMD ["functions-framework", "--target", "hello_pubsub", "--signature-type=event", "--port=8080"]
