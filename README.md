# Bridal Harmony🌸

A couture intelligence system that converts personal inputs and visual analysis into confident, couple-matched wedding outfit decisions.  

## 🌟 Overview

**Bridal Harmony MVP** allows users to:

1. Upload up to 3 skin images.
2. Receive personalized material suggestions.
3. View AI-generated explanations for each suggestion.
4. Preview material colors and download recommendations.

This MVP focuses on providing a **decision-making engine** designed to reduce anxiety and ensure confident boutique choices for couples.

## ⚡ Key Features

- Multi-image upload (up to 3 images)
- Real-time skin analysis:
  - Brightness
  - Skin tone
  - Redness
- Personalized material suggestions (Velvet, Chiffon, Silk, Satin)
- Material color swatches
- AI explanation powered by Google Gemini
- Downloadable suggestions
- Light/Dark mode support in Streamlit
- Simple safety check for uploaded images

## 🛠 Tech Stack

- Python 3.11+
- Streamlit 1.52.2
- Pillow 12.0.0
- NumPy 2.2.6
- OpenCV 4.12.0
- Pandas 2.3.3
- `google-genai` 1.56.0
- `python-dotenv` 1.2.1

## 🚀 Quick Start

1. Clone the repo:

git clone <your-repo-url>
cd bridal-harmony-mvp

2. Install dependencies:

pip install -r requirements.txt

3. Add your Gemini API Key in .env:

GEMINI_API_KEY=your_api_key_here

4. Run the app:

streamlit run app.py

📂 Project Structure:

bridal-harmony-mvp/
│
├── app.py                # Main Streamlit app
├── skin_analysis.py      # Image analysis logic
├── material_logic.py     # Rules for material suggestions
├── explanation.py        # AI explanation using Gemini
├── utils.py              # Helper functions
├── requirements.txt      # Required libraries
├── .env                  # Gemini API key
└── README.md             # This file

🎯 How It Works

1. Upload Images → The app validates and processes the images.

2. Skin Analysis Engine → Measures brightness, redness, and skin tone.

3. Material Logic Engine → Suggests fabrics based on skin metrics.

4. AI Explanation Engine → Generates a personalized explanation for the suggested materials.

5. Frontend Display → Shows the original image, skin metrics, suggested materials, color swatches, and AI explanation. Users can download suggestions.

Bridal Harmony — turning personal inputs and visual insights into confident, boutique-ready wedding outfit decisions. 🌸
