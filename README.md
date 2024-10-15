Here’s a **README** file tailored to your project titled **CSV Whisperer: Talk to Your Data**:

---

# 📊 CSV Whisperer: Talk to Your Data  
🚀 **Unlock Real-Time Insights from CSV Files with Natural Language Queries**

## Overview
**CSV Whisperer** empowers users to interact with their CSV data files through **natural language**. Built using the **Gemini API** and **PandasAI**, this application allows users to effortlessly query their CSV data and get real-time insights—no code required!

## Key Features
- **Upload CSV Files:** Effortlessly upload any CSV file for real-time processing.
- **Natural Language Queries:** Ask questions about your data in plain language, and get immediate responses.
- **Streamlit Interface:** A simple, interactive, and intuitive interface using Streamlit to handle all interactions.

## Technology Stack
- **Gemini API:** Leverages powerful natural language processing to understand user queries and generate intelligent responses.
- **PandasAI:** Manages data manipulation and querying for insights from the CSV files.
- **Streamlit:** Provides an easy-to-use and visually appealing interface for interacting with the app.

## Prerequisites

Ensure you have the following:

- **Python 3.8+**
- **Streamlit** installed to run the application.
- **Gemini API key** (Sign up to get an API key).

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nikhil80520/csv-whisperer-talk-to-your-data.git
cd csv-whisperer-talk-to-your-data
```

### 2. Install Dependencies

Use `pip` to install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Set Your Gemini API Key

You’ll need to set up your **Gemini API Key** as an environment variable to use the app. Once you have the key, add it to your environment variables:

For Linux/Mac:
```bash
export GEMINI_API_KEY="your_api_key"
```

For Windows (Command Prompt):
```bash
set GEMINI_API_KEY="your_api_key"
```

### 4. Run the Application

Start the application with Streamlit:

```bash
streamlit run app.py
```

Once the application is running, open your browser and visit `http://localhost:8501` to start interacting with your CSV files.
