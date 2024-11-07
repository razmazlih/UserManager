from app.utils.firebase import initialize_firebase
initialize_firebase()  # מבצע אתחול Firebase לפני יצירת האפליקציה

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)