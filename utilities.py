import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pywhatkit as kit
from config import contact_list


def get_BBC_newsletter():
    url = "https://www.bbc.com/news"
    response = requests.get(url)

    now = datetime.now()
    file = now.strftime('%Y%m%d%H')
    filename = "data/"+ file + '.txt'
    print("file name: " + filename)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    for article in soup.find_all("a", {"data-testid": "internal-link"}):
        link = "https://www.bbc.com" + article["href"]  # Complete URL
        headline_tag = article.find("h2", {"data-testid": "card-headline"})
        description_tag = article.find("p", {"data-testid": "card-description"})
        
        if headline_tag and description_tag:
            articles.append({
                "headline": headline_tag.get_text(strip=True),
                "description": description_tag.get_text(strip=True),
                "link": link
            })

    # Print results
    with open(filename, "a") as f:
        for article in articles:
            print(f"Headline: {article['headline']}",file=f)
            print(f"Description: {article['description']}",file=f)
            print(f"Link: {article['link']}\n",file=f)
    f.close()
    
    return f"newsletter from BBC is Extracted successfully"

def send_whatsapp_message():
    try:
        now = datetime.now()
        filename = now.strftime('%Y%m%d%H')

        contact_list_ = contact_list

        # Read the file safely
        try:
            name = "data/" + filename + ".txt"
            with open(name, 'r') as f:
                content = f.read().strip()
                print(content)
        except FileNotFoundError:
            print("Error: output.txt file not found.")
            content = "Default message in case file is missing."

        # Send WhatsApp message
        try:
            for phone_number in contact_list_:
                kit.sendwhatmsg_instantly(phone_number, content)
                print(f"Sent to {phone_number}")

        except Exception as e:
            print(f"Error sending WhatsApp message: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
    return f"whatsapp message sent successfully."

