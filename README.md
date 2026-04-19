
# FightStore

An e-commerce web application for buying fighting/combat video games across platforms like PSN and XBOX. Built with Django as a group project.

## About the Project

This was a **group project**. The application allows users to browse a catalogue of fighting games, search for products, add them to a session-based shopping cart, apply voucher codes for discounts, and complete purchases via Stripe.

### My Contributions

The features I was responsible for building:

- **Products** — Product catalogue with category filtering, product detail pages, pagination, and the staff-only "Add New Stock" feature
- **Search** — Full-text search across product names and descriptions with filtered results
- **Stripe Payment Integration** — Secure checkout flow using the Stripe API for processing payments, creating customers, and handling charges
- **Styling** — CSS styling and layout across the site using Bootstrap 5 and custom CSS

---

## Tech Stack

- **Backend:** Django 4.2.6 (Python)
- **Database:** SQLite3
- **Payments:** Stripe 7.4.0
- **Frontend:** Bootstrap 5, Django Crispy Forms
- **Images:** Pillow 10.1.0

## Features

- **Authentication:** Sign up, log in/out, password change & reset, custom user model with phone & date of birth fields
- **Product Catalogue:** Browse all products or filter by category, product detail pages, pagination (6 per page)
- **Shopping Cart:** Add/remove items, session-based cart persistence, real-time item counter
- **Stripe Checkout:** Secure payment processing with billing & shipping address capture
- **Transaction History:** View past orders and detailed transaction invoices (login required)
- **Voucher System:** Apply discount codes with time-based validity (0–100% off)
- **Search:** Search products by name or description
- **Staff Feature:** Add new stock restricted to users with staff status (via Django Admin groups)
- **Category Navigation:** Bottom navbar displaying all product categories
- **Terms & Conditions Page**
- **Django Admin** for full site management
- **UUID primary keys** on products and categories
- **JSON fixtures** for seeding the database
- **Static assets & image uploads** for product and category images

## Setup

```bash
# Clone the repository
git clone <repo-url>
cd CA2

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Load seed data
python manage.py loaddata shop/fixtures/shop.json

# Start the development server
python manage.py runserver
```

## Project Structure

| App | Purpose |
|-----|---------|
| `shop` | Product catalogue, categories, pagination |
| `cart` | Session-based shopping cart |
| `transaction` | Stripe payments, order history |
| `users` | Custom user model, authentication |
| `vouchers` | Discount code system |
| `search_app` | Product search |

## What I Learned

- How to integrate a **third-party payment API (Stripe)** into a Django application, including creating customers, handling tokens, and processing charges securely
- Building a **product catalogue** with category-based filtering, UUID primary keys, and pagination using Django's `Paginator`
- Implementing **full-text search** across multiple model fields using Django ORM queries (`Q` objects with `icontains`)
- Working with **Django's session framework** to persist cart data across requests without requiring authentication
- Using **context processors** to inject global data (cart count, category links) into every template
- Creating **custom template tags** to check user group membership for role-based access control
- Structuring a multi-app Django project with proper URL namespacing and separation of concerns
- Collaborating on a **group project** — coordinating features, avoiding merge conflicts, and integrating independently built apps into a single working application


## Screenshots

![HomePage](https://github.com/user-attachments/assets/9f05ea3f-662d-45f0-a490-4e21e22117d9)

![ProductDetails](https://github.com/user-attachments/assets/940afbd8-7202-4657-a15b-1699523108bd)

![PSN](https://github.com/user-attachments/assets/aa63b81a-b96e-45be-b8bb-980586b01921)

![XBOX](https://github.com/user-attachments/assets/df8bf0b8-257b-4944-bdce-3390a1683c5e)

![Transaction](https://github.com/user-attachments/assets/78c21177-6d4b-4f37-951a-a58948d8ff7f)

![TransactionDetail](https://github.com/user-attachments/assets/ec98ce88-234a-4609-9d05-ffaa90e0db8b)

![Reviews](https://github.com/user-attachments/assets/386cbae9-7943-4158-b07a-b244e611d582)

![Wishlist](https://github.com/user-attachments/assets/ed353ade-2e43-400d-a39e-7fd43d1d02b7)

![Wishlist2](https://github.com/user-attachments/assets/e7fd271a-d0eb-4645-b736-651516f99904)

---
