# syntax=docker/dockerfile:1
FROM python:3.11-slim

# 基本環境
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# 設定工作目錄
WORKDIR /app

# 安裝套件（先複製 requirements）
COPY requirements.txt .
RUN pip install -r requirements.txt

# 再複製程式碼
COPY . .

# 容器內 Gradio port
EXPOSE 7860

# 啟動你的 Gradio App
CMD ["python", "startup.py"]
