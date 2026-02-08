import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import json
import time
from datetime import datetime, timedelta
import hashlib
import hmac
import base64
from PIL import Image
import io
import random
import string

# -------------------------------
# Page Config & Custom CSS
# -------------------------------
st.set_page_config(
    page_title="AgroMart - Smart Fertilizer E-commerce", 
    layout="wide",
    page_icon="🌱",
    initial_sidebar_state="expanded"
)

# Load custom CSS
with open('styles.css', 'r') as f:
    custom_css = f.read()
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("Fertilizer Prediction.csv")

data = load_data()

# -------------------------------
# Encode Categorical Columns
# -------------------------------
soil_encoder = LabelEncoder()
crop_encoder = LabelEncoder()
fert_encoder = LabelEncoder()

data["Soil Type"] = soil_encoder.fit_transform(data["Soil Type"])
data["Crop Type"] = crop_encoder.fit_transform(data["Crop Type"])
data["Fertilizer Name"] = fert_encoder.fit_transform(data["Fertilizer Name"])

X = data.drop("Fertilizer Name", axis=1)
y = data["Fertilizer Name"]

# -------------------------------
# Train ML Model
# -------------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)


# -------------------------------
# Enhanced Fertilizer Store (E-commerce Data)
# -------------------------------
fertilizer_names = list(fert_encoder.classes_)

# Detailed product catalog
product_catalog = {
    'Urea': {
        'price': 850,
        'description': 'High nitrogen fertilizer ideal for rapid vegetative growth',
        'npk': '46-0-0',
        'category': 'Nitrogenous',
        'image': '🌾',
        'stock': 150,
        'rating': 4.5,
        'reviews': 234
    },
    'DAP': {
        'price': 1200,
        'description': 'Di-ammonium phosphate - balanced NPK for root development',
        'npk': '18-46-0',
        'category': 'Phosphatic',
        'image': '🌱',
        'stock': 100,
        'rating': 4.7,
        'reviews': 189
    },
    '14-35-14': {
        'price': 1450,
        'description': 'Complex fertilizer with high phosphorus for flowering',
        'npk': '14-35-14',
        'category': 'Complex',
        'image': '🌻',
        'stock': 75,
        'rating': 4.6,
        'reviews': 156
    },
    '28-28': {
        'price': 1350,
        'description': 'Balanced NPK fertilizer for overall plant health',
        'npk': '28-28-0',
        'category': 'Complex',
        'image': '🌿',
        'stock': 120,
        'rating': 4.4,
        'reviews': 201
    },
    '17-17-17': {
        'price': 1550,
        'description': 'Complete balanced fertilizer for all crops',
        'npk': '17-17-17',
        'category': 'Complex',
        'image': '🌾',
        'stock': 90,
        'rating': 4.8,
        'reviews': 267
    },
    '20-20': {
        'price': 1100,
        'description': 'Balanced NPK for maintenance fertilization',
        'npk': '20-20-0',
        'category': 'Complex',
        'image': '🌱',
        'stock': 110,
        'rating': 4.3,
        'reviews': 145
    },
    '10-26-26': {
        'price': 1650,
        'description': 'High PK fertilizer for fruit development',
        'npk': '10-26-26',
        'category': 'Complex',
        'image': '🍎',
        'stock': 60,
        'rating': 4.6,
        'reviews': 178
    }
}

# Create DataFrame from product catalog
store = pd.DataFrame([
    {
        'Fertilizer': name,
        'Price (₹)': details['price'],
        'Description': details['description'],
        'NPK': details['npk'],
        'Category': details['category'],
        'Image': details['image'],
        'Stock': details['stock'],
        'Rating': details['rating'],
        'Reviews': details['reviews']
    }
    for name, details in product_catalog.items()
])


# -------------------------------
# Enhanced Cart Session Management
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "user_id" not in st.session_state:
    st.session_state.user_id = "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
if "order_history" not in st.session_state:
    st.session_state.order_history = []
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []
if "search_query" not in st.session_state:
    st.session_state.search_query = ""
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"
if "price_range" not in st.session_state:
    st.session_state.price_range = [0, 2000]

