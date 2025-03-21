# Chat Bot
Chatbot application built using Django, Template, Grog API, SQLite3, and a frontend developed with Tailwind CSS, CSS, and JavaScript. This project serves as a texting assistant chat with interactive chat functionalities with sentiment analysis.

## Features

- **Chat Bot with LLM**: Integrates Grog API (Llama3) for high-quality text responses with sentiment analysis.
- **User-Friendly UI**: Responsive and interactive chat interface built with Tailwind CSS, CSS, and JavaScript.
- **Conversation Management**: Users can create, retrieve, update, and delete conversations.
- **User Authentication**: Register, login, and token refresh functionality in chatbot conversations.
- **Unit Testing**: Ensures API reliability with mock data testing.
- **SQLite3 Database**: Stores chat logs and user interactions.
- **Error Handling & Fallback**: Manages API limits and provides fallback responses.

## Project Structure

```
Assignment/
├── Ai_bot/
│   ├── chatbot/
│   ├── chatbot_llm/
│   ├── template/
│   ├── manage.py
│   ├── requirements.txt
│   ├── db.sqlite3
├── frontend/  # Contains CSS & JS for the chat UI
```

## Installation & Setup

### Clone the Repository
```sh
git clone: https://github.com/your-repo/Chatbot.git](https://github.com/AshiqSazid/Chatbot.git
cd Chatbot
```

### Create a Virtual Environment & Install Dependencies
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file with the following content:
```env
grog_API_KEY=grog_api_key_here
DATABASE_URL=sqlite3://username:password@localhost: http://127.0.0.1:8000/Chatbot_db
```

### Apply Database Migrations
```sh
python manage.py migrate
python manage.py createsuperuser  # (Optional, for admin access)
```

### Run the Server
```sh
python manage.py runserver
```

## Usage
1. Open a browser and go to `sqlite3://username:password@localhost:http://127.0.0.1:8000/Chatbot_db`
2. Register or log in to start chatting with the Chat bot.
3. Manage conversations from the chatbot interface.
## Contributing
Contributions are welcome! Fork the repository, make your changes, and submit a pull request,or mail ashiqsazid494@gmail.com


