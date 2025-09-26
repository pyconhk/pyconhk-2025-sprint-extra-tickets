FROM python:3.13-alpine

# Set the working directory inside the container.
WORKDIR /app

# Copy the Python requirements file first to leverage Docker's layer caching.
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# --- Final Configuration ---
# Create a non-root user for security.
RUN adduser -D ctf-user
USER ctf-user
WORKDIR /home/ctf-user

COPY encryptor .
COPY solver.py .
COPY ticket.txt .

CMD ["python", "solver.py"]
