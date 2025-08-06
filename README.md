# 🤖 Amazon SageMaker Chatbot Project

This project demonstrates how to build a simple rule-based chatbot using **Amazon SageMaker** and Python. The chatbot accepts continuous user input, processes it with predefined logic, and generates interactive responses until the user exits the conversation.

---

## 📌 Features
- Continuous interactive loop
- 300+ smart, quirky, and fallback responses
- Easy to run on Amazon SageMaker Notebook Instances
- Clean structure ready for upgrade to ML/NLP models

---

## 📁 Project Structure

sagemaker-chatbot/
├── chatbot_loop.py              # Main chatbot script with interactive loop and responses
├── README.md                    # Project documentation
├── /screenshots/                # Screenshots of chatbot in SageMaker + terminal output
└── /notebooks/
    └── chatbot_sagemaker.ipynb  # Jupyter notebook version of the chatbot

---

---

## 🚀 How to Run

1. Launch an Amazon SageMaker notebook instance
2. Open a new Jupyter notebook (e.g., `chatbot_sagemaker.ipynb`)
3. Paste the chatbot Python code or run `chatbot_loop.py` in terminal
4. Chat with the bot! Type `quit` or `end` to stop the session

---

## 🔧 Technologies Used
- Amazon SageMaker
- Python 3
- Jupyter Notebooks

---

## 📸 Screenshots

| Chatbot Running | Terminal Interaction |
|-----------------|----------------------|
| ![Notebook](/Screenshot/Test.png) | ![Chat](/Screenshot/chat.png) |

---

## 🌐 Future Improvements
- Integrate HuggingFace Transformers or OpenAI API
- Deploy as RESTful API with SageMaker Endpoint
- Add memory/context retention

---

## 👤 Author

Samuel Opeyemi Oni  
[LinkedIn](https://www.linkedin.com/in/oni-samuel-6b1820267/) | [GitHub](https://github.com/OniSamuelOpeyemi)
