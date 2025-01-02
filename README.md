The project, titled "Car Inventory Management System," is a Python-based GUI application developed to manage car inventory, customer orders, and administrative tasks. Here’s a brief overview of the project and the steps followed:

**Overview**:
- **Objective**: Develop a system for inventory and client management using a graphical user interface.
- **Tools Used**:
  - **Frontend**: Tkinter for GUI development.
  - **Backend**: Python logic for functionality and MySQL for database management.
- **Features**:
  - Login authentication.
  - Adding and managing products.
  - Searching inventory.
  - Managing customer reservations (orders).
  - Password reset functionality.

**Steps Followed**:
1. **System Architecture**:
   - Designed a structured system integrating Python logic with a Tkinter-based GUI and MySQL database.

2. **Database Design**:
   - Created tables for:
     - `login`: User credentials storage.
     - `inventory`: Car details, including brand, model, and condition.
     - `orders`: Customer reservation tracking.
   - Implemented database operations like INSERT, SELECT, UPDATE, and DELETE.

3. **Login System**:
   - Built a secure login mechanism fetching user credentials from the `login` table and validating inputs.

4. **User Interface Design**:
   - Designed the GUI using Tkinter for functionalities like:
     - Adding and viewing products.
     - Showing inventory.
     - Searching for specific products.
     - Viewing and managing orders.

5. **Inventory and Order Management**:
   - Added validation checks to handle partial or invalid inputs.
   - Built a view to display inventory in tabular format with options for deletion.
   - Implemented order processing to verify inventory before shipping and update relevant tables.

6. **Password Reset**:
   - Enabled users to securely reset passwords with checks on minimum length and field matching.

7. **Conclusion**:
   - Delivered a functional small-scale inventory management system.
   - Proposed future improvements like role-based authentication and advanced search/reporting features.
