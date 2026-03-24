
import streamlit as st
import pandas as pd  # Neu hinzugefügt: Pandas importieren, um DataFrames zu verwenden
from functions.halbwertszeit import halbwertszeit, berechne_zeit_bis_menge
from datetime import datetime
import pytz
from utils.data_manager import DataManager  # --- NEW CODE: import data manager ---
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

st.title("🧪 Halbwertszeit Rechner")

st.write("Berechne die verbleibende Menge oder Zeit bei radioaktivem Zerfall")

# Initialisiere st.session_state['data_df'], falls es noch nicht existiert
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = pd.DataFrame(columns=['Modus', 'N0', 't_half', 't', 'N', 'Result'])

# Wähle den Rechner-Modus
modus = st.radio("Wähle einen Modus:", ["Verbleibende Menge", "Zeit bis Menge"])

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
            
            # ---: Historie aktualisieren ---
            new_row = pd.DataFrame([{
                "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),  # Current swiss time
                'Modus': modus,
                'N0': N0,
                't_half': t_half,
                't': t,
                'N': None,  # Nicht relevant für diesen Modus
                'Result': result
            }])
            st.session_state['data_df'] = pd.concat([st.session_state['data_df'], new_row], ignore_index=True)
                        # ---: save data to data manager ---
            data_manager = DataManager()
            data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
            
    
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
                
                # ---: Historie aktualisieren ---
                new_row = pd.DataFrame([{
                    "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),  # Current swiss time
                    'Modus': modus,
                    'N0': N0,
                    't_half': t_half,
                    't': None,  # Nicht relevant für diesen Modus
                    'N': N,
                    'Result': result
                }])
                st.session_state['data_df'] = pd.concat([st.session_state['data_df'], new_row], ignore_index=True)
                                
                data_manager = DataManager()
                data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
            except ValueError as e:
                st.error(str(e))

# --- NEU: Historie-Tabelle anzeigen (außerhalb der Form, um persistent zu sein) ---
st.subheader("📋 Berechnungshistorie")
st.dataframe(st.session_state['data_df'])

# --- NEU: Diagramm erstellen ---
st.subheader("📊 Balkendiagramm der Messungen")
# Daten vorbereiten
df = st.session_state['data_df'].copy()
if not df.empty:
    # Sortiere nach timestamp (chronologische Reihenfolge beibehalten)
    df = df.sort_values('timestamp')
    
    # Füge eine fortlaufende Index-Spalte hinzu (beginnend bei 1)
    df['index'] = range(1, len(df) + 1)
    
    # Filtere nach Modus
    df_menge = df[df['Modus'] == 'Verbleibende Menge']
    df_zeit = df[df['Modus'] == 'Zeit bis Menge']
    
    # Erstelle Figur und Achsen
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Linke Y-Achse (rot) für "Verbleibende Menge"
    if not df_menge.empty:
        ax1.bar(df_menge['index'], df_menge['Result'], color='red', alpha=0.7, label='Verbleibende Menge')
    ax1.set_ylabel('Verbleibende Menge', color='red')
    ax1.tick_params(axis='y', labelcolor='red')
    
    # Rechte Y-Achse (blau) für "Zeit bis Menge"
    ax2 = ax1.twinx()
    if not df_zeit.empty:
        ax2.bar(df_zeit['index'], df_zeit['Result'], color='blue', alpha=0.7, label='Zeit bis Menge')
    ax2.set_ylabel('Zeit bis Menge', color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')
    
    # X-Achse anpassen 
    ax1.set_xlabel('Messungsnummer')
    plt.xticks(df['index'])  # Setze Ticks auf die Index-Werte
    
    # Titel und Legende
    plt.title('Balkendiagramm: Verbleibende Menge (rot) vs. Zeit bis Menge (blau)')
    fig.tight_layout()
    
    # Diagramm in Streamlit anzeigen
    st.pyplot(fig)
else:
    st.write("Keine Daten vorhanden, um ein Diagramm zu erstellen.")




        
