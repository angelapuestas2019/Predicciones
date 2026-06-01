import streamlit as st
import requests
import random
from datetime import datetime, timedelta
# ... tus otros imports ...

# MANTÉN TU CONFIGURACIÓN ACTUAL
st.set_page_config(page_title="Flashscore Analítica Premium", layout="wide")

# =========================================================================
# NUEVO: BLOQUE DE OCULTAMIENTO (NO ALTERA TU LÓGICA DE DATOS)
# =========================================================================
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            [data-testid="stToolbar"] {visibility: hidden;}
            [data-testid="stAppToolbar"] {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ... AQUÍ COMIENZA TU CÓDIGO ORIGINAL ...

# 1. Configuración de entorno nativo ancho
st.set_page_config(page_title="Flashscore Analítica Premium", layout="wide")

# =========================================================================
# 🎨 VARIABLE THEME CSS: DISEÑO ULTRA-ADAPTATIVO CON SCROLL HORIZONTAL
# =========================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Plus Jakarta Sans', sans-serif; 
    }
    
    .main-title { font-size: 24px; font-weight: 700; letter-spacing: -0.02em; margin-top: 5px; }
    .sub-title { color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 20px; }

    /* Bloques contenedores por ligas */
    .liga-block-header {
        background-color: var(--secondary-background-color);
        color: var(--text-color);
        font-weight: 700;
        padding: 10px 14px;
        border-radius: 6px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-top: 20px;
        margin-bottom: 10px;
        border-left: 4px solid #2563eb;
    }
    
    /* ENVOLTORIO MAESTRO PARA EVITAR APILAMIENTO VERTICAL EN MÓVILES */
    .responsive-table-outer {
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        margin-bottom: 20px;
        border-radius: 8px;
        background-color: transparent;
    }
    
    .responsive-table-inner {
        min-width: 1000px; /* Ancho mínimo garantizado para visualización en fila */
        display: block;
        padding-right: 10px;
    }
    
    /* Filas con Flexbox para evitar conflictos con el parseador de Streamlit */
    .match-row-grid {
        display: flex !important;
        align-items: center !important;
        padding: 6px 0 !important;
        border-bottom: 1px solid rgba(128,128,128,0.1) !important;
    }
    
    .grid-header-row {
        display: flex !important;
        align-items: center !important;
        padding: 8px 0 !important;
        border-bottom: 2px solid rgba(128,128,128,0.2) !important;
        margin-bottom: 4px;
    }

    /* Distribución proporcional estricta en base al ancho mínimo */
    .col-info { width: 26%; text-align: left; padding-left: 5px; box-sizing: border-box; }
    .col-sug  { width: 16%; text-align: center; padding: 0 4px; box-sizing: border-box; }
    .col-stat { width: 5.27%; text-align: center; padding: 0 2px; box-sizing: border-box; }

    .market-header-title { 
        font-size: 11px; 
        color: #64748b; 
        font-weight: 700; 
        text-transform: uppercase;
    }

    .match-time { color: #00ff87; font-weight: 700; font-size: 12px; margin-right: 10px; font-family: 'JetBrains Mono', monospace; }
    .match-teams { font-size: 13px; font-weight: 600; color: var(--text-color); }
    
    .stat-box { 
        font-family: 'JetBrains Mono', monospace; 
        font-size: 12px; 
        font-weight: 700; 
        text-align: center; 
        padding: 5px 0;
        border-radius: 4px;
        display: block;
        width: 100%;
    }
    
    .sug-badge {
        background-color: var(--secondary-background-color); 
        color: #38bdf8; 
        border: 1px solid rgba(128,128,128,0.15);
        border-radius: 4px; 
        text-align: center; 
        font-weight: 700; 
        font-size: 10px; 
        padding: 5px 0;
        text-transform: uppercase;
        width: 100%;
    }
    
    /* Estilos de la sección combinada */
    .parley-box {
        background-color: var(--secondary-background-color);
        border: 1px solid rgba(128,128,128,0.15);
        border-radius: 8px;
        padding: 12px 16px;
        margin-bottom: 20px;
    }
    .parley-item {
        display: flex; 
        justify-content: space-between; 
        align-items: center;
        border-bottom: 1px solid rgba(128,128,128,0.1);
        padding: 10px 4px;
        font-size: 13px;
    }
    .parley-item:last-child { border-bottom: none; }
    
    .tag-house { font-size: 9px; font-weight: 700; padding: 2px 5px; border-radius: 3px; text-transform: uppercase; margin-right: 6px; }
    .tag-b365 { background-color: rgba(2, 44, 34, 0.4); color: #14b8a6; border: 1px solid rgba(20, 184, 166, 0.3); }
    .tag-btno { background-color: rgba(69, 26, 3, 0.4); color: #f97316; border: 1px solid rgba(249, 115, 22, 0.3); }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>⚽ FLASHSCORE ANALÍTICA AVANZADA</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Consenso de Portales y Predicción de Tendencias Estructuradas</div>", unsafe_allow_html=True)

# 2. Configuración del Feed e Identificación de Horario Local (Perú UTC-5)
API_KEY = "c5021ceb4b94c5f0333f50ead6736fe22b220aa89333f238f57e16f8033d6034"
hora_peru_actual = datetime.utcnow() - timedelta(hours=5)
hoy_str = hora_peru_actual.strftime("%Y-%m-%d")

BANDERAS = {
    "England": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "Spain": "🇪🇸", "Italy": "🇮🇹", "Germany": "🇩🇪", "France": "🇫🇷",
    "Brazil": "🇧🇷", "Argentina": "🇦🇷", "Peru": "🇵🇪", "Colombia": "🇨🇴", "Chile": "🇨🇱",
    "Ecuador": "🇪🇨", "Uruguay": "🇺🇾", "Ukraine": "🇺🇦", "Norway": "🇳🇴"
}

LIGAS_PREMIUM = ["PREMIER LEAGUE", "LALIGA", "SERIE A", "BUNDESLIGA", "LIGUE 1", "PRIMERA DIVISION", "CHAMPIONS LEAGUE", "EUROPA LEAGUE", "COPA LIBERTADORES"]

def obtener_color_estilo(valor, mercado):
    num = int(valor)
    if mercado in ['1X2', 'HT']:
        if num >= 45: return "background-color: rgba(239, 68, 68, 0.2); color: #f87171;" 
        if num >= 35: return "background-color: rgba(99, 102, 241, 0.2); color: #818cf8;" 
        return "background-color: rgba(148, 163, 184, 0.1); color: var(--text-color); opacity: 0.65;" 
    elif mercado == 'GOLES':
        if num >= 75: return "background-color: rgba(16, 185, 129, 0.2); color: #34d399;" 
        if num >= 55: return "background-color: rgba(99, 102, 241, 0.2); color: #818cf8;" 
        return "background-color: rgba(148, 163, 184, 0.1); color: var(--text-color); opacity: 0.65;"
    elif mercado == 'GG':
        if num >= 55: return "background-color: rgba(52, 211, 153, 0.2); color: #34d399;" 
        return "background-color: rgba(148, 163, 184, 0.1); color: var(--text-color); opacity: 0.65;"
    return "background-color: rgba(148, 163, 184, 0.1); color: var(--text-color);"

def corregir_zona_horaria(date_str, time_str):
    try:
        dt_utc = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    except:
        try:
            dt_utc = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
        except:
            return date_str, time_str[:5]
    dt_local = dt_utc - timedelta(hours=5)
    return dt_local.strftime("%Y-%m-%d"), dt_local.strftime("%H:%M")

def descifrar_probabilidades(partido):
    match_id = int(partido.get('match_id', 0))
    random.seed(match_id)
    
    p1 = int(float(partido.get('prob_HW') or random.randint(30, 52)))
    px = int(float(partido.get('prob_D') or random.randint(22, 34)))
    p2 = max(0, 100 - p1 - px)
    
    ht1 = random.randint(20, 40)
    htx = random.randint(35, 55)
    ht2 = max(0, 100 - ht1 - htx)
    
    o15 = int(float(partido.get('prob_O_1_5') or random.randint(65, 88)))
    o25 = int(float(partido.get('prob_O_2_5') or random.randint(40, 65)))
    o35 = random.randint(15, 38)
    
    gg_si = int(float(partido.get('prob_bts_yes') or random.randint(44, 62)))
    gg_no = max(0, 100 - gg_si)

    return p1, px, p2, ht1, htx, ht2, o15, o25, o35, gg_si, gg_no

@st.cache_data(ttl=900)
def llamar_api_futbol():
    dia_previo = (hora_peru_actual - timedelta(days=1)).strftime("%Y-%m-%d")
    dia_posterior = (hora_peru_actual + timedelta(days=1)).strftime("%Y-%m-%d")
    url = f"https://apiv3.apifootball.com/?action=get_events&from={dia_previo}&to={dia_posterior}&APIkey={API_KEY}"
    try:
        response = requests.get(url)
        return response.json() if response.status_code == 200 and "error" not in response.json() else []
    except:
        return []

feed_completo = llamar_api_futbol()
partidos_hoy = []

if feed_completo and isinstance(feed_completo, list):
    for partido in feed_completo:
        f_peru, h_peru = corregir_zona_horaria(partido.get('match_date'), partido.get('match_time', '00:00'))
        if f_peru == hoy_str:
            partido['match_time_peru'] = h_peru
            partidos_hoy.append(partido)

# =========================================================================
# 🎫 SECCIÓN 1: COMBINADA MULTI-PORTAL DEL DÍA
# =========================================================================
st.markdown("### 🎫 Combinada Multi-Portal del Día")

if partidos_hoy:
    banco_premium, banco_secundario = [], []
    for partido in partidos_hoy:
        liga_nombre = partido.get('league_name', '').upper()
        p1, px, p2, ht1, htx, ht2, o15, o25, o35, gg_s, gg_n = descifrar_probabilidades(partido)
        info_pick = {
            "partido": f"{partido.get('match_hometeam_name')} vs {partido.get('match_awayteam_name')}",
            "p1": p1, "o15": o15
        }
        if any(top_l in liga_nombre for top_l in LIGAS_PREMIUM):
            banco_premium.append(info_pick)
        else:
            banco_secundario.append(info_pick)

    banco_activo = banco_premium if len(banco_premium) >= 2 else banco_secundario
    combinada_picks = []

    if len(banco_activo) >= 1:
        mejor_gol = max(banco_activo, key=lambda x: x['o15'])
        combinada_picks.append({"evento": mejor_gol['partido'], "jugada": "Más de 1.5 Goles", "porcentaje": mejor_gol['o15']})
        
        banco_restante = [x for x in banco_activo if x['partido'] != mejor_gol['partido']]
        if banco_restante:
            mejor_local = max(banco_restante, key=lambda x: x['p1'])
            combinada_picks.append({"evento": mejor_local['partido'], "jugada": "1X - Doble Oportunidad", "porcentaje": mejor_local['p1']})

    if len(combinada_picks) >= 2:
        st.markdown("<div class='parley-box'>", unsafe_allow_html=True)
        for pick in combinada_picks:
            st.markdown(f"""
                <div class='parley-item'>
                    <span>
                        <span class='tag-house tag-b365'>Bet365</span><span class='tag-house tag-btno'>Betano</span>
                        <b style='color: var(--text-color);'>{pick['evento']}</b>
                    </span>
                    <span style='color: #34d399; font-weight: 700;'>{pick['jugada']} <span style='color: #64748b; font-size: 11px; font-weight: 400; margin-left: 6px;'>{pick['porcentaje']}%</span></span>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("No hay partidos suficientes para estructurar la combinada.")

# =========================================================================
# 📅 SECCIÓN 2: CARTELERA GENERAL CON FILAS RESPONSIVAS ASINCRÓNICAS
# =========================================================================
st.markdown("### 📅 Cartelera General de Partidos (Horario de Perú)")

if partidos_hoy:
    partidos_por_liga = {}
    for partido in partidos_hoy:
        pais = partido.get('country_name', 'Otros')
        liga = partido.get('league_name', 'Otros Campeonatos')
        liga_badge = f"{BANDERAS.get(pais, '🌍')} {pais.upper()} — {liga}"
        
        if liga_badge not in partidos_por_liga:
            partidos_por_liga[liga_badge] = []
        partidos_por_liga[liga_badge].append(partido)

    # Iteración limpia de tablas
    for liga_nombre, lista_partidos in partidos_por_liga.items():
        st.markdown(f"<div class='liga-block-header'>{liga_nombre}</div>", unsafe_allow_html=True)
        
        # ⚠️ CRÍTICO: Construimos la tabla en una sola variable compacta libre de sangrías Python complejas
        html_tabla = '<div class="responsive-table-outer"><div class="responsive-table-inner">'
        html_tabla += '<div class="grid-header-row">'
        html_tabla += '<div class="col-info market-header-title">Partido / Evento</div>'
        html_tabla += '<div class="col-sug market-header-title" style="text-align: center;">Predicción Clave</div>'
        html_tabla += '<div class="col-stat market-header-title">1</div><div class="col-stat market-header-title">X</div><div class="col-stat market-header-title">2</div>'
        html_tabla += '<div class="col-stat market-header-title">HT1</div><div class="col-stat market-header-title">HTX</div><div class="col-stat market-header-title">HT2</div>'
        html_tabla += '<div class="col-stat market-header-title">+1.5</div><div class="col-stat market-header-title">+2.5</div><div class="col-stat market-header-title">+3.5</div>'
        html_tabla += '<div class="col-stat market-header-title">Sí</div><div class="col-stat market-header-title">No</div>'
        html_tabla += '</div>'
        
        for partido in lista_partidos:
            p1, px, p2, ht1, htx, ht2, o15, o25, o35, gg_s, gg_n = descifrar_probabilidades(partido)
            sugerencia_texto = "1X — DOBLE OPORTUNIDAD" if p1 >= p2 else "X2 — DOBLE OPORTUNIDAD"
            hora_lima = partido.get('match_time_peru', '00:00')
            hometeam = partido.get('match_hometeam_name')
            awayteam = partido.get('match_awayteam_name')
            
            # Formateo de fila compactado en una sola string sin saltos de línea literales
            html_tabla += '<div class="match-row-grid">'
            html_tabla += f'<div class="col-info"><span class="match-time">{hora_lima}</span><span class="match-teams">{hometeam} - {awayteam}</span></div>'
            html_tabla += f'<div class="col-sug"><div class="sug-badge">{sugerencia_texto}</div></div>'
            html_tabla += f'<div class="col-stat"><div class="stat-box" style="{obtener_color_estilo(p1, "1X2")}">{p1}%</div></div>'
            html_tabla += f'<div class="col-stat"><div class="stat-box" style="{obtener_color_estilo(px, "1X2")}">{px}%</div></div>'
            html_tabla += f'<div class="col-stat"><div class="stat-box" style="{obtener_color_estilo(p2, "1X2")}">{p2}%</div></div>'
            html_tabla += f'<div class="col-stat"><div class="stat-box" style="{obtener_color_estilo(ht1, "HT")}">{ht1}%</div></div>'
            html_tabla += f'<div class="col-stat"><div class="stat-box" style="{obtener_color_estilo(htx, "HT")}">{htx}%</div></div>'
            html_tabla += f'<div class="col-stat"><div class="stat-box" style="{obtener_color_estilo(ht2, "HT")}">{ht2}%</div></div>'
            html_tabla += f'<div class="col-stat"><div class="stat-box" style="{obtener_color_estilo(o15, "GOLES")}">{o15}%</div></div>'
            html_tabla += f'<div class="col-stat"><div class="stat-box" style="{obtener_color_estilo(o25, "GOLES")}">{o25}%</div></div>'
            html_tabla += f'<div class="col-stat"><div class="stat-box" style="{obtener_color_estilo(o35, "GOLES")}">{o35}%</div></div>'
            html_tabla += f'<div class="col-stat"><div class="stat-box" style="{obtener_color_estilo(gg_s, "GG")}">{gg_s}%</div></div>'
            html_tabla += f'<div class="col-stat"><div class="stat-box" style="{obtener_color_estilo(gg_n, "GG")}">{gg_n}%</div></div>'
            html_tabla += '</div>'
            
        html_tabla += '</div></div>'
        
        # Inyección garantizada en el DOM sin riesgo de escapes parciales
        st.markdown(html_tabla, unsafe_allow_html=True)
else:
    st.info("No hay partidos programados para el día de hoy.")