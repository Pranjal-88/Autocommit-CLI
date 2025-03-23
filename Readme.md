# 🚀 AutoCommit-CLI: AI-Powered Git Commit Messages

AutoCommit-CLI is a powerful command-line tool that automates the process of writing meaningful Git commit messages using **Google Gemini AI**. No more struggling to come up with good commit messages—just let AI do it for you! 🎯

## ✨ Features
- 🔍 **Analyze Git changes** and generate meaningful commit messages.
- 🔄 **Auto-commit** staged changes with AI-generated messages.
- ☁️ **Push changes** to the repository automatically.
- ⚡ **Works with Google Gemini API** for intelligent commit suggestions.
- 🏗 **Easy to use & install** as a CLI tool.

---

## 📦 Installation

### **1️⃣ Install via `pip`**
```bash
pip install autocommit-cli
```

### **2️⃣ Set Up Google Gemini API Key**
AutoCommit-CLI requires a Google Gemini API key. Get your key from [Google AI Studio](https://aistudio.google.com/) and store it in a `.env` file in your project:
```ini
GEMINI_API_KEY="your_api_key_here"
```

---

## 🛠 Usage

### **1️⃣ Analyze Changes & Get a Suggested Commit Message**
```bash
autocommit --analyze
```
📌 **Example Output:**
```
💡 Suggested Commit Message:
fix: resolved authentication issue in login flow
```

### **2️⃣ Commit with AI-Generated Message**
```bash
autocommit --commit
```
📌 **Example Output:**
```
✅ Committed Successfully: fix: updated error handling in user registration
```


---

## ⚙️ How It Works
1. The tool fetches **staged Git changes** using `git diff --staged`.
2. It sends these changes to the **Google Gemini API** to generate a relevant commit message.
3. It commits the changes with the generated message.
4. (Optional) It pushes the changes to the repository if `--push` is used.

---

## 🔧 Development & Contribution
Want to improve AutoCommit-CLI? Follow these steps:

### **Clone the repository:**
```bash
git clone https://github.com/Pranjal-88/Autocommit-CLI.git
cd Autocommit-CLI
```

### **Install dependencies:**
```bash
pip install -r requirements.txt
```

### **Run locally for testing:**
```bash
python autocommit.py --analyze
```

### **Contribute:**
- Fork the repo ✅
- Create a new branch ✅
- Make your changes ✅
- Submit a pull request ✅

---

## 📝 License
This project is licensed under the **MIT License**.

---

## ❤️ Support
If you like this project, **give it a ⭐ on GitHub**! 🙌

