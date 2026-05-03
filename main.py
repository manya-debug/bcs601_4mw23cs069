from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    text = "Fun with Programming"

    reversed_text = text[::-1]

    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)

    upper_text = text.upper()

    return f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #74ebd5, #ACB6E5);
                text-align: center;
                padding: 50px;
            }}

            .container {{
                background: white;
                padding: 30px;
                border-radius: 15px;
                width: 50%;
                margin: auto;
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            }}

            h2 {{
                color: #333;
            }}

            p {{
                font-size: 18px;
                margin: 10px;
            }}

            .highlight {{
                color: #007BFF;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h2>✨ String Operations</h2>

            <p><span class="highlight">Original:</span> {text}</p>
            <p><span class="highlight">Reversed:</span> {reversed_text}</p>
            <p><span class="highlight">Vowel Count:</span> {vowel_count}</p>
            <p><span class="highlight">Uppercase:</span> {upper_text}</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
