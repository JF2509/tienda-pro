import streamlit as st

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="Tienda Pro", layout="wide", page_icon="🛒")

# Ocultar menú técnico
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS (PRODUCTOS) ---
PRODUCTOS = [
    {"id": 1, "nombre": "Smartwatch Elite", "precio": 120.00, "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400", "cat": "Tecnología"},
    {"id": 2, "nombre": "Zapatillas Urban", "precio": 85.50, "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400", "cat": "Moda"},
    {"id": 3, "nombre": "Auriculares Pro", "precio": 199.00, "img": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400", "cat": "Sonido"},
    {"id": 4, "nombre": "Mochila Travel", "precio": 45.00, "img": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400", "cat": "Viaje"},
]

# --- MEMORIA (CARRITO) ---
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

def calcular_total():
    return sum(item['precio'] for item in st.session_state.carrito)

# --- MENÚ LATERAL ---
st.sidebar.title("🛍️ MI TIENDA")
menu = st.sidebar.radio("Ir a:", ["Catálogo", "Mi Carrito"])
st.sidebar.divider()
st.sidebar.metric("Total Carrito", f"${calcular_total():.2f}")

# --- PANTALLA 1: CATÁLOGO ---
if menu == "Catálogo":
    st.title("🔥 Novedades")
    st.write("Selección premium con envío rápido.")
    
    col1, col2 = st.columns(2)
    
    for i, prod in enumerate(PRODUCTOS):
        col = col1 if i % 2 == 0 else col2
        with col:
            st.image(prod['img'], use_column_width=True)
            st.subheader(prod['nombre'])
            st.write(f"**${prod['precio']}**")
            if st.button("Añadir", key=prod['id']):
                st.session_state.carrito.append(prod)
                st.toast(f"Añadido: {prod['nombre']}")
            st.divider()

# --- PANTALLA 2: PAGAR ---
elif menu == "Mi Carrito":
    st.title("🛒 Finalizar Compra")
    
    if len(st.session_state.carrito) > 0:
        for item in st.session_state.carrito:
            st.write(f"• {item['nombre']} - ${item['precio']}")
        
        st.divider()
        st.write(f"### Total a Pagar: ${calcular_total():.2f}")
        
        st.write("#### 🚚 Datos de Envío")
        with st.form("pedido"):
            st.text_input("Nombre Completo")
            st.text_input("Dirección")
            
            if st.form_submit_button("💳 PAGAR AHORA", type="primary"):
                st.success(f"¡Pedido recibido! (Simulación)")
                st.balloons()
                st.session_state.carrito = [] # Vaciar carrito
    else:
        st.info("Tu carrito está vacío.")
