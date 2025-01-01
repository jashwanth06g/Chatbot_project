Event Finder Chatbot
A chatbot designed to help users discover and explore events in their district, offering personalized event details and seamless user interaction.
Table of Contents
Overview
Features
Tech Stack
Installation
Usage
Challenges Faced
Contributing
License
Acknowledgments
Overview
The Event Finder Chatbot is an intelligent solution for users to inquire about events happening in their local districts. Built using Python and Flask, the chatbot provides detailed event information, alternative suggestions, and a smooth conversational experience.

Features
Interactive chatbot interface for querying events.
District-based event filtering with a fallback for nearby locations.
Detailed event descriptions, including date, location, and ticket pricing.
Web-based deployment with a responsive and user-friendly frontend.
JSON-based event data storage for easy scalability and management.
Tech Stack
Backend: Python, Flask
Frontend: HTML, CSS, Bootstrap
Data Storage: JSON
Deployment: Flask local server
Installation
Follow these steps to set up the project locally:

Clone the Repository:

git clone https://github.com/yourusername/event-finder-chatbot.git  
cd event-finder-chatbot  
Create a Virtual Environment:


python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
Install Dependencies:


pip install -r requirements.txt  
Run the Application:


python app.py  
Access the Chatbot:
Open your browser and navigate to http://127.0.0.1:5000/.

Usage
Launch the chatbot via the Flask app.
Interact with the chatbot by entering the name of a district to search for events.
If events are found, the chatbot will display details. Otherwise, it will suggest nearby events.
Users can request detailed information about specific events.
Challenges Faced
Designing a conversational flow that accounts for various user inputs and edge cases.
Implementing error handling for invalid district names or missing event data.
Creating a seamless user experience while managing large datasets.
Debugging Flask integration for the chatbot’s backend functionality.
Contributing
We welcome contributions to enhance the Event Finder Chatbot.

Fork the repository.
Create a new branch:

git checkout -b feature/your-feature-name  
Commit your changes:

git commit -m "Add your message here"  
Push to the branch:

git push origin feature/your-feature-name  
Submit a pull request.


Acknowledgments
Flask documentation for backend development.
Bootstrap for providing responsive UI components.
Real Python for insights into JSON handling and Python debugging.
Event management platforms like Eventbrite for design inspiration.
