import streamlit as st
import re

st.set_page_config(page_title="Editor Editoriale AI", layout="wide")

st.title("🖋️ Editor Editoriale – Bold Titoli e Parole Chiave")

# Input utente
user_text = st.text_area("Inserisci il tuo testo qui", height=300)

# Parole chiave da evidenziare (input manuale)
keywords_input = st.text_input("Parole chiave da evidenziare (separate da virgola)", "")

# Pulsante per processare il testo
if st.button("Applica Formattazione"):
    keywords = [kw.strip() for kw in keywords_input.split(",") if kw.strip()]

    # Funzione per evidenziare parole chiave
    def bold_keywords(text, keywords):
        for kw in keywords:
            text = re.sub(rf'\b({re.escape(kw)})\b', r'**\1**', text, flags=re.IGNORECASE)
        return text

    # Funzione per rendere in grassetto titoli (es: Titolo: ... o # Titolo)
    def bold_titles(text):
        lines = text.split("\n")
        formatted = []
        for line in lines:
            if line.strip().endswith(":") or line.strip().startswith("#"):
                formatted.append(f"**{line.strip()}**")
            else:
                formatted.append(line)
        return "\n".join(formatted)

    # Applica entrambe le formattazioni
    processed = bold_keywords(user_text, keywords)
    processed = bold_titles(processed)

    st.markdown("### Risultato Formattato")
    st.markdown(processed)

---

## 📄 File `requirements.txt`

```txt
streamlit
