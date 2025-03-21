Ai bot:
Ai bot application using Django,Template,Grog API,Sqite3, and a frontend built(CSS & JS) with tailwind css. The project is basically of texting  assistant chat,it also has chat interactions.
Features:
Aibot with LLM: Integrates Grog API (llama3) for good text responses.
User-Friendly UI: Built with tailwind css,css and  JavaScript for a good responsive and friendly  chat interface.
Conversation Management: Create, retrieve, update, and delete conversations.
Authentication for user: Register, login, and we also used token refresh functionality in the chatbot conversation.
Unit Testing: Ensures API reliability with mock data testing.
SQLITE3 Database: Stores chat logs and user interactions.
Error Handling & Fallback: Handles API limits and provides fallback responses.

Assignment/
├── Ai_bot/
│   ├── chatbot/
│   ├── chatbot_llm/
│   ├── template
│   ├── manage.py
│   ├── requirements.txt
│   ├── db.sqlite3
├─── frontend/ (Contains CSS & JS chat UI)

Installation & Setup:
1. Clone the Repository
git clone https: //github.com/your-repo/AIbot-llm.git
cd chatbot-llm
2. Create a Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Set Up Environment Variables
Create a .env file with the following content:
grog_API_KEY=your_api_key_here
DATABASE_URL=sqlite3://username:password@localhost: http://127.0.0.1:8000/Chatbot_db
4. Apply Database Migrations
python manage.py migrate
python manage.py createsuperuser  # (Optional, for admin access)
5. Run the Server
python manage.py runserver
