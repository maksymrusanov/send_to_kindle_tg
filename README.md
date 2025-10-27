# 📚 send_to_kindle_tg
**Telegram bot for sending books and documents to your Kindle via email**  
Bot: `@email_to_kindle_bot` 👋

This bot allows you to send documents and books to your Kindle device via email.

---

## ⚙️ Setup Instructions

### 1. Create a Kindle account

[Kindle Account Settings](https://www.amazon.co.uk/hz/mycd/preferences/myx#/home/settings/payment)

### 2. Approve the bot email

Add `botsendtokindle@gmail.com` to your **Approved Personal Document E-mail List** (at the bottom of your Kindle settings page) to enable sending and receiving documents.

### 3. Supported File Types

- PDF  
- DOC / DOCX  
- TXT  
- RTF  
- HTM / HTML  
- PNG / GIF / JPG / JPEG / BMP  
- EPUB  

---

## 🚀 Installation and Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/maksymrusanov/send_to_kindle_tg.git
cd send_to_kindle_tg
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root with the following:

```env
TELEGRAM_API_TOKEN=your_bot_token
KINDLE_EMAIL=your_kindle_email
SENDER_EMAIL=your_sender_email
SMTP_SERVER=smtp_server_address
SMTP_PORT=smtp_server_port
SMTP_PASSWORD=your_email_password
```

### 5. Run the bot

```bash
python bot_main.py
```

---

## 🐳 Docker (Optional)

Build and run using Docker:

```bash
docker build -t send_to_kindle_bot .
docker run --env-file .env send_to_kindle_bot
```

Or with Docker Compose:

```bash
docker compose up --build
```

---

## 🛠️ Usage

1. Open Telegram and find the bot `@email_to_kindle_bot`.  
2. Press **Start** to begin.  
3. Send any supported file to the bot.  
4. The bot will automatically forward the file to your Kindle.

---

## 🗂️ Project Structure

- `bot_main.py` — main entry point  
- `handlers.py` — command and message handlers  
- `sender.py` — logic for sending files to Kindle  
- `requirements.txt` — Python dependencies  
- `Dockerfile` — Docker image configuration  
- `docker-compose.yml` — Docker Compose setup  
- `.gitignore` — ignored files  

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
