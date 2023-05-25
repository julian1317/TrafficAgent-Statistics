FROM python:3.11.3

WORKDIR /Heatmap

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir protobuf==3.19.0

COPY . .

CMD ["streamlit", "run", "Heatmap.py"]

