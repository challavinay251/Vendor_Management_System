Vendor Management System

Overview
--------
This is a Vendor Management System built using Django and Django REST Framework. The system handles vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

Features
--------
- Vendor Profile Management
- Purchase Order Tracking
- Vendor Performance Evaluation

Requirements
------------
- Python 3.x
- Django 4.x
- Django REST Framework

Setup Instructions
------------------
1. Clone the Repository
-----------------------
git clone https://github.com/yourusername/vendor-management-system.git
cd vendor-management-system

2. Create a Virtual Environment
-------------------------------
Create a virtual environment to isolate your dependencies:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies
-----------------------
Install the required dependencies using pip:
pip install -r requirements.txt

4. Apply Migrations
-------------------
Apply the initial database migrations:
python manage.py migrate

5. Create a Superuser
---------------------
Create a superuser account to access the Django admin interface:
python manage.py createsuperuser
Follow the prompts to set the superuser's username, email, and password.

6. Run the Development Server
-----------------------------
Start the Django development server:
python manage.py runserver
You can now access the application at http://127.0.0.1:8000/.

Testing Instructions
--------------------
See TESTING_INSTRUCTIONS.txt for details on how to run the test suite.

API Endpoints
-------------
Vendor Endpoints
----------------
- POST /api/vendors/: Create a new vendor.
- GET /api/vendors/: List all vendors.
- GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
- PUT /api/vendors/{vendor_id}/: Update a vendor's details.
- DELETE /api/vendors/{vendor_id}/: Delete a vendor.

Purchase Order Endpoints
------------------------
- POST /api/purchase_orders/: Create a purchase order.
- GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
- GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
- PUT /api/purchase_orders/{po_id}/: Update a purchase order.
- DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

Vendor Performance Endpoints
----------------------------
- GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics.

Accessing the Admin Interface
-----------------------------
You can access the Django admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials you created earlier.



Frontend Interface
------------------
- GET /vendors/: View the list of vendors.
- GET /purchase_orders/: View the list of purchase orders.

Contact
-------
For any questions or issues, please contact [your email] or create an issue in the repository.
