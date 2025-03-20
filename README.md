# 🎯 Host Header Injection Tester

A powerful Python tool designed to detect and test Host Header Injection vulnerabilities in web applications.

## 🚀 Features

- Tests multiple malicious host headers
- Automatic redirect detection
- Error handling and timeout management
- Clean and readable output format

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/vaibhavkubade/hostheader.git
cd hostheader
```

2. **Set up virtual environment**
```bash
python -m venv venv
```

3. **Activate virtual environment**

📍 Windows:
```bash
.\venv\Scripts\activate
```

📍 Unix/MacOS:
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install requests
```

## 🔧 Usage

1. Edit the `TARGET_URL` in `hostheader.py` to your target website
2. Run the script:
```bash
python hostheader.py
```

## 📝 Example Output
```
[*] Testing Host Header Injection on http://example.com
[+] Host Header Injection Possible! Redirected to: http://evil.com
[-] No redirection for Host: attacker.com
```

## ⚠️ Disclaimer

This tool is for educational purposes and authorized testing only. Do not use against systems you don't have permission to test.

## 📄 License

MIT License - feel free to use and modify as you like.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Contact

Your Name - Vaibhav Kubade (vaibhavkubade.in)
