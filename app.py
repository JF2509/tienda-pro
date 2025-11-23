import streamlit as st

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="Tienda Pro", layout="wide", page_icon="🛒")

# Ocultar menú de desarrollador para que parezca una web real
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS (SIMULADA) ---
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

# --- BARRA LATERAL (Navegación) ---
st.sidebar.title("🛍️ MI TIENDA")
menu = st.sidebar.radio("Ir a:", ["Catálogo", "Mi Carrito"])
st.sidebar.divider()
st.sidebar.metric("Total Carrito", f"${calcular_total():.2f}")

# --- PÁGINA: CATÁLOGO ---
if menu == "Catálogo":
    st.title("🔥 Novedades")
    st.write("Selección premium con envío rápido.")
    
    # Diseño GRID (2 columnas para móvil)
    col1, col2 = st.columns(2)
    
    for i, prod in enumerate(PRODUCTOS):
        # Alternar columnas
        col = col1 if i % 2 == 0 else col2
        with col:
            st.image(prod['img'], use_column_width=True)
            st.subheader(prod['nombre'])
            st.write(f"**${prod['precio']}**")
            if st.button("Añadir", key=prod['id']):
                st.session_state.carrito.append(prod)
                st.toast(f"Añadido: {prod['nombre']}")
            st.divider()

# --- PÁGINA: CARRITO Y PAGO ---
elif menu == "Mi Carrito":
    st.title("🛒 Finalizar Compra")
    
    if len(st.session_state.carrito) > 0:
        # Lista de items
        for item in st.session_state.carrito:
            col_izq, col_der = st.columns([3, 1])
            col_izq.write(f"• {item['nombre']}")
            col_der.write(f"${item['precio']}")
        
        st.divider()
        st.write(f"### Total a Pagar: ${calcular_total():.2f}")
        
        # Formulario de datos
        st.write("#### 🚚 Datos de Envío")
        with st.form("pedido"):
            nombre = st.text_input("Nombre Completo")
            direccion = st.text_input("Dirección")
            email = st.text_input("Email")
            
            # Botón de pago (Simulado por ahora)
            if st.form_submit_button("💳 PAGAR AHORA", type="primary"):
                if nombre and direccion:
                    st.success(f"¡Pedido recibido! Gracias {nombre}.")
                    st.balloons()
                    st.session_state.carrito = [] # Vaciar carrito
                else:
                    st.error("Por favor rellena todos los datos.")
    else:
        st.info("Tu carrito está vacío.")
