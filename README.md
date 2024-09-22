# WhatsApp Water Reminder

A Python script that sends automatic reminders to help remember to drink water throughout the day. This project utilizes the `pywhatkit` library to send messages via WhatsApp, featuring the ability to schedule messages only during specific hours.

## 🌟 Features

- **Automatic Reminders**: Sends WhatsApp messages at regular intervals to remind you to stay hydrated.
- **Customizable Schedule**: Messages are sent only during active hours (from 9 AM to 10 PM) to avoid disturbances at night.
- **Data Security**: Sensitive information, such as phone numbers and messages, is managed through environment variables for added security.

## 💻 Technologies Used

- Python
- `pywhatkit`
- `dotenv`

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/whatsapp-water-reminder.git
   cd whatsapp-water-reminder

2. Install the dependencies:
    ```bash
   pip install -r requirements.txt]

3. **Change the Phone Number and the Message**

  `phone_number = ("YOUR PHONE_NUMBER")`
  
  `message = ("YOUR MESSAGE")`
  
4. **Run the script:**
     ```bash
     python main.py