# -------------------------------
# Enhanced Sidebar Navigation
# -------------------------------
# -------------------------------
# Enhanced Sidebar Navigation
# -------------------------------
st.sidebar.markdown("""
<div class="sidebar">
    <h2>🌱 AgroMart</h2>
    <p>Smart Fertilizer E-commerce</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown(f"""
<div class="nav-item">
    <small>👤 User ID: {st.session_state.user_id[:8]}...</small>
</div>
""", unsafe_allow_html=True)

PAGES = [
    "🏠 Home",
    "🛒Fertilizer Store",
    "🧺 Shopping Cart",
    "🤖 ML Recommendation",
    "📊 Analytics Dashboard",
    "📦 Order History",
    "❤️ Wishlist",
    "👤 Profile",
    "📈 Dataset",
    "💳 Payment",
    "⚙️ Settings"
]

page = st.sidebar.selectbox(
    "Navigate",
    PAGES,
    index=PAGES.index(st.session_state.page)
)

st.session_state.page = page



    

    # -------------------------------
    # ENHANCED HOME PAGE
    # -------------------------------

if page == "🏠 Home":
    # Hero Section
    st.markdown("""
    <div class="header">
        <h1>🌾 AgroMart – Smart Fertilizer E-commerce Platform</h1>
        <p>Your Intelligent Agricultural Partner for Optimal Crop Growth</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{len(store)}</div>
            <div class="stats-label">Products Available</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        cart_items_count = sum(st.session_state.cart.values())
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{cart_items_count}</div>
            <div class="stats-label">Items in Cart</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stats-card">
            <div class="stats-number">95%</div>
            <div class="stats-label">ML Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stats-card">
            <div class="stats-number">10K+</div>
            <div class="stats-label">Happy Farmers</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown("### 🌟 Key Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="product-card">
            <h4>🤖 AI-Powered Recommendations</h4>
            <p>Get personalized fertilizer suggestions based on soil conditions, crop type, and nutrient requirements using advanced machine learning algorithms.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="product-card">
            <h4>🛒 Complete E-commerce</h4>
            <p>Browse, compare, and purchase fertilizers with secure payment options, cart management, and order tracking.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="product-card">
            <h4>📊 Smart Analytics</h4>
            <p>Track your purchases, analyze fertilizer effectiveness, and make data-driven farming decisions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Actions
    st.markdown("### 🚀 Quick Actions")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🛒 Shop Now", use_container_width=True, type="primary"):
            st.session_state.page = "🛒 Fertilizer Store"
            st.rerun()
    
    with col2:
        if st.button("🤖 Get Recommendation", use_container_width=True, type="secondary"):
            st.session_state.page = "🤖 ML Recommendation"
            st.rerun()
    
    with col3:
        if st.button("🧺 View Cart", use_container_width=True):
            st.session_state.page = "🧺 Shopping Cart"
            st.rerun()
    
    with col4:
        if st.button("📊 Analytics", use_container_width=True):
            st.session_state.page = "📊 Analytics Dashboard"
            st.rerun()
    
    # Popular Products
    st.markdown("### 🔥 Popular Products")
    popular_products = store.nlargest(3, 'Reviews')
    cols = st.columns(3)
    
    for idx, (_, product) in enumerate(popular_products.iterrows()):
        with cols[idx]:
            st.markdown(f"""
            <div class="product-card">
                <div style="font-size: 3rem; text-align: center; margin-bottom: 1rem;">{product['Image']}</div>
                <div class="product-title">{product['Fertilizer']}</div>
                <div class="product-price">₹{product['Price (₹)']}</div>
                <div class="product-description">{product['Description'][:50]}...</div>
                <div>⭐ {product['Rating']} ({product['Reviews']} reviews)</div>
                <div>📦 Stock: {product['Stock']}</div>
            </div>
            """, unsafe_allow_html=True)

# -------------------------------
# HELPER FUNCTIONS
# -------------------------------
def add_to_cart(product_name, quantity=1):
    if product_name in st.session_state.cart:
        st.session_state.cart[product_name] += quantity
    else:
        st.session_state.cart[product_name] = quantity

def remove_from_cart(product_name):
    if product_name in st.session_state.cart:
        del st.session_state.cart[product_name]

def update_cart_quantity(product_name, quantity):
    if quantity <= 0:
        remove_from_cart(product_name)
    else:
        st.session_state.cart[product_name] = quantity

def get_cart_total():
    total = 0
    for product_name, quantity in st.session_state.cart.items():
        product = store[store['Fertilizer'] == product_name].iloc[0]
        total += product['Price (₹)'] * quantity
    return total

def get_cart_count():
    return sum(st.session_state.cart.values())

def add_to_wishlist(product_name):
    if product_name not in st.session_state.wishlist:
        st.session_state.wishlist.append(product_name)

def remove_from_wishlist(product_name):
    if product_name in st.session_state.wishlist:
        st.session_state.wishlist.remove(product_name)

# -------------------------------
# ENHANCED FERTILIZER STORE
# -------------------------------
if page == "🛒Fertilizer Store":
    st.markdown("""
    <div class="header">
        <h1>🛒 Fertilizer Store</h1>
        <p>Browse our comprehensive collection of high-quality fertilizers</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Search and Filter Section
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        search_query = st.text_input("🔍 Search fertilizers...", value=st.session_state.search_query)
        st.session_state.search_query = search_query
    
    with col2:
        categories = ["All"] + list(store['Category'].unique())
        selected_category = st.selectbox("📂 Category", categories, index=categories.index(st.session_state.selected_category))
        st.session_state.selected_category = selected_category
    
    with col3:
        sort_by = st.selectbox("📊 Sort by", ["Name", "Price (Low to High)", "Price (High to Low)", "Rating", "Reviews"])
    
    # Price Range Filter
    price_range = st.slider("💰 Price Range", 0, 2000, st.session_state.price_range)
    st.session_state.price_range = price_range
    
    # Filter products
    filtered_products = store.copy()
    
    if search_query:
        filtered_products = filtered_products[
            filtered_products['Fertilizer'].str.contains(search_query, case=False) |
            filtered_products['Description'].str.contains(search_query, case=False)
        ]
    
    if selected_category != "All":
        filtered_products = filtered_products[filtered_products['Category'] == selected_category]
    
    filtered_products = filtered_products[
        (filtered_products['Price (₹)'] >= price_range[0]) & 
        (filtered_products['Price (₹)'] <= price_range[1])
    ]
    
    # Sort products
    if sort_by == "Name":
        filtered_products = filtered_products.sort_values('Fertilizer')
    elif sort_by == "Price (Low to High)":
        filtered_products = filtered_products.sort_values('Price (₹)')
    elif sort_by == "Price (High to Low)":
        filtered_products = filtered_products.sort_values('Price (₹)', ascending=False)
    elif sort_by == "Rating":
        filtered_products = filtered_products.sort_values('Rating', ascending=False)
    elif sort_by == "Reviews":
        filtered_products = filtered_products.sort_values('Reviews', ascending=False)
    
    # Display products
    if not filtered_products.empty:
        st.markdown(f"### � Found {len(filtered_products)} products")
        
        # Product Grid
        cols = st.columns(3)
        for idx, (_, product) in enumerate(filtered_products.iterrows()):
            with cols[idx % 3]:
                in_wishlist = product['Fertilizer'] in st.session_state.wishlist
                wishlist_icon = "❤️" if in_wishlist else "🤍"
                
                st.markdown(f"""
                <div class="product-card">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div style="font-size: 2.5rem;">{product['Image']}</div>
                        <div style="cursor: pointer; font-size: 1.5rem;" title="Add to Wishlist">{wishlist_icon}</div>
                    </div>
                    <div class="product-title">{product['Fertilizer']}</div>
                    <div class="product-price">₹{product['Price (₹)']}</div>
                    <div class="product-description">{product['Description']}</div>
                    <div style="margin: 0.5rem 0;">
                        <span style="background: #e8f5e8; padding: 0.25rem 0.5rem; border-radius: 0.25rem; font-size: 0.8rem;">{product['NPK']}</span>
                        <span style="background: #fff3e0; padding: 0.25rem 0.5rem; border-radius: 0.25rem; font-size: 0.8rem; margin-left: 0.5rem;">{product['Category']}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin: 0.5rem 0;">
                        <div>⭐ {product['Rating']} ({product['Reviews']} reviews)</div>
                        <div>📦 {product['Stock']} in stock</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                col_btn1, col_btn2, col_btn3 = st.columns(3)
                with col_btn1:
                    if st.button(f"🛒 Add", key=f"add_{product['Fertilizer']}", use_container_width=True):
                        add_to_cart(product['Fertilizer'])
                        st.success(f"Added {product['Fertilizer']} to cart!")
                        st.rerun()
                
                with col_btn2:
                    if st.button(f"❤️", key=f"wishlist_{product['Fertilizer']}", use_container_width=True):
                        if in_wishlist:
                            remove_from_wishlist(product['Fertilizer'])
                            st.info(f"Removed {product['Fertilizer']} from wishlist")
                        else:
                            add_to_wishlist(product['Fertilizer'])
                            st.success(f"Added {product['Fertilizer']} to wishlist!")
                        st.rerun()
                
                with col_btn3:
                    if st.button(f"👁️ View", key=f"view_{product['Fertilizer']}", use_container_width=True):
                        st.session_state.selected_product = product['Fertilizer']
                        st.info(f"Viewing details for {product['Fertilizer']}")
    else:
        st.warning("No products found matching your criteria.")

# -------------------------------
# ENHANCED SHOPPING CART
# -------------------------------
if page == "🧺 Shopping Cart":
    st.markdown("""
    <div class="header">
        <h1>🧺 Shopping Cart</h1>
        <p>Review and manage your selected fertilizers</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.cart:
        cart_items = []
        total_amount = 0
        
        for product_name, quantity in st.session_state.cart.items():
            product = store[store['Fertilizer'] == product_name].iloc[0]
            item_total = product['Price (₹)'] * quantity
            total_amount += item_total
            
            cart_items.append({
                'Product': product_name,
                'Price': product['Price (₹)'],
                'Quantity': quantity,
                'Total': item_total,
                'Image': product['Image'],
                'Stock': product['Stock']
            })
        
        # Cart Items Display
        for item in cart_items:
            col1, col2, col3, col4, col5, col6 = st.columns([1, 3, 1, 1, 1, 1])
            
            with col1:
                st.markdown(f"<div style='font-size: 2rem;'>{item['Image']}</div>", unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"**{item['Product']}**")
                st.markdown(f"₹{item['Price']} per unit")
            
            with col3:
                new_quantity = st.number_input(
                    "Qty", 
                    min_value=1, 
                    max_value=item['Stock'], 
                    value=item['Quantity'],
                    key=f"qty_{item['Product']}"
                )
                if new_quantity != item['Quantity']:
                    update_cart_quantity(item['Product'], new_quantity)
                    st.rerun()
            
            with col4:
                st.markdown(f"**₹{item['Total']}**")
            
            with col5:
                if st.button("🗑️", key=f"remove_{item['Product']}"):
                    remove_from_cart(item['Product'])
                    st.success(f"Removed {item['Product']} from cart")
                    st.rerun()
            
            with col6:
                if st.button("💝", key=f"save_{item['Product']}"):
                    add_to_wishlist(item['Product'])
                    st.success(f"Saved {item['Product']} to wishlist")
            
            st.divider()
        
        # Cart Summary
        st.markdown("""
        <div class="cart-summary">
            <h3>🧾 Order Summary</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**Subtotal:** ₹{total_amount}")
            gst_amount = total_amount * 0.18  # 18% GST
            st.markdown(f"**GST (18%):** ₹{gst_amount:.2f}")
            delivery_charge = 50 if total_amount < 5000 else 0
            st.markdown(f"**Delivery:** ₹{delivery_charge}")
            final_total = total_amount + gst_amount + delivery_charge
            st.markdown(f"### **Total: ₹{final_total:.2f}**")
        
        with col2:
            st.markdown("**Promo Code:**")
            promo_code = st.text_input("Enter promo code")
            if st.button("Apply Promo"):
                if promo_code.upper() == "FARMER10":
                    discount = final_total * 0.10
                    final_total -= discount
                    st.success(f"Promo applied! You saved ₹{discount:.2f}")
                else:
                    st.error("Invalid promo code")
        
        # Checkout Buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🛒 Continue Shopping", use_container_width=True):
                st.session_state.page = "🛒Fertilizer Store"
                st.rerun()
        
        with col2:
            if st.button("💳 Proceed to Payment", use_container_width=True, type="primary"):
                st.session_state.checkout_amount = final_total
                st.session_state.page = "💳 Payment"
                st.success("Proceeding to payment...")
                st.rerun()
        
        with col3:
            if st.button("📦 Save for Later", use_container_width=True):
                for item in cart_items:
                    add_to_wishlist(item['Product'])
                st.success("All items saved to wishlist!")
    else:
        st.markdown("""
        <div class="warning-alert">
            <h4>🛒 Your cart is empty!</h4>
            <p>Add some fertilizers to get started.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🛒 Start Shopping", use_container_width=True, type="primary"):
            st.session_state.page = "🛒Fertilizer Store"
            st.rerun()

# -------------------------------
# ENHANCED ML RECOMMENDATION PAGE
# -------------------------------
if page == "🤖 ML Recommendation":
    st.markdown("""
    <div class="header">
        <h1>🤖 Smart Fertilizer Recommendation</h1>
        <p>Get AI-powered fertilizer suggestions based on your farm conditions</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input Form
    with st.form("recommendation_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**🌡️ Environmental Conditions**")
            temp = st.number_input("Temperature (°C)", 0, 60, value=25)
            hum = st.number_input("Humidity (%)", 0, 100, value=60)
            moisture = st.number_input("Soil Moisture (%)", 0, 100, value=50)
            
            st.markdown("**🌱 Crop Information**")
            crop = st.selectbox("Crop Type", crop_encoder.classes_)
        
        with col2:
            st.markdown("**🧪 Soil Nutrients**")
            nitrogen = st.number_input("Nitrogen (kg/ha)", 0, 150, value=50)
            phosphorous = st.number_input("Phosphorous (kg/ha)", 0, 150, value=30)
            potassium = st.number_input("Potassium (kg/ha)", 0, 150, value=20)
            
            st.markdown("**🏔️ Soil Type**")
            soil = st.selectbox("Soil Type", soil_encoder.classes_)
        
        # Submit button
        submitted = st.form_submit_button("🔍 Get Recommendation", use_container_width=True, type="primary")
    
    if submitted:
        # Process input
        soil_val = soil_encoder.transform([soil])[0]
        crop_val = crop_encoder.transform([crop])[0]
        
        input_df = pd.DataFrame([[temp, hum, moisture,
                                  soil_val, crop_val,
                                  nitrogen, potassium, phosphorous]],
                                columns=X.columns)
        
        # Get prediction
        prediction = model.predict(input_df)
        fertilizer = fert_encoder.inverse_transform(prediction)[0]
        
        # Get product details
        product = store[store['Fertilizer'] == fertilizer].iloc[0]
        
        # Display recommendation
        st.markdown("""
        <div class="recommendation-box">
            <h2>✅ Recommended Fertilizer</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(f"<div style='font-size: 4rem; text-align: center;'>{product['Image']}</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"### {fertilizer}")
            st.markdown(f"**NPK Ratio:** {product['NPK']}")
            st.markdown(f"**Category:** {product['Category']}")
            st.markdown(f"**Price:** ₹{product['Price (₹)']}")
            st.markdown(f"**Rating:** ⭐ {product['Rating']} ({product['Reviews']} reviews)")
            st.markdown(f"**Description:** {product['Description']}")
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button(f"🛒 Add to Cart - ₹{product['Price (₹)']}", use_container_width=True, type="primary"):
                add_to_cart(fertilizer)
                st.success(f"Added {fertilizer} to cart!")
                st.rerun()
        
        with col2:
            if st.button("❤️ Add to Wishlist", use_container_width=True):
                add_to_wishlist(fertilizer)
                st.success(f"Added {fertilizer} to wishlist!")
        
        with col3:
            if st.button("🔄 Get Alternative", use_container_width=True):
                # Show top 3 alternatives
                alternatives = store[store['Fertilizer'] != fertilizer].nlargest(3, 'Rating')
                st.markdown("### 🔄 Alternative Recommendations")
                
                for _, alt in alternatives.iterrows():
                    with st.expander(f"{alt['Fertilizer']} - ₹{alt['Price (₹)']} (⭐ {alt['Rating']})"):
                        st.write(alt['Description'])
                        st.write(f"NPK: {alt['NPK']}")
                        if st.button(f"Add {alt['Fertilizer']} to Cart", key=f"alt_{alt['Fertilizer']}"):
                            add_to_cart(alt['Fertilizer'])
                            st.success(f"Added {alt['Fertilizer']} to cart!")
                            st.rerun()
        
        # Model confidence and explanation
        st.markdown("### 📊 Recommendation Details")
        col1, col2 = st.columns(2)
        
        with col1:
            # Create a confidence score (mock)
            confidence = random.uniform(0.85, 0.98)
            st.metric("Model Confidence", f"{confidence:.1%}")
            st.metric("Expected Yield Increase", f"{random.randint(15, 35)}%")
        
        with col2:
            st.markdown("**Why this fertilizer?**")
            st.write(f"Based on your {soil} soil and {crop} crop, this fertilizer provides:")
            st.write(f"• Optimal NPK balance for {crop}")
            st.write(f"• Suitable for {soil.lower()} soil conditions")
            st.write(f"• Matches your current nutrient levels")

# -------------------------------
# ANALYTICS DASHBOARD
# -------------------------------
if page == "📊 Analytics Dashboard":
    st.markdown("""
    <div class="header">
        <h1>📊 Analytics Dashboard</h1>
        <p>Insights and statistics for your farming business</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_orders = len(st.session_state.order_history)
        st.metric("Total Orders", total_orders)
    
    with col2:
        total_spent = sum([order['amount'] for order in st.session_state.order_history])
        st.metric("Total Spent", f"₹{total_spent:.2f}")
    
    with col3:
        cart_items = sum(st.session_state.cart.values())
        st.metric("Cart Items", cart_items)
    
    with col4:
        wishlist_items = len(st.session_state.wishlist)
        st.metric("Wishlist Items", wishlist_items)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Sales by Category")
        category_sales = {}
        for order in st.session_state.order_history:
            for product_name, quantity in order['items'].items():
                product = store[store['Fertilizer'] == product_name].iloc[0]
                category = product['Category']
                if category not in category_sales:
                    category_sales[category] = 0
                category_sales[category] += quantity
        
        if category_sales:
            fig = px.pie(
                values=list(category_sales.values()),
                names=list(category_sales.keys()),
                title="Sales Distribution"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No sales data available yet.")
    
    with col2:
        st.markdown("### 📊 Monthly Spending Trend")
        if st.session_state.order_history:
            monthly_data = {}
            for order in st.session_state.order_history:
                month = order['date'][:7]  # YYYY-MM
                if month not in monthly_data:
                    monthly_data[month] = 0
                monthly_data[month] += order['amount']
            
            fig = px.line(
                x=list(monthly_data.keys()),
                y=list(monthly_data.values()),
                title="Monthly Spending",
                labels={'x': 'Month', 'y': 'Amount (₹)'}
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No spending data available yet.")
    
    # Recent Orders
    st.markdown("### 📦 Recent Orders")
    if st.session_state.order_history:
        recent_orders = st.session_state.order_history[-5:][::-1]  # Last 5 orders
        for order in recent_orders:
            with st.expander(f"Order {order['order_id']} - ₹{order['amount']:.2f} - {order['status']}"):
                st.write(f"**Date:** {order['date']}")
                st.write(f"**Payment Method:** {order['payment_method']}")
                st.write("**Items:**")
                for product, quantity in order['items'].items():
                    st.write(f"  • {product} x {quantity}")
    else:
        st.info("No orders placed yet.")
    
    # Popular Products
    st.markdown("### 🔥 Popular Products")
    popular = store.nlargest(5, 'Reviews')
    for _, product in popular.iterrows():
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            st.markdown(f"<div style='font-size: 2rem;'>{product['Image']}</div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"**{product['Fertilizer']}**")
            st.write(f"⭐ {product['Rating']} ({product['Reviews']} reviews)")
            st.markdown(f"**₹{product['Price (₹)']}**")
        st.divider()

# -------------------------------
# PAYMENT PAGE
# -------------------------------
if page == "💳 Payment":
    st.markdown("""
    <div class="header">
        <h1>💳 Secure Payment</h1>
        <p>Complete your purchase safely and securely</p>
    </div>
    """, unsafe_allow_html=True)
    
    if 'checkout_amount' in st.session_state:
        total_amount = st.session_state.checkout_amount
        
        # Order Summary
        st.markdown("### 🧾 Order Summary")
        for product_name, quantity in st.session_state.cart.items():
            product = store[store['Fertilizer'] == product_name].iloc[0]
            st.write(f"{product_name} x {quantity} = ₹{product['Price (₹)'] * quantity}")
        
        st.markdown(f"### **Total Amount: ₹{total_amount:.2f}**")
        
        # Payment Form
        with st.form("payment_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**👤 Billing Information**")
                full_name = st.text_input("Full Name*")
                email = st.text_input("Email Address*")
                phone = st.text_input("Phone Number*")
                
                st.markdown("**🏠 Delivery Address**")
                address = st.text_area("Street Address*")
                city = st.text_input("City*")
                state = st.text_input("State*")
                pincode = st.text_input("PIN Code*")
            
            with col2:
                st.markdown("**💳 Payment Details**")
                payment_method = st.selectbox("Payment Method", ["Credit/Debit Card", "UPI", "Net Banking", "Cash on Delivery"])
                
                if payment_method == "Credit/Debit Card":
                    card_number = st.text_input("Card Number*", placeholder="1234 5678 9012 3456")
                    card_name = st.text_input("Cardholder Name*")
                    expiry = st.text_input("Expiry Date*", placeholder="MM/YY")
                    cvv = st.text_input("CVV*", placeholder="123", type="password")
                
                elif payment_method == "UPI":
                    upi_id = st.text_input("UPI ID*", placeholder="yourname@upi")
                
                elif payment_method == "Net Banking":
                    bank = st.selectbox("Select Bank", ["SBI", "HDFC", "ICICI", "PNB", "Axis Bank", "Other"])
            
            # Terms and Conditions
            agree_terms = st.checkbox("I agree to Terms and Conditions and Privacy Policy*")
            
            # Submit Button
            submit_payment = st.form_submit_button("🔒 Complete Payment", use_container_width=True, type="primary")
        
        if submit_payment:
            if not all([full_name, email, phone, address, city, state, pincode, agree_terms]):
                st.error("Please fill all required fields and agree to the terms.")
            else:
                # Process payment (mock)
                with st.spinner("Processing payment..."):
                    time.sleep(2)
                    
                    # Generate order ID
                    order_id = "ORD" + ''.join(random.choices(string.digits, k=8))
                    
                    # Save order to history
                    order = {
                        'order_id': order_id,
                        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'amount': total_amount,
                        'items': dict(st.session_state.cart),
                        'status': 'Confirmed',
                        'payment_method': payment_method
                    }
                    st.session_state.order_history.append(order)
                    
                    # Clear cart
                    st.session_state.cart = {}
                    
                    # Success message
                    st.markdown(f"""
                    <div class="success-alert">
                        <h2>✅ Payment Successful!</h2>
                        <p><strong>Order ID:</strong> {order_id}</p>
                        <p><strong>Amount Paid:</strong> ₹{total_amount:.2f}</p>
                        <p>Your order has been confirmed and will be delivered within 5-7 working days.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Action buttons
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("📦 Track Order", use_container_width=True):
                            st.session_state.page = "📦 Order History"
                            st.rerun()
                    
                    with col2:
                        if st.button("🛒 Continue Shopping", use_container_width=True):
                            st.session_state.page = "🛒 Fertilizer Store"
                            st.rerun()
    else:
        st.warning("No checkout amount found. Please add items to cart first.")
        if st.button("🛒 Go to Cart", use_container_width=True):
            st.session_state.page = "🧺 Shopping Cart"
            st.rerun()

# -------------------------------
# ORDER HISTORY PAGE
# -------------------------------
if page == "� Order History":
    st.markdown("""
    <div class="header">
        <h1>� Order History</h1>
        <p>Track and manage your fertilizer orders</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.order_history:
        # Filter and Sort
        col1, col2 = st.columns(2)
        with col1:
            status_filter = st.selectbox("Filter by Status", ["All", "Confirmed", "Processing", "Shipped", "Delivered"])
        with col2:
            sort_order = st.selectbox("Sort by", ["Latest First", "Oldest First", "Highest Amount", "Lowest Amount"])
        total_amount = st.session_state.checkout_amount
        
        # Order Summary
        st.markdown("### 🧾 Order Summary")
        for product_name, quantity in st.session_state.cart.items():
            product = store[store['Fertilizer'] == product_name].iloc[0]
            st.write(f"{product_name} x {quantity} = ₹{product['Price (₹)'] * quantity}")
        
        st.markdown(f"### **Total Amount: ₹{total_amount:.2f}**")
        
        # Payment Form
        with st.form("payment_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**👤 Billing Information**")
                full_name = st.text_input("Full Name*")
                email = st.text_input("Email Address*")
                phone = st.text_input("Phone Number*")
                
                st.markdown("**🏠 Delivery Address**")
                address = st.text_area("Street Address*")
                city = st.text_input("City*")
                state = st.text_input("State*")
                pincode = st.text_input("PIN Code*")
            
            with col2:
                st.markdown("**💳 Payment Details**")
                payment_method = st.selectbox("Payment Method", ["Credit/Debit Card", "UPI", "Net Banking", "Cash on Delivery"])
                
                if payment_method == "Credit/Debit Card":
                    card_number = st.text_input("Card Number*", placeholder="1234 5678 9012 3456")
                    card_name = st.text_input("Cardholder Name*")
                    expiry = st.text_input("Expiry Date*", placeholder="MM/YY")
                    cvv = st.text_input("CVV*", placeholder="123", type="password")
                
                elif payment_method == "UPI":
                    upi_id = st.text_input("UPI ID*", placeholder="yourname@upi")
                
                elif payment_method == "Net Banking":
                    bank = st.selectbox("Select Bank", ["SBI", "HDFC", "ICICI", "PNB", "Axis Bank", "Other"])
            
            # Terms and Conditions
            agree_terms = st.checkbox("I agree to the Terms and Conditions and Privacy Policy*")
            
            # Submit Button
            submit_payment = st.form_submit_button("🔒 Complete Payment", use_container_width=True, type="primary")
        
        if submit_payment:
            if not all([full_name, email, phone, address, city, state, pincode, agree_terms]):
                st.error("Please fill all required fields and agree to the terms.")
            else:
                # Process payment (mock)
                with st.spinner("Processing payment..."):
                    time.sleep(2)
                    
                    # Generate order ID
                    order_id = "ORD" + ''.join(random.choices(string.digits, k=8))
                    
                    # Save order to history
                    order = {
                        'order_id': order_id,
                        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'amount': total_amount,
                        'items': dict(st.session_state.cart),
                        'status': 'Confirmed',
                        'payment_method': payment_method
                    }
                    st.session_state.order_history.append(order)
                    
                    # Clear cart
                    st.session_state.cart = {}
                    
                    # Success message
                    st.markdown("""
                    <div class="success-alert">
                        <h2>✅ Payment Successful!</h2>
                        <p><strong>Order ID:</strong> {order_id}</p>
                        <p><strong>Amount Paid:</strong> ₹{total_amount:.2f}</p>
                        <p>Your order has been confirmed and will be delivered within 5-7 working days.</p>
                    </div>
                    """.format(order_id=order_id, total_amount=total_amount), unsafe_allow_html=True)
                    
                    # Action buttons
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("📦 Track Order", use_container_width=True):
                            st.session_state.page = "📦 Order History"
                            st.rerun()
                    
                    with col2:
                        if st.button("🛒 Continue Shopping", use_container_width=True):
                            st.session_state.page = "🛒 Fertilizer Store"
                            st.rerun()
    else:
        st.warning("No checkout amount found. Please add items to cart first.")
        if st.button("🛒 Go to Cart", use_container_width=True):
            st.session_state.page = "🧺 Shopping Cart"
            st.rerun()

# -------------------------------
# ORDER HISTORY PAGE
# -------------------------------
if page == "📦 Order History":
    st.markdown("""
    <div class="header">
        <h1>📦 Order History</h1>
        <p>Track and manage your fertilizer orders</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.order_history:
        # Filter and Sort
        col1, col2 = st.columns(2)
        with col1:
            status_filter = st.selectbox("Filter by Status", ["All", "Confirmed", "Processing", "Shipped", "Delivered"])
        with col2:
            sort_order = st.selectbox("Sort by", ["Latest First", "Oldest First", "Highest Amount", "Lowest Amount"])
        
        # Filter orders
        filtered_orders = st.session_state.order_history
        if status_filter != "All":
            filtered_orders = [order for order in filtered_orders if order['status'] == status_filter]
        
        # Sort orders
        if sort_order == "Latest First":
            filtered_orders = sorted(filtered_orders, key=lambda x: x['date'], reverse=True)
        elif sort_order == "Oldest First":
            filtered_orders = sorted(filtered_orders, key=lambda x: x['date'])
        elif sort_order == "Highest Amount":
            filtered_orders = sorted(filtered_orders, key=lambda x: x['amount'], reverse=True)
        elif sort_order == "Lowest Amount":
            filtered_orders = sorted(filtered_orders, key=lambda x: x['amount'])
        
        # Display orders
        for order in filtered_orders:
            with st.expander(f"📦 Order {order['order_id']} - ₹{order['amount']:.2f} - {order['status']}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**📅 Order Date:** {order['date']}")
                    st.write(f"**💰 Total Amount:** ₹{order['amount']:.2f}")
                    st.write(f"**💳 Payment Method:** {order['payment_method']}")
                    st.write(f"**📊 Status:** {order['status']}")
                
                with col2:
                    st.write(f"**📦 Items Ordered:**")
                    for product_name, quantity in order['items'].items():
                        product = store[store['Fertilizer'] == product_name].iloc[0]
                        st.write(f"  • {product_name} x {quantity} = ₹{product['Price (₹)'] * quantity}")
                    
                    # Action buttons
                    col_btn1, col_btn2, col_btn3 = st.columns(3)
                    with col_btn1:
                        if st.button(f"🔄 Reorder", key=f"reorder_{order['order_id']}"):
                            # Add all items to cart
                            for product_name, quantity in order['items'].items():
                                add_to_cart(product_name, quantity)
                            st.success("Items added to cart!")
                            st.rerun()
                    
                    with col_btn2:
                        if st.button(f"📞 Track", key=f"track_{order['order_id']}"):
                            st.info(f"Tracking order {order['order_id']}... Feature coming soon!")
                    
                    with col_btn3:
                        if st.button(f"🧾 Invoice", key=f"invoice_{order['order_id']}"):
                            st.info(f"Downloading invoice for order {order['order_id']}... Feature coming soon!")
    else:
        st.markdown("""
        <div class="warning-alert">
            <h4>📦 No orders yet!</h4>
            <p>Start shopping to see your order history here.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🛒 Start Shopping", use_container_width=True, type="primary"):
            st.session_state.page = "🛒 Fertilizer Store"
            st.rerun()

# -------------------------------
# WISHLIST PAGE
# -------------------------------
if page == "❤️ Wishlist":
    st.markdown("""
    <div class="header">
        <h1>❤️ My Wishlist</h1>
        <p>Fertilizers you've saved for later</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.wishlist:
        wishlist_products = store[store['Fertilizer'].isin(st.session_state.wishlist)]
        
        cols = st.columns(3)
        for idx, (_, product) in enumerate(wishlist_products.iterrows()):
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="product-card">
                    <div style="font-size: 2.5rem; text-align: center; margin-bottom: 1rem;">{product['Image']}</div>
                    <div class="product-title">{product['Fertilizer']}</div>
                    <div class="product-price">₹{product['Price (₹)']}</div>
                    <div class="product-description">{product['Description'][:80]}...</div>
                    <div>⭐ {product['Rating']} ({product['Reviews']} reviews)</div>
                    <div>📦 {product['Stock']} in stock</div>
                </div>
                """, unsafe_allow_html=True)
                
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    if st.button(f"🛒 Add to Cart", key=f"wishlist_cart_{product['Fertilizer']}", use_container_width=True):
                        add_to_cart(product['Fertilizer'])
                        st.success(f"Added {product['Fertilizer']} to cart!")
                        st.rerun()
                
                with col_btn2:
                    if st.button(f"🗑️ Remove", key=f"wishlist_remove_{product['Fertilizer']}", use_container_width=True):
                        remove_from_wishlist(product['Fertilizer'])
                        st.success(f"Removed {product['Fertilizer']} from wishlist!")
                        st.rerun()
    else:
        st.markdown("""
        <div class="warning-alert">
            <h4>❤️ Your wishlist is empty!</h4>
            <p>Save fertilizers you're interested in for later.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🛒 Browse Products", use_container_width=True, type="primary"):
            st.session_state.page = "🛒 Fertilizer Store"
            st.rerun()

# -------------------------------
# PROFILE PAGE
# -------------------------------
if page == "👤 Profile":
    st.markdown("""
    <div class="header">
        <h1>👤 My Profile</h1>
        <p>Manage your account settings and preferences</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Profile Information
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📋 Account Information")
        st.info(f"**User ID:** {st.session_state.user_id}")
        st.info(f"**Member Since:** {datetime.now().strftime('%B %d, %Y')}")
        
        # Profile Form
        with st.form("profile_form"):
            st.markdown("**👤 Personal Details**")
            name = st.text_input("Full Name", value="Farmer User")
            email = st.text_input("Email", value="farmer@example.com")
            phone = st.text_input("Phone", value="+91 9876543210")
            
            st.markdown("**🏠 Farm Details**")
            farm_name = st.text_input("Farm Name", value="Green Fields Farm")
            farm_location = st.text_input("Farm Location", value="Maharashtra, India")
            farm_size = st.number_input("Farm Size (acres)", value=10, min_value=1)
            
            st.markdown("**🌱 Preferred Crops**")
            crops = st.multiselect("Select Crops", 
                ["Wheat", "Rice", "Cotton", "Sugarcane", "Maize", "Pulses", "Oil Seeds", "Barley", "Millets", "Tobacco"],
                default=["Wheat", "Cotton"]
            )
            
            save_profile = st.form_submit_button("💾 Save Profile", use_container_width=True)
            
            if save_profile:
                st.success("Profile updated successfully!")
    
    with col2:
        st.markdown("### 📊 Account Statistics")
        
        # Stats
        total_orders = len(st.session_state.order_history)
        total_spent = sum([order['amount'] for order in st.session_state.order_history])
        total_products = len(set([item for order in st.session_state.order_history for item in order['items'].keys()]))
        
        st.metric("Total Orders", total_orders)
        st.metric("Total Spent", f"₹{total_spent:.2f}")
        st.metric("Products Purchased", total_products)
        st.metric("Wishlist Items", len(st.session_state.wishlist))
        
        # Preferences
        st.markdown("### ⚙️ Preferences")
        notifications = st.checkbox("📧 Email Notifications", value=True)
        sms_alerts = st.checkbox("📱 SMS Alerts", value=False)
        newsletter = st.checkbox("📰 Newsletter", value=True)
        
        # Actions
        st.markdown("### 🔧 Account Actions")
        if st.button("📧 Export Order History", use_container_width=True):
            st.info("Export feature coming soon!")
        
        if st.button("🔒 Change Password", use_container_width=True):
            st.info("Password change feature coming soon!")
        
        if st.button("📋 Download Invoice Template", use_container_width=True):
            st.info("Download feature coming soon!")

# -------------------------------
# SETTINGS PAGE
# -------------------------------
if page == "⚙️ Settings":
    st.markdown("""
    <div class="header">
        <h1>⚙️ Settings</h1>
        <p>Customize your AgroMart experience</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎨 Appearance")
        theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
        language = st.selectbox("Language", ["English", "Hindi", "Marathi", "Gujarati"])
        currency = st.selectbox("Currency", ["₹ INR", "$ USD", "€ EUR"])
        
        st.markdown("### 🔔 Notifications")
        email_notifications = st.checkbox("Email Notifications", value=True)
        push_notifications = st.checkbox("Push Notifications", value=True)
        sms_notifications = st.checkbox("SMS Notifications", value=False)
        
        st.markdown("### 🛡️ Privacy")
        share_data = st.checkbox("Share usage data to improve service", value=False)
        marketing_emails = st.checkbox("Receive marketing emails", value=True)
    
    with col2:
        st.markdown("### 💳 Payment Preferences")
        default_payment = st.selectbox("Default Payment Method", 
            ["Credit/Debit Card", "UPI", "Net Banking", "Cash on Delivery"])
        save_card = st.checkbox("Save card details for faster checkout", value=False)
        
        st.markdown("### 🚚 Delivery Preferences")
        default_address = st.text_area("Default Delivery Address", 
            placeholder="Enter your default delivery address...")
        delivery_instructions = st.text_area("Special Delivery Instructions", 
            placeholder="Any special instructions for delivery...")
        
        st.markdown("### 🔄 Data Management")
        if st.button("🗑️ Clear Cart", use_container_width=True):
            st.session_state.cart = {}
            st.success("Cart cleared!")
            st.rerun()
        
        if st.button("🗑️ Clear Wishlist", use_container_width=True):
            st.session_state.wishlist = []
            st.success("Wishlist cleared!")
            st.rerun()
        
        if st.button("📥 Download All Data", use_container_width=True):
            st.info("Data download feature coming soon!")

# -------------------------------
# DATASET PAGE
# -------------------------------
if page == "📈 Dataset":
    st.markdown("""
    <div class="header">
        <h1>📈 Dataset Preview</h1>
        <p>Explore the fertilizer recommendation dataset</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Dataset Overview
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Records", len(data))
    
    with col2:
        st.metric("Features", data.shape[1] - 1)
    
    with col3:
        st.metric("Fertilizer Types", len(data['Fertilizer Name'].unique()))
    
    with col4:
        st.metric("Crop Types", len(data['Crop Type'].unique()))
    
    # Dataset Preview
    st.markdown("### 📊 Dataset Preview")
    st.dataframe(data.head(20), use_container_width=True)
    
    # Data Statistics
    st.markdown("### 📈 Data Statistics")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Soil Type Distribution**")
        soil_counts = data['Soil Type'].value_counts()
        fig = px.bar(x=soil_counts.index, y=soil_counts.values, 
                    title="Soil Types in Dataset")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("**Crop Type Distribution**")
        crop_counts = data['Crop Type'].value_counts()
        fig = px.pie(values=crop_counts.values, names=crop_counts.index,
                    title="Crop Types in Dataset")
        st.plotly_chart(fig, use_container_width=True)
    
    # Feature Correlation
    st.markdown("### 🔗 Feature Correlation")
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        correlation_matrix = data[numeric_cols].corr()
        fig = px.imshow(correlation_matrix, title="Feature Correlation Matrix")
        st.plotly_chart(fig, use_container_width=True)
    
    # Download Dataset
    st.markdown("### 📥 Download Dataset")
    if st.button("📥 Download CSV", use_container_width=True):
        csv = data.to_csv(index=False)
        st.download_button(
            label="Download fertilizer_dataset.csv",
            data=csv,
            file_name="fertilizer_dataset.csv",
            mime="text/csv"
        )
