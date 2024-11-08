from app.utils.firebase import initialize_firebase
from app.config import Config
initialize_firebase()

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=Config.PORT, debug=Config.DEBUG)