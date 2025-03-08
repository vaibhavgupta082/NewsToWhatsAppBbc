# News to WhatsApp - Web Scraping Project

## 📌 Project Overview
This project fetches news articles from a public website using web scraping techniques and sends the extracted content to an individual via WhatsApp. It automates the process of retrieving the latest news and delivering it directly to a recipient’s WhatsApp.

## 🚀 Features
- Scrapes real-time news data from a public website.
- Extracts and processes relevant news content.
- Integrates with WhatsApp API to send messages.
- Automates news delivery at regular intervals.

## 🔧 Technologies Used
- **Python** - Core programming language.
- **BeautifulSoup** - Web scraping.
- **Requests** - Fetching website content.
- **Selenium** *(if needed)* - Handling dynamic content.
- **Twilio API / WhatsApp API** - Sending messages via WhatsApp.

## 🛠 Setup Instructions
1. **Clone the repository**
   ```sh
   git clone https://github.com/vaibhavgupta082/NewsToWhatsAppBbc.git
   cd NewsToWhatsAppBbc
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure WhatsApp API**
   - Sign up for Twilio / WhatsApp API.
   - Get API keys and configure them in `.env` or script.
4. **Run the script**
   ```sh
   python main.py
   ```

## 📌 Usage
- Modify the website URL in the script to scrape news from different sources.
- Customize the message format before sending it to WhatsApp.
- Schedule the script using cron jobs or task schedulers for automated updates.

## 📜 License
This project is open-source and available under the MIT License.

---
### ✨ Contributions & Feedback
Feel free to contribute, suggest improvements, or report issues by creating a pull request or opening an issue on GitHub.

📩 **Author:** Vaibhav Gupta  
🔗 **GitHub:** [vaibhavgupta082](https://github.com/vaibhavgupta082)

