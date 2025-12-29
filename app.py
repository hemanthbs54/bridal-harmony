import streamlit as st
from PIL import Image
from skin_analysis import analyze_skin
from material_logic import get_material_suggestion
from explanation import get_gemini_explanation

st.set_page_config(page_title="Bridal Harmony MVP 🌸", layout="centered", page_icon="🌸")

st.title("Bridal Harmony MVP 🌸")
st.write("Upload an image of the skin and get personalized material suggestions with AI explanation.")

# Multi-file upload
uploaded_files = st.file_uploader(
    "Choose up to 3 images...", accept_multiple_files=True, type=["jpg", "jpeg", "png"]
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            # Open image
            image = Image.open(uploaded_file)

            # Simple safety check
            if image.mode not in ("RGB", "RGBA"):
                st.warning(f"{uploaded_file.name} may not be a valid skin image.")
                continue

            st.subheader(f"Uploaded Image: {uploaded_file.name}")
            st.image(image, width=300, caption="Original Image")

            # Analyze skin
            result = analyze_skin(image)
            st.subheader("Skin Analysis Result:")
            st.json(result)

            # Get material suggestions
            materials = get_material_suggestion(result)
            st.subheader("Material Suggestion:")
            st.write(", ".join(materials))

            # Material swatch preview
            st.subheader("Material Color Preview:")
            colors = {
                "Velvet": "#800000",
                "Chiffon": "#F5DEB3",
                "Silk": "#C0C0C0",
                "Satin": "#FFD700",
            }
            for mat in materials:
                color_hex = colors.get(mat, "#CCCCCC")
                st.markdown(
                    f"<div style='width:80px;height:30px;background-color:{color_hex};display:inline-block;margin-right:10px;border:1px solid #000'></div>{mat}",
                    unsafe_allow_html=True,
                )

            # AI explanation using Gemini
            ai_explanation = get_gemini_explanation(
                f"Skin analysis: {result}. Suggested materials: {', '.join(materials)}"
            )
            st.subheader("AI Explanation:")
            st.write(ai_explanation)

            # Download button
            st.download_button(
                "Download Suggestions",
                data=ai_explanation,
                file_name=f"{uploaded_file.name.split('.')[0]}_suggestion.txt",
            )

        except Exception as e:
            st.error(f"Error processing {uploaded_file.name}: {e}")

st.write("💡 Tip: Use the Streamlit settings (⚙️ top-right) to switch light/dark mode for better demo visuals.")
