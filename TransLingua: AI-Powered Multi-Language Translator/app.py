import streamlit as st
from deep_translator import GoogleTranslator

# ---------------- TRANSLATE FUNCTION ----------------
def translate_text(text, source_language, target_language):
    return GoogleTranslator(
        source=source_language.lower(),
        target=target_language.lower()
    ).translate(text)


# ---------------- ITINERARY FUNCTION ----------------
def generate_itinerary(destination):
    return f"""
Day 1:
- Explore famous landmarks of {destination}
- Visit local markets
- Try traditional food

Day 2:
- Visit museums and cultural sites
- Enjoy local street food
- Evening city walk

Day 3:
- Nature spots or nearby attractions
- Shopping for souvenirs
- Relax and explore hidden gems

Travel Tips:
- Try local cuisine
- Use public transport
- Carry water and essentials
"""


# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="TransLingua", page_icon="🌍")

st.title("🌍 TransLingua: Multi-Language Translator & Travel Planner")

menu = st.sidebar.selectbox(
    "Choose Feature",
    ["Language Translator", "Travel Itinerary Generator"]
)

if menu == "Language Translator":
    text = st.text_area("Enter text to translate:")
    languages = ["english", "hindi", "spanish", "french", "german", "chinese"]
    source_language = st.selectbox("Source Language", languages)
    target_language = st.selectbox("Target Language", languages)

    if st.button("Translate"):
        if text:
            result = translate_text(text, source_language, target_language)
            st.subheader("Translated Text:")
            st.write(result)
        else:
            st.warning("Please enter text.")

elif menu == "Travel Itinerary Generator":
    destination = st.text_input("Enter destination city:")
    if st.button("Generate Itinerary"):
        if destination:
            result = generate_itinerary(destination)
            st.subheader("Your Travel Plan:")
            st.write(result)
        else:
            st.warning("Please enter destination.")
