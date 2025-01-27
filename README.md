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

## Helpful Links

If you're new to Python development, here are some helpful resources that guide you through setting up the project:

1. **Setting up a virtual environment**:  
   [How to create a virtual environment in Python](https://realpython.com/python-virtual-environments-a-primer/)
   
2. **Creating and using `.env` files for environment variables**:  
   [Using environment variables in Python with python-dotenv](https://pypi.org/project/python-dotenv/)

3. **Cloning a GitHub repository**:  
   [How to clone a repository from GitHub](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

4. **Pushing changes to a GitHub repository**:  
   [How to push code to GitHub](https://docs.github.com/en/github/using-git/pushing-commits-to-a-remote-repository)

5. **General Git help**:  
   [Git Basics Documentation](https://git-scm.com/doc)

These links will guide you through the basics of setting up your project, working with Git, and handling environment variables securely. If you encounter any issues, feel free to refer to these resources for troubleshooting.


Happy coding! 😄
