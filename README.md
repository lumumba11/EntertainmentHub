# 🎮 Entertainment Hub - Django E-Commerce Platform

Entertainment Hub is a Django-based e-commerce web application that allows users to browse and interact with movies and games. It includes features such as a cart, wishlist, product search, category browsing, and product management directly from the homepage.

---

## 🚀 Features

- 🏠 Homepage with Featured Products
- 🔍 Product Search Functionality
- 🛍️ Product Detail View
- 🛒 Shopping Cart with Quantity Tracking
- 💖 Wishlist Functionality
- 🧾 Contact and Privacy Policy Pages
- ➕ Add Products via Button (No Admin Login Required)
- 🎬 Category Filtering (Movies and Games)
- 🎨 Bootstrap 5 UI with Responsive Design

---

## 🧱 Tech Stack

- **Backend:** Django 4+
- **Frontend:** HTML, Bootstrap 5
- **Database:** SQLite3 (can be upgraded to PostgreSQL)
- **Static Handling:** `django.contrib.staticfiles`

---

## 📁 Project Structure

```
moistore/
├── manage.py
├── moistore/
│   └── settings.py
│   └── urls.py
├── store/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   ├── store/
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── product_detail.html
│   │   │   ├── wishlist.html
│   │   │   ├── cart.html
│   │   │   ├── add_product.html
│   │   │   ├── contact.html
│   │   │   └── privacy.html
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   └── media/
│       └── product/  # Uploaded product images
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/entertainment-hub.git
   cd entertainment-hub
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

---

## 📸 Media & Static Files

Ensure your media files (product images) are saved under:

```bash
/media/product/
```

In `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

---

## 🧪 Sample Data

You can add products manually using the homepage `➕ Add Product` button.

Each product can be assigned a **category** like `Movie` or `Game`.

---

## ✅ To Do

- [ ] Implement user registration and login (optional)
- [ ] Add checkout and payment integration
- [ ] Implement order tracking
- [ ] Add product ratings/reviews

---

## 📬 Contact

For questions or suggestions:

**TechWizard**  
nmabys90@gmail.com

---

## 📄 License

This project is licensed under the MIT License.
