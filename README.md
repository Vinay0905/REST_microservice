# ZEKA REST Microservice

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/Vinay0905/REST_microservice)
[![Language](https://img.shields.io/badge/Language-Python-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)](CONTRIBUTING.md)

> A production-ready REST microservice for managing customers and orders with MongoDB integration, built with Python and FastAPI principles. Features comprehensive API endpoints, Docker containerization, and CI/CD workflows.

## 🎯 Overview

ZEKA REST Microservice is a scalable backend solution designed to handle customer and order management operations. It demonstrates best practices in microservice architecture, including:

- **RESTful API Design**: Standard HTTP methods for CRUD operations
- **Database Integration**: MongoDB with connection pooling
- **Containerization**: Docker and Docker Compose support
- **Testing**: Comprehensive test suite with pytest
- **CI/CD Pipeline**: GitHub Actions workflow for automated testing
- **Environment Management**: Environment variable configuration

## ⚙️ Tech Stack

| Component | Technology | Version |
|-----------|-----------|----------|
| **Runtime** | Python | 3.8+ |
| **Database** | MongoDB | 4.0+ |
| **Web Framework** | Flask/FastAPI-like | - |
| **Containerization** | Docker | Latest |
| **Testing** | Pytest | Latest |
| **CI/CD** | GitHub Actions | - |

## 📋 Features

✅ **Customer Management**
- Create new customers (name, email)
- Retrieve all customers
- Customer validation and error handling

✅ **Order Management**
- Create orders for customers
- Track items and amounts
- Link orders to customers
- Order history tracking

✅ **Infrastructure**
- Docker containerization for easy deployment
- Docker Compose for local development
- Environment configuration via .env files
- Automated CI/CD workflows

✅ **Testing & Quality**
- Unit tests with pytest
- Test isolation and fixtures
- Continuous Integration pipeline

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- MongoDB (local or Atlas)
- pip (Python package manager)
- Docker (optional, for containerization)

### Local Development Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/Vinay0905/REST_microservice.git
cd REST_microservice
```

#### 2. Create Environment Configuration

Create a `.env` file in the project root:

```env
MONGODB_URI="mongodb+srv://<user>:<pass>@zeka.7ijqrc1.mongodb.net/?retryWrites=true&w=majority"
MONGODB_DB="ZEKA"
PYTHON_ENV="development"
PORT=8000
```

#### 3. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 4. Run the Application

```bash
python run.py
```

The server will start at `http://localhost:8000`

### Docker Setup

#### Using Docker Compose (Recommended)

```bash
# Build and start services
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop services
docker-compose down
```

#### Using Docker Directly

```bash
# Build image
docker build -t zeka-rest-api .

# Run container
docker run -p 8000:8000 --env-file .env zeka-rest-api
```

## 📚 API Documentation

### Base URL
```
http://localhost:8000/api
```

### Endpoints

#### Customers

**Create Customer**
```http
POST /api/customers
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Response (201 Created)**
```json
{
  "_id": "507f1f77bcf86cd799439011",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}
```

**Get All Customers**
```http
GET /api/customers
```

**Response (200 OK)**
```json
[
  {
    "_id": "507f1f77bcf86cd799439011",
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2024-01-15T10:30:00Z"
  }
]
```

#### Orders

**Create Order**
```http
POST /api/orders
Content-Type: application/json

{
  "customer_id": "507f1f77bcf86cd799439011",
  "item": "Laptop",
  "amount": 999.99
}
```

**Response (201 Created)**
```json
{
  "_id": "507f1f77bcf86cd799439012",
  "customer_id": "507f1f77bcf86cd799439011",
  "item": "Laptop",
  "amount": 999.99,
  "created_at": "2024-01-15T11:00:00Z"
}
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_customers.py

# Run with coverage report
pytest --cov=app
```

Test files are located in the `tests/` directory.

## 📁 Project Structure

```
REST_microservice/
├── app/                          # Application code
│   ├── __init__.py
│   ├── models.py                # Data models
│   ├── routes.py                # API endpoints
│   └── database.py              # Database configuration
├── tests/                       # Test suite
│   ├── test_customers.py
│   ├── test_orders.py
│   └── conftest.py             # Pytest fixtures
├── .github/
│   └── workflows/               # CI/CD workflows
│       └── tests.yml           # Automated testing pipeline
├── .env.example                 # Environment template
├── .dockerignore                # Docker ignore rules
├── .gitignore                   # Git ignore rules
├── Dockerfile                   # Docker image definition
├── docker-compose.yml           # Docker Compose configuration
├── requirements.txt             # Python dependencies
├── pytest.ini                   # Pytest configuration
├── run.py                       # Application entry point
└── README.md                    # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `MONGODB_URI` | MongoDB connection string | Yes |
| `MONGODB_DB` | Database name | Yes |
| `PYTHON_ENV` | Environment (development/production) | No |
| `PORT` | Server port | No (default: 8000) |
| `LOG_LEVEL` | Logging level | No (default: INFO) |

### MongoDB Atlas Setup

1. Create a MongoDB Atlas account at [mongodb.com/atlas](https://www.mongodb.com/cloud/atlas)
2. Create a cluster
3. Get connection string: `mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority`
4. Add to `.env` file

## 🔄 CI/CD Pipeline

The project includes GitHub Actions workflows for:

- **Automated Testing**: Runs on every push and pull request
- **Code Quality**: Checks for code standards
- **Docker Build**: Builds and pushes Docker images (on release)

Workflow file: `.github/workflows/tests.yml`

## 📦 Dependencies

Key dependencies in `requirements.txt`:

```
Flask/FastAPI-like framework
PyMongo - MongoDB driver
pytest - Testing framework
python-dotenv - Environment configuration
requests - HTTP client
```

View full list: `pip freeze`

## 🐛 Troubleshooting

### MongoDB Connection Error

**Problem**: `MongoAuthenticationError`

**Solution**:
- Verify MongoDB URI in `.env` file
- Check MongoDB credentials
- Ensure IP is whitelisted in MongoDB Atlas
- Verify network connectivity

### Port Already in Use

**Problem**: `Address already in use on port 8000`

**Solution**:
```bash
# Kill process using port 8000
# On macOS/Linux:
lsof -ti:8000 | xargs kill -9

# On Windows (PowerShell):
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Virtual Environment Issues

**Problem**: `No module named 'app'`

**Solution**:
```bash
# Ensure venv is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall requirements
pip install -r requirements.txt
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit a pull request

### Contribution Guidelines

- Follow PEP 8 Python style guide
- Write tests for new features
- Update documentation
- Keep commits clear and descriptive

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Vinay0905**
- GitHub: [@Vinay0905](https://github.com/Vinay0905)
- Focus: Backend Development, Microservices, Python

## 🙏 Acknowledgments

- MongoDB documentation and community
- Python community best practices
- GitHub Actions for CI/CD
- Contributors and testers

## 📞 Support

For issues or questions:

1. Check existing [GitHub Issues](https://github.com/Vinay0905/REST_microservice/issues)
2. Create a new issue with detailed information
3. Include steps to reproduce for bugs
4. Provide environment details

## 📈 Roadmap

### Version 1.1
- [ ] Add authentication (JWT)
- [ ] Implement pagination
- [ ] Add logging
- [ ] Request validation schemas

### Version 1.2
- [ ] GraphQL endpoint
- [ ] Redis caching
- [ ] Advanced filtering
- [ ] API rate limiting

### Version 2.0
- [ ] Kubernetes deployment
- [ ] Message queue integration
- [ ] Analytics dashboard
- [ ] Payment processing

---

**Happy coding! 🚀**
