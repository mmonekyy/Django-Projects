# 🛍️ Minion Shop

## 📂 Project Structure
Shop
├── README.md
├── requirements.txt
├── manage.py
├── db.sqlite3
├── Templates/
│ ├── Accounts/
│ │ └── templates/
│ │ ├── urls.py
│ │ └── views.py
│ ├── Payments/
│ │ └── templates/
│ │ ├── models.py
│ │ ├── urls.py
│ │ └── views.py
│ └── Products/
│ ├── migrations/
│ └── templates/
│ ├── models.py
│ ├── urls.py
│ └── views.py
├── Media/
├── Static/
│ ├── css/
│ └── js/
## 🟡 Landing Page  
This is the page the user sees immediately upon entering the shop:

![About us](IMG_TO_README/About_us.png)

---

## 🧸 Product Page  
When the user clicks on **Minions**, they will see the product list:

![Shop](IMG_TO_README/Shop.png)

---

## 🛒 Add to Cart & Login  
When the user clicks the **"Add to cart"** button, the product will be added to the cart.  
However, they won’t be able to proceed to checkout without logging in first.  
They will be automatically redirected to the login or account creation page.

### 🔐 Login Page  
![Login](IMG_TO_README/Account_Management.png)

### 📝 Register Page  
![Register](IMG_TO_README/Account_Management_Register.png)

---

## 📦 Checkout Process  
Upon re-entering the cart, the user will be able to proceed to the checkout page.  
They will be required to:

- Enter their **shipping address**
- Provide their **ZIP code**
- Choose a **payment method**

After completing these steps, they will be redirected to a page with **bank transfer details**.

![Shopping Cart](IMG_TO_README/Shopping_Cart.png)

---

## ✅ Order Confirmation  
When everything is correctly filled out, the user will see a success confirmation page:

![Success](IMG_TO_README/Succes.png)

---

> Thank you for shopping at **Minion Shop**! 💛  
