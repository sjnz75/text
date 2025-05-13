import streamlit as st
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

st.set_page_config(page_title="Editor Editoriale AI", layout="wide")

st.title("🖋️ Editor Editoriale – Analisi automatica titoli e parole chiave")

# Funzione per trovare le parole chiave principali con TF-IDF
def estrai_parole_chiave(text, num_keywords=10):
    vectorizer = TfidfVectorizer(stop_words='italian')
    tfidf_matrix = vectorizer.fit_transform([text])
    scores = zip(vectorizer.get_feature_names_out(), tfidf_matrix.toarray()[0])
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    keywords = [word for word, score in sorted_scores[:num_keywords]]
    return keywords

# Funzione per rendere in grassetto le parole chiave trovate
def evidenzia_keywords(text, keywords):
    for kw in keywords:
        text = re.sub(rf'\b({re.escape(kw)})\b', r'**\1**', text, flags=re.IGNORECASE)
    return text

# Funzione per rendere in grassetto i titoli (es. che finiscono con ":")
def evidenzia_titoli(text):
    lines = text.split("\n")
    formatted = []
    for line in lines:
        if line.strip().endswith(":") or line.strip().startswith("#"):
            formatted.append(f"**{line.strip()}**")
        else:
            formatted.append(line)
    return "\n".join(formatted)

# Input utente
user_text = st.text_area("Inserisci il tuo testo qui:", height=300)

if user_text.strip():
    # Estrai parole chiave
    parole_chiave = estrai_parole_chiave(user_text, num_keywords=8)

    # Applica le trasformazioni
    testo_con_kw = evidenzia_keywords(user_text, parole_chiave)
    testo_formattato = evidenzia_titoli(testo_con_kw)

    # Mostra risultato
    st.markdown("### 🔍 Parole chiave trovate:")
    st.write(", ".join(parole_chiave))

    st.markdown("### ✨ Testo formattato")
    st.markdown(testo_formattato)
else:
    st.info("Inserisci un testo nel campo sopra per avviare l'analisi.")
