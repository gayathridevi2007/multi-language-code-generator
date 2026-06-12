# AI-Powered Multi-Language Code Generator

An AI-powered web application that converts natural language programming prompts into executable code in **Python**, **Java**, and **C** using **Google Gemini AI**.

---

## Overview

The AI-Powered Multi-Language Code Generator enables users to describe programming problems in plain English and instantly receive equivalent code implementations in multiple programming languages.

The application uses **Google Gemini AI** to dynamically generate code instead of relying on predefined templates, making it capable of handling a wide variety of programming requests.

---

## ✨ Features

* Generate code from natural language prompts
* Supports Python, Java, and C
* Powered by Google Gemini AI
* Modern and responsive user interface
* One-click code copy functionality
* Real-time code generation
* Flask-based backend
* Secure API key management using environment variables

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### AI Integration

* Google Gemini API
* Google GenAI SDK

### Version Control

* Git
* GitHub

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/gayathridevi2007/multi-language-code-generator.git
```

### Move to Project Directory

```bash
cd multi-language-code-generator
```

### Install Dependencies

```bash
pip install flask
pip install google-genai
pip install python-dotenv
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root directory.

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

---

## ▶️ Run the Application

```bash
python app.py
---

## 🔄 Workflow

```text
User Prompt
     ↓
Frontend (HTML/CSS/JavaScript)
     ↓
Flask Backend
     ↓
Google Gemini API
     ↓
Python / Java / C Code Generation
     ↓
Display Results on Web Page
```

### How It Works

1. User enters a programming prompt.
2. JavaScript sends the prompt to the Flask backend.
3. Flask forwards the request to Google Gemini AI.
4. Gemini generates code in Python, Java, and C.
5. Flask processes the response.
6. Generated code is displayed on the webpage.

---

## 🎯 Sample Prompts

```text
Create a palindrome checker
```

```text
Create a factorial program
```

```text
Create a student management system
```

```text
Create a library management system
```

```text
Create a calculator using functions
```

---

## 🚀 Future Enhancements

* Support additional programming languages
* Download generated code files
* Syntax highlighting
* Light/Dark theme toggle
* AI-powered code explanation
* Cloud deployment
* User authentication system

---


## 📄 License

This project is developed for educational and learning purposes.
