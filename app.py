from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

from flask import Flask, render_template, request, jsonify
from google import genai
import re

app = Flask(__name__)

# Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_codes(user_prompt):

    prompt = f"""
Generate code for the following problem:

{user_prompt}

Generate code in Python, Java and C.

IMPORTANT RULES:
1. Do NOT use markdown.
2. Do NOT use triple backticks.
3. Do NOT explain anything.
4. Return ONLY code.

Return EXACTLY in this format:

### PYTHON
code here

### JAVA
code here

### C
code here
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text

    python_code = ""
    java_code = ""
    c_code = ""

    try:

        python_match = re.search(
            r"### PYTHON(.*?)### JAVA",
            text,
            re.DOTALL
        )

        java_match = re.search(
            r"### JAVA(.*?)### C",
            text,
            re.DOTALL
        )

        c_match = re.search(
            r"### C(.*)",
            text,
            re.DOTALL
        )

        if python_match:
            python_code = (
                python_match.group(1)
                .replace("```python", "")
                .replace("```", "")
                .strip()
            )

        if java_match:
            java_code = (
                java_match.group(1)
                .replace("```java", "")
                .replace("```", "")
                .strip()
            )

        if c_match:
            c_code = (
                c_match.group(1)
                .replace("```c", "")
                .replace("```", "")
                .strip()
            )

    except Exception as e:
        print("Error:", e)

    return {
        "python": python_code,
        "java": java_code,
        "c": c_code
    }


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():

    data = request.json

    user_input = data.get('input', '')

    if not user_input.strip():
        return jsonify({
            "python": "",
            "java": "",
            "c": ""
        })

    result = generate_codes(user_input)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)