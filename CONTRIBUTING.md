Here is a detailed `CONTRIBUTING.md` file to guide contributors on how to contribute to your **Autocommit-CLI** project.  

---
<!--  This comment is for testing auto-commit CLI -->

## **CONTRIBUTING.md**
```md
# Contributing to Autocommit-CLI 🚀

First off, thanks for considering contributing to **Autocommit-CLI**! 🎉  
We welcome all contributions—whether it’s fixing a bug, improving documentation, or adding a new feature.

---

## 📌 How to Contribute

### 1️⃣ Fork the Repository 🍴
- Click the **"Fork"** button on the top right of this repo.
- This creates a copy of the repo under your GitHub account.

### 2️⃣ Clone the Forked Repository 🖥️
Run the following command in your terminal:
```sh
git clone https://github.com/Pranjal-88/Autocommit-CLI.git
cd Autocommit-CLI
```

### 3️⃣ Set Up the Development Environment 🛠️
- Make sure you have **Python 3.8+** installed.
- Create a virtual environment:
  ```sh
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

### 4️⃣ Create a New Branch 🌱
Before making changes, create a new branch:
```sh
git checkout -b feature-branch-name
```

### 5️⃣ Make Your Changes ✨
- Edit the code in the `autocommit/` directory.
- Follow best practices and keep your code clean.

### 6️⃣ Test Your Changes 🧪
- Run tests to ensure everything works fine:
  ```sh
  pytest
  ```

### 7️⃣ Commit and Push Changes 📤
- Commit your changes with a meaningful message:
  ```sh
  git add .
  git commit -m "feat: Added XYZ feature"
  ```
- Push the changes to your fork:
  ```sh
  git push origin feature-branch-name
  ```

### 8️⃣ Create a Pull Request (PR) 🔄
- Go to the original repository: `https://github.com/Pranjal-88/Autocommit-CLI`
- Click **"New Pull Request"** and select your branch.
- Provide a clear title and description of your changes.
- Click **"Create Pull Request"** 🎉

---

## 💡 Contribution Guidelines
✔️ Follow **PEP8** coding standards.  
✔️ Keep pull requests small and focused.  
✔️ Add comments where necessary.  
✔️ Update **README.md** if changes affect usage.  

---

## 💬 Need Help?
- Open an **issue** if you found a bug.
- Reach out via **Discussions** if you have questions.

🚀 **Happy Coding!**  
Thanks for contributing! ❤️
```

---

### **📌 How to Add This to Your Repo**
1. **Create the file**:
   ```sh
   touch CONTRIBUTING.md
   ```
2. **Commit & Push**:
   ```sh
   git add CONTRIBUTING.md
   git commit -m "docs: Add contributing guidelines"
   git push origin main
   ```

This makes it easier for people to **contribute effectively** to your project! 🚀