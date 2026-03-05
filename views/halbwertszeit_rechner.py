import streamlit as st
from functions.halbwertszeit import halbwertszeit, berechne_zeit_bis_menge, berechne_halbwertszyklen

st.title("🧪 Halbwertszeit Rechner")

st.write("Berechne die verbleibende Menge oder Zeit bei radioaktivem Zerfall")

# Wähle den Rechner-Modus
modus = st.radio("Wähle einen Modus:", ["Verbleibende Menge", "Zeit bis Menge", "Halbwertszyklen"])

with st.form("halbwertszeit_form"):
    if modus == "Verbleibende Menge":
        st.subheader("📊 Verbleibende Menge berechnen")
        st.latex(r"N(t) = N_0 \cdot \left(\frac{1}{2}\right)^{\frac{t}{t_{\frac{1}{2}}}}")
        
        N0 = st.number_input("Anfangsmenge (N₀):", min_value=0.1, value=100.0)
        t_half = st.number_input("Halbwertszeit (t_half):", min_value=0.1, value=10.0)
        t = st.number_input("Verstrichene Zeit (t):", min_value=0.0, value=20.0)
        
        submit_button = st.form_submit_button("Berechnen")
        if submit_button:
            result = halbwertszeit(N0, t_half, t)
            st.success(f"Verbleibende Menge: **{result:.4f}**")
    
    elif modus == "Zeit bis Menge":
        st.subheader("⏱️ Zeit bis Zielmenge berechnen")
        st.latex(r"t = t_{\frac{1}{2}} \cdot \log_2\left(\frac{N_0}{N}\right)")
        
        N0 = st.number_input("Anfangsmenge (N₀):", min_value=0.1, value=100.0)
        N = st.number_input("Zielmenge (N):", min_value=0.1, value=25.0)
        t_half = st.number_input("Halbwertszeit (t_half):", min_value=0.1, value=10.0)
        
        submit_button = st.form_submit_button("Berechnen")
        if submit_button:
            try:
                result = berechne_zeit_bis_menge(N0, N, t_half)
                st.success(f"Zeit bis Zielmenge: **{result:.4f}** Zeiteinheiten")
            except ValueError as e:
                st.error(str(e))
    
    else:  # Halbwertszyklen
        st.subheader("🔄 Halbwertszyklen berechnen")
        st.latex(r"n = \frac{t}{t_{\frac{1}{2}}}")
        
        t = st.number_input("Verstrichene Zeit (t):", min_value=0.0, value=30.0)
        t_half = st.number_input("Halbwertszeit (t_half):", min_value=0.1, value=10.0)
        
        submit_button = st.form_submit_button("Berechnen")
        if submit_button:
            result = berechne_halbwertszyklen(t, t_half)
            st.success(f"Anzahl der Halbwertszyklen: **{result:.4f}**")



