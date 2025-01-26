# Fit Zone

## Description
**Fit Zone** is a Python project that implements a connection pool for interacting with a MySQL database using the **DAO (Data Access Object)** pattern. The project ensures secure management of sensitive information such as database credentials through environment variables.

## Features
- **Connection Pooling**: Efficient management of database connections.
- **DAO Pattern**: A design pattern for structured and maintainable data access.
- **Environment Variable Management**: Secure handling of sensitive data, including database credentials.

## Installation

### Prerequisites
- Python 3.8 or higher
- MySql

### Steps to install:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/juanseDev31/fit-zone.git
2. Navigate to the project
   ```bash
   cd fit-zone
3. Create a virtual environmen Windows:
   ```bash
   python -m venv .venv
4. Activate the virtual environment
    ```bash
   .venv\Scripts\activate
5. Create a .env in your python project
   DATABASE_URL=your_database_url
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

## Alternative Setup

These steps outline the basic way to install and run the project. However, feel free to adapt the process according to your preferences or environment. If you prefer to use a different setup or package manager, it's perfectly valid as long as the required dependencies are installed and the environment is configured properly.

Happy coding! 😄
