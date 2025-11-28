import streamlit as st

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="Tienda Juan", layout="wide", page_icon="🛍️")

# --- ESTILOS CSS (MEJORADO) ---
st.markdown("""
    <style>
    /* Ocultamos solo el pie de página de Streamlit por defecto */
    footer {visibility: hidden;}
    
    /* Estilo para el pie de página legal propio */
    .legal-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f0f2f6;
        color: #555;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        z-index: 100;
        border-top: 1px solid #ddd;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS (PRODUCTOS) ---
PRODUCTOS = [
    {"id": 1, "nombre": "Smartwatch Elite", "precio": 120.00, "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400", "cat": "Tecnología"},
    {"id": 2, "nombre": "Zapatillas Urban", "precio": 85.50, "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400", "cat": "Moda"},
    {"id": 3, "nombre": "Auriculares Pro", "precio": 199.00, "img": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400", "cat": "Sonido"},
]

# --- MEMORIA (CARRITO) ---
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

def calcular_total():
    return sum(item['precio'] for item in st.session_state.carrito)

# --- NAVEGACIÓN (BARRA LATERAL VISIBLE) ---
st.sidebar.title("🛍️ MENÚ")
menu = st.sidebar.radio("Ir a:", ["Catálogo", "Mi Carrito", "Legal"])

# --- PANTALLA 1: CATÁLOGO ---
if menu == "Catálogo":
    st.title("🔥 Catálogo Premium")
    
    col1, col2 = st.columns(2)
    for i, prod in enumerate(PRODUCTOS):
        col = col1 if i % 2 == 0 else col2
        with col:
            st.image(prod['img'], use_column_width=True)
            st.write(f"**{prod['nombre']}**")
            st.write(f"${prod['precio']}")
            if st.button("Añadir", key=f"add_{prod['id']}"):
                st.session_state.carrito.append(prod)
                st.toast(f"¡{prod['nombre']} añadido al carrito!")
            st.divider()

# --- PANTALLA 2: CARRITO ---
elif menu == "Mi Carrito":
    st.title("🛒 Tu Cesta")
    if len(st.session_state.carrito) > 0:
        for i, item in enumerate(st.session_state.carrito):
            cols = st.columns([3, 1])
            cols[0].write(f"• {item['nombre']}")
            cols[1].write(f"${item['precio']}")
        st.divider()
        st.subheader(f"Total: ${calcular_total():.2f}")
        st.button("PAGAR AHORA", type="primary")
    else:
        st.info("El carrito está vacío.")

# --- PANTALLA 3: LEGAL ---
elif menu == "Legal":
    st.title("⚖️ Información Legal")
    st.markdown("### Términos y Condiciones")
    st.caption("Esta tienda es un proyecto de demostración gestionado por Juan.")
    st.markdown("### Política de Privacidad")
    st.caption("No guardamos datos reales de tarjetas de crédito. Los pedidos son simulados.")
    st.markdown("### Cookies")
    st.caption("Usamos cookies técnicas para recordar tu carrito de compra.")

# --- PIE DE PÁGINA (Footer) ---
st.markdown('<div class="legal-footer">© 2025 Tienda Juan - Todos los derechos reservados | <a href="#">Privacidad</a></div>', unsafe_allow_html=True)
