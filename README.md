# Drishti AI: Multimodal Visual Guide

**Drishti AI** (resembling 'Vision') is a smart, interactive web application built with Streamlit that leverages Google's **Gemini 3.1 Flash** model to provide advanced image analysis and natural language processing. 

The application is engineered with a **smart routing system** capable of handling text-only queries, image-only analysis, or simultaneous text-and-image inputs seamlessly. It also features a production-ready, custom **auto-clearing chat form** interface to ensure smooth user interactions.

---

##  Live Demo
https://drishti-ai-9d5wdc2xvkpfchfvgrbfze.streamlit.app/

---

##  Key Features
* **Multimodal Intelligence:** Analyzes both text and images dynamically using Google's latest `gemini-3.1-flash-lite` model.
* **Auto-Clearing Chat Interface:** Utilizes Streamlit session states and callback functions to clear user input fields immediately upon submission while retaining the backend processing data.
* **Responsive Sidebar:** Includes profile highlights, project background, and direct connection channels.
* **Production Secure:** Structured environmental separation using `.env` handling to prevent API key leaks.

---

##  Tech Stack & Libraries
* **Frontend UI:** Streamlit (Python-based framework)
* **AI Core engine:** Google Generative AI SDK (`google-generativeai`)
* **Image Processing:** Pillow (`PIL`)
* **Environment Management:** `python-dotenv`

---

##  Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rasdharidisha-280306/Drishti-AI.git](https://github.com/rasdharidisha-280306/Drishti-AI.git)
   cd Drishti-AI
