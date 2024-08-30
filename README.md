
# FletAuth Lite

![Version](https://img.shields.io/badge/version-0.2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.12.2-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🚀 Introduction

Welcome to **FletAuth Lite**, a sleek and modern Python application built using the [Flet](https://flet.dev/) framework. The app features user authentication using Firebase Authentication and customizable settings. It is designed to work seamlessly on every major operating system (Windows, macOS, Linux) and mobile platforms (iOS, Android). The project is still a work in progress (WIP), with some features currently under development.

## ✨ Features

- 🚧 **User Authentication (WIP)**
  - Login and registration system using Firebase Authentication.
  - Secure password storage via Firebase.

- 🚧 **Settings (WIP)**
  - Customize your app experience.
  - More options coming soon!

## 🛠️ Installation

To get started with FletAuth Lite, follow these simple steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/xdmanus1/First-app-in-flet.git
   cd flet-app
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Firebase:**
   - Set up a Firebase project in the Firebase Console.
   - Download the `google-services.json` (for Android) or `GoogleService-Info.plist` (for iOS) from your Firebase project.
   - Ensure that your Firebase credentials (API keys, etc.) are not hardcoded in your code. Use environment variables or a secure method to manage these credentials.

   **Example using environment variables:**

   ```python
   import os

   firebase_api_key = os.getenv('FIREBASE_API_KEY')
   ```

   - Store your Firebase credentials in a `.env` file and add `.env` to your `.gitignore` to prevent leaks.

5. **Run the app:**
   - For desktop (PC/Mac):
     ```bash
     flet run main.py
     ```
   - For Web:
     ```bash
     flet run main.py --web
     ```
   - For Android/iOS:
     ```bash
     flet run main.py --android  # or --ios
     ```

## 📋 Usage

Once the app is running, you can access it via your browser or directly from the Flet interface. The current version includes the following pages:

- **Login Page (WIP):** Securely log in to access your data.
- **Registration Page (WIP):** Create a new account (work in progress).
- **Settings Page (WIP):** Personalize your app settings (work in progress).

## 🔄 Roadmap

### Upcoming Features

- **Advanced Authentication:**
  - Implement Firebase and oauth.
  - Implement social logins.
  
- **Settings Overhaul:**
  - More customizable settings.

## 🐛 Contributing

Contributions are welcome! If you have ideas, issues, or bugs, feel free to submit a pull request or open an issue on GitHub.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📫 Contact

For any questions or suggestions, feel free to reach out at [karsahunor@gmail.com](mailto:karsahunor@gmail.com).

---

Made with ❤️ by [xdmanus](https://github.com/xdmanus1)
