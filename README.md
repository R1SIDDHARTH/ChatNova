
# 🤖 ChatNova-(Terminal-Based Gemini Chatbot)

A simple command-line chatbot that uses Google's Gemini API to generate responses to your messages.

## ✨ Features

* 💬 Interactive terminal-based chat interface.
* 🧠 Utilizes the Gemini API for intelligent responses.
* 📜 Maintains conversation history for context-aware interactions.
* 🧹 Supports clearing the conversation history.
* 👋 Provides a welcome message and clear instructions.
* ⏳ Includes a "thinking" animation to indicate processing.
* ⚠️ Handles API errors gracefully.
* ⚙️ Supports specifying the Gemini model to use.

## ⚙️ Prerequisites

* 🐍 Python 3.6 or higher.
* ☁️ An active Google Cloud project with the Gemini API enabled.
* 🔑 A valid Gemini API key.

## 🛠️ Setup

1.  **Clone the repository** (if you have the code in a repository):
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install required libraries:**
    ```bash
    pip install requests
    ```

## 🚀 Getting Started

There are two ways to provide your Gemini API key to the chatbot:

**🔑 Method 1: Using the `--api-key` command-line argument**

Open your terminal or command prompt and navigate to the directory where you saved the `gemni-Ai.py` file. Then, run the script with your API key:

```bash
python gemni-Ai.py --api-key="YOUR_GEMINI_API_KEY"
````

**⚠️ Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.**

**🗝️ Method 2: Setting the `GEMINI_API_KEY` environment variable**

You can set your API key as an environment variable. This is generally a more secure way to handle sensitive information.

**🐧 On Linux/macOS:**

```bash
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
python gemni-Ai.py
```

**💻 On Windows (Command Prompt):**

```bash
set GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
python gemni-Ai.py
```

**\<0xF0\>\<0x9F\>\<0xAA\>\<0x9B\> On Windows (PowerShell):**

```powershell
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
python gemni-Ai.py
```

## 🧑‍💻 Usage

Once the chatbot is running, you will see a welcome message with instructions. Simply type your messages and press Enter. The chatbot will process your input and display the response from the Gemini API.

**✨ Special Commands:**

  * `exit`, `quit`, or `bye`: 👋 Ends the chatbot session.
  * `clear`: 🧹 Clears the current conversation history.

## ⚙️ Optional Arguments

  * `--model`: ⚙️ Specifies the Gemini model to use. The default is `gemini-1.5-flash`. You can explore other available models if needed (e.g., `gemini-pro`).

<!-- end list -->

```bash
python gemni-Ai.py --api-key="YOUR_GEMINI_API_KEY" --model="gemini-pro"
```

## ❗ Error Handling

The script includes basic error handling for API requests and missing API keys. If an error occurs, a descriptive message will be displayed.

## 🤝 Contributing

Contributions to this project are welcome\! Feel free to fork 🍴 the repository and submit pull requests 📤 with improvements or bug fixes.

## 🙏 Acknowledgements

  * 🧠 This project utilizes the powerful Gemini API from Google.

**⚠️ Note:** Remember to keep your API key secure and do not share it publicly.

```
```

## 📃 License

MIT License — Free to use with attribution.

## 👨‍💻 Author

Made with ❤️ by [R1SIDDHARTH](https://github.com/R1SIDDHARTH)

