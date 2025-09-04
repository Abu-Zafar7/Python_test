#  Soccer Players API

A comprehensive Django REST API for managing soccer players, tracking likes, and providing various ranking systems. Built with Django, Django REST Framework, and PostgreSQL.

##  Features

### Core Features
- **Player Management**: CRUD operations for soccer players with name, club, position, and likes
- **Like System**: Users can like players with duplicate prevention
- **Advanced Filtering**: Filter players by club and/or position
- **Comprehensive Rankings**: Multiple ranking systems for different perspectives

### Ranking Systems
1. **Overall Ranking**: All players ordered by total likes (highest first)
2. **Position-based Ranking**: Players grouped by position, sorted by likes within each group
3. **Club-based Ranking**: Players grouped by club, sorted by likes within each group
4. **Top N Players**: Configurable top N most liked players
5. **Most Liked Per Club**: Find the most popular player(s) in each club

### Bonus Features (All Implemented!)
-  **Duplicate Like Prevention**: Users cannot like the same player twice
-  **Authentication System**: Token-based authentication for secure operations
-  **Top N Players**: Configurable parameter for returning top N players
-  **Most Liked Per Club**: Endpoint to find most popular players in each club
-  **Comprehensive Unit Tests**: Full test coverage for ranking and like logic
-  **Pagination**: Built-in pagination for player lists

##  Architecture & Design Choices

### Technology Stack
- **Backend**: Django 5.2.5 + Django REST Framework
- **Database**: PostgreSQL with optimized schemas
- **Authentication**: Token-based authentication
- **API Design**: RESTful principles with intuitive endpoint naming

### Database Schema
- **Player Model**: Core player information with position choices
- **Like Model**: Many-to-many relationship with user tracking and duplicate prevention
- **User Model**: Django's built-in User model for authentication

### Design Principles
- **RESTful Design**: Intuitive endpoint structure and HTTP methods
- **Separation of Concerns**: Clear separation between models, views, and serializers
- **DRY Principle**: Reusable components and minimal code duplication
- **Security First**: Authentication required for like operations

##  Requirements

- Python 3.8+
- Django 5.2.5
- Django REST Framework
- PostgreSQL
- Virtual environment (recommended)

## Installation & Setup

### 1. Set Up Virtual Environment
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### 2. Clone the Repository
```bash
git clone <repository-url>
cd Python_test
```

### 3. Install Dependencies
```bash
pip install django
pip install djangorestframework
pip install psycopg2-binary
```

### 4. Database Setup
Create a PostgreSQL database named `soccerdb` and update the database credentials in `soccer_api/settings.py` if needed:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "soccerdb",
        "USER": "postgres",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Load Sample Data
```bash
python manage.py load_players
```

### 7. Create Superuser
```bash
python manage.py createsuperuser
```

### 8. Run the Development Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/token/` - Obtain authentication token

### Players
- `GET /api/players/` - List all players (with optional filtering)
  - Query parameters: `?club=<club_name> or ?position=<position>`
- `POST /api/players/<id>/like/` - Like a player (requires authentication)

### Rankings
- `GET /api/rankings/overall/` - Overall player ranking by likes
- `GET /api/rankings/position/` - Position-based rankings
  - Query parameters: `?position=<position>` (optional)
- `GET /api/rankings/club/` - Club-based rankings
  - Query parameters: `?club=<club_name>` (optional)
- `GET /api/rankings/top/` - Top N players
  - Query parameters: `?top=<number>` (optional)
- `GET /api/rankings/club/top/` - Most liked players per club
  - Query parameters: `?club=<club_name>` (optional)



## Authentication

The API uses token-based authentication:
1. Register a user at `/api/auth/register/`
2. Obtain a token at `/api/auth/token/`
3. Include the token in the Authorization header: `Authorization: Token <your_token>`

## Testing

Run the comprehensive test suite:
```bash
python manage.py test
```

The test suite covers:
- Player like functionality
- Duplicate like prevention
- Ranking systems
- Club and position filtering
- Top N players functionality
- Most liked per club logic

## Project Structure

```
Python_test/
├── soccer_api/           # Main Django project
│   ├── settings.py      # Project configuration
│   ├── urls.py          # Main URL routing
│   └── wsgi.py          # WSGI configuration
├── players/              # Players app
│   ├── models.py        # Database models
│   ├── views.py         # API views and logic
│   ├── serializers.py   # Data serialization
│   ├── urls.py          # App URL routing
│   ├── admin.py         # Django admin configuration
│   ├── tests.py         # Comprehensive test suite
│   └── management/      # Custom management commands
│       └── commands/
│           └── load_players.py  # Data loading command
├── players.json          # Sample player data
├── manage.py             # Django management script
└── README.md             # This file
```

##  Usage Examples

### Get All Players
```bash
curl http://localhost:8000/api/players/
```

### Filter Players by Club
```bash
curl "http://localhost:8000/api/players/?club=PSG"
```

### Like a Player (with authentication)
```bash
curl -X POST http://localhost:8000/api/players/1/like/ \
  -H "Authorization: Token your_token_here"
```

### Get Top 5 Players
```bash
curl "http://localhost:8000/api/rankings/top/?top=5"
```

### Get Position Rankings
```bash
curl http://localhost:8000/api/rankings/position/
```


### Pagination
Default pagination is set to 10 items per page. This can be modified in `settings.py`:

```python
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10, 
}
```

### Database
The project is configured for PostgreSQL but can easily be adapted for other databases by modifying the `DATABASES` setting.



##  Acknowledgments

- Built with Django and Django REST Framework
- PostgreSQL for robust data storage
- Comprehensive testing with Django's testing framework
- RESTful API design principles

## Bonus Tip: Use Postman to check the endpoints.
---
