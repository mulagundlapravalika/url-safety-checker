from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# 🔴 Blacklist sites
BLACKLIST = [
    "fakebank.com",
    "malicious.com",
    "phishing-site.net",
    "login-secure.xyz"
]

# 🔍 suspicious patterns
def is_suspicious(url):
    patterns = [
        r"login",
        r"bank",
        r"verify",
        r"secure",
        r"\.xyz$",
        r"\.top$",
        r"-login"
    ]

    for pattern in patterns:
        if re.search(pattern, url):
            return True
    return False

# 🏠 HOME ROUTE (IMPORTANT)
@app.route("/")
def home():
    return "URL Safety Checker API is Running ✅"

# 🔐 MAIN API ROUTE (POST ONLY)
@app.route("/check", methods=["POST"])
def check_url():
    data = request.get_json()
    url = data.get("url", "").lower()

    # 1. blacklist check
    for site in BLACKLIST:
        if site in url:
            return jsonify({"result": "❌ Dangerous Website (Blacklisted)"})

    # 2. suspicious check
    if is_suspicious(url):
        return jsonify({"result": "⚠️ Suspicious Website"})

    # 3. format check
    if not url.startswith("http"):
        return jsonify({"result": "⚠️ Invalid URL Format"})

    return jsonify({"result": "✅ Safe Website"})


if __name__ == "__main__":
    app.run(debug=True)