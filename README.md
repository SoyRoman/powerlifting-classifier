# Powerlifting Classifier

A web-based application powered by Machine Learning to classify powerlifting athletes into **novice**, **intermediate**, or **advanced** levels. Users can input their physical and training data to receive real-time predictions based on a trained model.

## Features

- Clean and responsive UI with a dark theme using Bootstrap 4  
- Predictive model for experience level classification  
- Interactive form with field validation and tooltips  
- Flask backend integration  
- Docker support for simple and fast deployment  

## Input Features

| Feature             | Description                                                  |
|--------------------|--------------------------------------------------------------|
| Age                | Athlete's age in years                                       |
| Sex                | Biological sex (0: Female, 1: Male)                          |
| Weight (kg)        | Athlete's body weight in kilograms                           |
| Height (cm)        | Athlete's height in centimeters                              |
| Total Lifted (kg)  | Combined max squat, bench press, and deadlift in kilograms   |
| Years Training     | Years of powerlifting training                               |
| Training Frequency | Training sessions per week                                   |

## Model Details

The classification model was trained using Scikit-learn and preprocessed with MinMax scaling. A KMeans clustering model is also included for exploratory grouping of lifters. The Flask backend can be easily adapted to load any `.pkl` model or even use other frameworks like TensorFlow or PyTorch.

## Installation & Run

1. **Clone the repository, install dependencies, or run with Docker**



```bash
# Clone the repository
git clone https://github.com/SoyRoman/powerlifting-classifier.git
cd powerlifting-classifier

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install Python dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Access from your browser
http://localhost:5000
