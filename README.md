# 🌾 AgroMart - Smart Fertilizer E-commerce Platform

A comprehensive, AI-powered e-commerce platform for fertilizers with machine learning recommendations, complete shopping cart functionality, and secure payment processing.

## 🚀 Features

### 🛒 E-commerce Features
- **Product Catalog**: Browse and search through comprehensive fertilizer collection
- **Advanced Filtering**: Filter by category, price range, NPK ratio, and ratings
- **Shopping Cart**: Full-featured cart with quantity management and price calculations
- **Wishlist**: Save products for later purchase
- **Order History**: Track and manage all your orders
- **Secure Checkout**: Multiple payment methods (Card, UPI, Net Banking, COD)

### 🤖 AI-Powered Recommendations
- **ML Model**: Random Forest classifier trained on agricultural data
- **Smart Suggestions**: Personalized fertilizer recommendations based on:
  - Soil type and conditions
  - Crop type
  - Nutrient levels (NPK)
  - Environmental factors (temperature, humidity, moisture)
- **Confidence Scores**: Model accuracy and expected yield improvements

### 📊 Analytics & Insights
- **Dashboard**: Comprehensive analytics for spending and purchases
- **Visualizations**: Interactive charts for sales trends and category distribution
- **Order Tracking**: Monitor order status and delivery
- **Data Export**: Download order history and invoices

### 🎨 Modern UI/UX
- **Responsive Design**: Works seamlessly on desktop and mobile
- **Interactive Interface**: Smooth animations and transitions
- **Professional Styling**: Modern, agricultural-themed design
- **Accessibility**: User-friendly for farmers of all technical levels

## 🛠️ Technology Stack

- **Frontend**: Streamlit with custom CSS styling
- **Backend**: Python with Streamlit framework
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Data Visualization**: Plotly for interactive charts
- **Data Processing**: Pandas for data manipulation
- **Payment Integration**: Stripe/Razorpay (ready for integration)

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
```bash
git clone <repository-url>
cd agromart
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Access the application**
Open your browser and navigate to `http://localhost:8501`

## 📁 Project Structure

```
agromart/
├── app.py                 # Main application file
├── requirements.txt        # Python dependencies
├── styles.css            # Custom styling
├── README.md             # Project documentation
├── Fertilizer Prediction.csv  # Dataset for ML model
```

## 📊 Dataset Information

The ML model is trained on a comprehensive fertilizer recommendation dataset containing:
- **Environmental Data**: Temperature, humidity, soil moisture
- **Soil Types**: Sandy, Loamy, Black, Red, Clayey
- **Crop Types**: Wheat, Rice, Cotton, Sugarcane, Maize, Pulses, Oil Seeds, Barley, Millets, Tobacco
- **Nutrient Levels**: Nitrogen, Phosphorous, Potassium values
- **Fertilizer Recommendations**: 7 different fertilizer types with NPK ratios

## 🎯 Usage Guide

### For Farmers
1. **Browse Products**: Use the store to explore available fertilizers
2. **Get Recommendations**: Use ML recommendation for personalized suggestions
3. **Add to Cart**: Select quantities and add products to cart
4. **Checkout**: Complete purchase with preferred payment method
5. **Track Orders**: Monitor delivery status in order history

### For Administrators
1. **Analytics**: View sales trends and customer behavior
2. **Product Management**: Update product information and pricing
3. **Order Management**: Process and fulfill customer orders
4. **Customer Support**: Access customer data for support

## 📱 Mobile Responsiveness

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- Various screen sizes and orientations
- 
## 📝 License
Copyright © 2026 Vivek Chary

All rights reserved.
This source code may not be copied, modified, or distributed without explicit permission.


This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**🌾 AgroMart - Empowering Farmers with Smart Agriculture Technology**
