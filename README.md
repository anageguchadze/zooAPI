Animal Information API
This project is a RESTful API for managing information about animals and their categories. It is built with Django and Django REST Framework, allowing users to view, create, update, and delete animal data and categorize them based on specific criteria.

Features
Category Management: Create, retrieve, update, and delete animal categories.
Animal Management: Create, retrieve, update, and delete animals, along with their descriptions, habitats, diets, and conservation statuses.
Filtering: Search animals by name, category, and status using Django filters.
API Documentation: Auto-generated documentation using drf-yasg.
Project Structure
Models
Category: Defines animal categories with a name and description.
Animal: Defines animal details, including scientific name, habitat, diet, and conservation status, with a foreign key relationship to Category.
API Endpoints
Categories:
GET /categories/: List all categories.
POST /categories/: Create a new category.
GET /categories/<id>/: Retrieve, update, or delete a category by ID.
Animals:
GET /animals/: List all animals (with filtering support).
POST /animals/: Create a new animal entry.
GET /animals/<id>/: Retrieve, update, or delete an animal by ID.
Filters
Use query parameters like name, category, and status on the /animals/ endpoint to filter animal entries.
Setup and Installation

Clone the repository:
bash
git clone https://github.com/yourusername/animal-info-api.git
cd animal-info-api
Create a virtual environment (recommended):

bash
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
Install dependencies:

bash
pip install -r environment.txt
Run migrations:

bash
python manage.py migrate
Start the development server:

bash
python manage.py runserver
Access the Admin Panel (optional):

Create a superuser:
bash
python manage.py createsuperuser
Log in at http://127.0.0.1:8000/admin.
Dependencies

The project uses the following dependencies, as specified in environment.txt:
asgiref==3.8.1
Django==5.1.3
djangorestframework==3.15.2
drf-yasg==1.21.8 (for API documentation)
psycopg2-binary==2.9.10 (for PostgreSQL support)
simplejwt==2.0.1 (for JWT authentication)
Additional libraries like pillow, pytz, sqlparse, and others for functionality and compatibility.
Usage
Access the API at http://127.0.0.1:8000/.
Use tools like Postman or curl to interact with the endpoints.
Contributing
Feel free to fork the project, submit issues, and make pull requests. Contributions are welcome!

License
This project is licensed under the MIT License.
