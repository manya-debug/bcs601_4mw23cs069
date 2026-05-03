from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    text = "Fun with Programming"

    reversed_text = text[::-1]

    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)

    upper_text = text.upper()

    result = "<h2>String Operations</h2>"
    result += f"Original String: {text}<br><br>"
    result += f"Reversed String: {reversed_text}<br>"
    result += f"Vowel Count: {vowel_count}<br>"
    result += f"Uppercase: {upper_text}<br>"

    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
