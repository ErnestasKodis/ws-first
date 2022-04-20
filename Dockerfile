# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python

EXPOSE 5000

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

ENTRYPOINT [ "python" ]
CMD ["app.py"]