# Diversion

# AI Financial Chatbot

## Overview
The AI Financial Chatbot is a web-based financial assistant designed to help users with budget planning, investment suggestions, EMI calculations, and goal-based savings. The chatbot uses Google's Gemini API to provide intelligent financial insights and recommendations. The frontend is built using HTML, CSS, JavaScript, and Bootstrap, while the backend is powered by Python with Flask.

## Features
- **Budget Planner** – Helps users plan their monthly or yearly budget efficiently.
- **EMI Calculator** – Calculates EMI payments for loans based on principal, interest rate, and tenure.
- **Goal-Based Savings** – Assists users in setting and tracking their financial goals.
- **Investment Suggestions** – Provides personalized investment recommendations.
- **Ghost Mode** – Enables users to browse financial suggestions anonymously.
- **AI Chatbot** – A chatbot that provides real-time financial insights and answers queries using the Gemini API.

## Tech Stack
### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

### Backend
- Python
- Flask
- Gemini API (Google's AI-powered API for financial insights)

## Installation & Setup
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Flask (`pip install flask`)
- Requests (`pip install requests`)

### Steps to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-financial-chatbot.git
   cd ai-financial-chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Gemini API key in the `.env` file:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
4. Run the Flask server:
   ```bash
   python app.py
   ```
5. Open `index.html` in your browser or navigate to `http://127.0.0.1:5000/`.

## Usage
- Users can interact with the chatbot by entering queries related to financial planning.
- The budget planner, EMI calculator, and savings tracker can be accessed from the navigation bar.
- Ghost mode allows anonymous browsing of financial insights.

## Future Enhancements
- Integration with more financial APIs for real-time stock & crypto market insights.
- User authentication and profile-based financial tracking.
- Mobile app version for better accessibility.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

---
