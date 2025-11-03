# Python Calculator CI/CD

A Python calculator with complete Jenkins CI/CD pipeline.

## Features
- Basic arithmetic operations
- Unit tests with 100% coverage
- Automated CI/CD pipeline
- Security scanning
- Email notifications

## Local Development
```bash
pip install -r requirements.txt
pytest tests/
```

## CI/CD Pipeline

The Jenkins pipeline automatically:
1. Checks out code from GitHub
2. Installs dependencies
3. Runs linting (flake8)
4. Runs security scan (bandit)
5. Executes tests with coverage
6. Creates build artifact
7. Sends email notification