import requests

# URL של ה-API
url = "http://127.0.0.1:5000/admin/token"

# טוקן מנהל (Admin Token) לאימות בקשת המנהל
admin_token = "123"

# נתוני האפליקציה החדשה
data = {
    "app_id": "new_app",
    "token": "unique_token_for_app"
}

# כותרות הבקשה
headers = {
    "Authorization": f"Bearer {admin_token}",
    "Content-Type": "application/json"
}

# שליחת בקשת POST ליצירת האפליקציה
response = requests.post(url, json=data, headers=headers)

# בדיקה והדפסת התוצאה
if response.status_code == 201:
    print("Application created successfully!")
    print(response.json())
else:
    print("Failed to create application:", response.status_code, response.json())