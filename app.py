import json
import requests
from flask import Flask

app = Flask(__name__)

# Define the webhook URL
webhook_url = "https://discord.com/api/webhooks/1335280363576234014/SmCmZoScfpe3iXRdu2PPNutmeq1aBoLD2Ja80lH3tO-zI47ggMx3t9gfn1Nyk1h7mZQQ"

@app.route("/")
def index():
    # Data to send in the webhook message
    data = {
        "content": "Hello!",
        "embeds": [
            {
                "title": "Test Message",
                "description": "Hello! This is a test embed.",
                "color": 16711680  # Red color
            }
        ]
    }
    
    # Send the request to Discord webhook
    response = requests.post(webhook_url, json=data)
    
    # Check if the message was sent successfully
    if response.status_code == 204:
        return "Message sent successfully!"
    else:
        return "Failed to send message."

if __name__ == "__main__":
    app.run()
