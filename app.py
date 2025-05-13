import streamlit as st
import re

st.set_page_config(page_title="Editor AI", layout="centered")
st.title("📝 Editor Testo AI")

testo_input = st.text_area("Incolla qui il tuo testo:", height=300)

def evidenzia_testo(testo):
    righe = testo.split('\n')
    risultato = []
    for riga in righe:
        if re.match(r'^\s*\d+[\.\)]\s+', riga) or re.match(r'^\s*[A-Z][a-z]+:', riga):
            risultato.append(f"**{riga.strip()}**")
        else:
            parole = riga.split()
            evidenziate = [f"**{p}**" if len(p) > 8 else p for p in parole]
            risultato.append(" ".join(evidenziate))
    return "\n".join(risultato)

if st.button("✨ Applica Formattazione"):
    if testo_input:
        st.markdown(evidenzia_testo(testo_input))
    else:
        st.warning("Inserisci un testo prima di procedere.")
