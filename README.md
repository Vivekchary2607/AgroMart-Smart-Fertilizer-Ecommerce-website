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
├── .env                 # Environment variables (create this)
└── assets/              # Static assets (images, etc.)
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
# Payment Gateway Configuration
STRIPE_PUBLIC_KEY=pk_test_your_stripe_public_key
STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret

# Database Configuration (for production)
DATABASE_URL=your_database_connection_string

# Email Configuration (for notifications)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password
```

## 🌐 Deployment Options

### 1. Streamlit Cloud (Recommended for Easy Deployment)
1. Push your code to GitHub
2. Connect your GitHub repository to Streamlit Cloud
3. Set environment variables in Streamlit Cloud dashboard
4. Deploy with one click

### 2. Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
heroku config:set STRIPE_PUBLIC_KEY=your_key
git push heroku main
```

### 3. AWS/Azure/GCP
Deploy using Docker or direct server deployment with proper environment configuration.

### 4. Self-Hosted VPS
```bash
# Install dependencies
pip install -r requirements.txt

# Run with Gunicorn for production
gunicorn --bind 0.0.0.0:8501 streamlit run app.py
```

## 💳 Payment Integration Setup

### Stripe Integration
1. Create a Stripe account at [stripe.com](https://stripe.com)
2. Get API keys from Stripe Dashboard
3. Add keys to environment variables
4. Uncomment Stripe payment code in `app.py`

### Razorpay Integration (India)
1. Create Razorpay account at [razorpay.com](https://razorpay.com)
2. Get API keys from Razorpay Dashboard
3. Add keys to environment variables
4. Configure webhook endpoints

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

## 🔒 Security Features

- **Secure Payment Processing**: PCI-compliant payment gateways
- **Data Encryption**: HTTPS encryption for all data transmission
- **Input Validation**: Sanitized user inputs to prevent attacks
- **Session Management**: Secure session handling
- **Privacy Protection**: GDPR-compliant data handling

## 🚀 Performance Optimization

- **Caching**: Streamlit's built-in caching for ML model and data
- **Lazy Loading**: Efficient data loading for large datasets
- **Image Optimization**: Compressed images for faster loading
- **Database Indexing**: Optimized queries for better performance

## 📱 Mobile Responsiveness

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- Various screen sizes and orientations

## 🌍 Multi-language Support

Currently supports:
- English (Primary)
- Hindi (Coming soon)
- Marathi (Coming soon)
- Gujarati (Coming soon)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and queries:
- Email: support@agromart.com
- Phone: +91-XXXX-XXXX-XX
- Documentation: [Link to documentation]

## 🔄 Version History

- **v1.0.0** - Initial release with core e-commerce features
- **v1.1.0** - Added ML recommendations and analytics
- **v1.2.0** - Enhanced UI/UX and mobile optimization
- **v2.0.0** - Complete payment integration and advanced features

## 🏆 Acknowledgments

- Streamlit team for the amazing framework
- Scikit-learn for ML capabilities
- Plotly for beautiful visualizations
- Agricultural experts for domain knowledge
- Open-source community for valuable libraries

---

**🌾 AgroMart - Empowering Farmers with Smart Agriculture Technology**
