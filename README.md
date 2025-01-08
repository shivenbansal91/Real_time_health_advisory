# Real-Time Personalized Health Advisory System

## Overview

This project implements a **Real-Time Personalized Health Advisory System** that simulates health data, processes it in real-time, and provides actionable recommendations using **Retrieval-Augmented Generation (RAG)**. The system is built to demonstrate real-time data handling, intelligent processing, and dynamic visualization of personalized health insights.

### **Key Features**
- **Real-Time Data Generation**: Simulates health data, including heart rate, SpO₂, steps, and calories burned.
- **Data Processing**: Processes incoming data in real-time and detects anomalies like high heart rate or low SpO₂.
- **RAG Integration**: Leverages a knowledge base of predefined health recommendations to generate personalized advice dynamically.
- **Interactive Dashboard**: Displays real-time health metrics, insights, and recommendations using **Streamlit**.

---

## Project Components

### **1. Mock Data Generator**
The `mock_data_generator.py` script simulates real-time health data for:
- **Heart Rate (BPM)**: Randomly generated between 60 and 180.
- **SpO₂ (%)**: Randomly generated between 90 and 100.
- **Steps**: Simulates step counts between 0 and 20,000.
- **Calories Burned**: Randomly generated between 1,500 and 3,000.

The generated data is stored in `health_data.csv`.

---

### **2. Data Processing with RAG**
The `data_processor_with_rag.py` script processes the generated health data in real-time by:
- **Reading the latest health metrics** from `health_data.csv`.
- **Using a RAG model** with a knowledge base (`knowledge_base.json`) to provide actionable health insights.
- **Generating personalized recommendations**, such as:
  - "Your heart rate is too high! Consider resting."
  - "Low SpO₂ detected! Ensure you’re in a well-ventilated area."
  - "Great work! Stay hydrated after 10,000 steps."

Processed data and recommendations are saved to `processed_health_data.csv`.

---

### **3. Streamlit Dashboard**
The `dashboard.py` script uses **Streamlit** to provide a live, interactive dashboard that displays:
- **Real-Time Metrics**: Latest health metrics such as heart rate, SpO₂, steps, and calories.
- **Actionable Recommendations**: Based on the processed data.
- **Visual Insights**: Graphs showing trends in heart rate, steps, and SpO₂ over time.

---

## Files and Their Purpose

| **File**                     | **Description**                                                                 |
|------------------------------|---------------------------------------------------------------------------------|
| `mock_data_generator.py`     | Simulates real-time health data generation and writes it to `health_data.csv`.  |
| `data_processor_with_rag.py` | Processes health data in real-time and generates RAG-based recommendations.    |
| `dashboard.py`               | Interactive dashboard built with Streamlit for visualizing metrics and advice. |
| `knowledge_base.json`        | Stores predefined health recommendations used by the RAG model.                |
| `requirements.txt`           | Contains a list of Python dependencies for the project.                        |

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps to Set Up the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/real_time_health_advisory.git
   cd real_time_health_advisory
2. **Create a Virtual Environment:**
   *on windows:*
   ```bash
   python -m venv vez
   venv\Scripts\activate

3. **Install Dependencies: Install the required Python libraries**:
   ```bash
   pip install -r requirements.txt
## **How to Run the System**:
  
  **Step 1: Run the Mock Data Generator**:
  The **mock_data_generator.py** script generates real-time health data and writes it to **health_data.csv**. The simulated metrics include:

- Heart Rate: Random values between 60 and 180 BPM.
- Steps: Random values between 0 and 20,000.
- SpO₂ Levels: Random values between 90% and 100%.
- Calories Burned: Random values between 1,500 and 3,000.
  <br>
  Run the following command to start generating data:<br>
  ```bash
  python mock_data_generator.py
The script appends new data to the health_data.csv file every 2 seconds.
## **Step 2: Run the Data Processor with RAG**:
The data_processor_with_rag.py script:

1. Continuously reads the real-time data generated in health_data.csv.
2. Applies Retrieval-Augmented Generation (RAG) by referencing predefined health guidelines stored in knowledge_base.json.
3. Writes the processed data and personalized health recommendations to processed_health_data.csv.<br>
Execute the script using:<br>
  ```bash
  python data_processor_with_rag.py
  ```
<br>
The processor generates recommendations based on the following conditions:

- Heart Rate > 140 BPM: **"Your heart rate is too high! Consider resting or breathing exercises."**
- SpO₂ < 95%: **"Low SpO₂ detected! Ensure you are in a well-ventilated area."**
- Steps > 10,000: **"Great work! Stay hydrated."**
- Normal Metrics: **"All metrics look good. Keep maintaining a healthy lifestyle!"**

## **Step 3: Launch the Streamlit Dashboard**:
The **dashboard.py** script provides a real-time, interactive dashboard that visualizes:<br>

- Live Health Metrics: Displays the latest heart rate, steps, SpO₂, and calories.
- Recommendations: Displays actionable health tips dynamically based on processed data.
- Trends and Graphs: Showcases graphical insights into key metrics over time.<br>
  Run the following command to start the dashboard:<br>
  ```bash
  streamlit run dashboard.py
Once executed, open your browser and navigate to:
  ```bash
  http://localhost:8501
  ```











  

