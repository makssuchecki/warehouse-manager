# Warehouse Inventory API

A Flask-based REST API for managing products and warehouse operations for a music store. Built with a strong emphasis on test coverage and business-rule correctness — the project includes a complete automated testing pyramid (unit, API, BDD, and performance tests).

## Overview

The application supports the core lifecycle of warehouse inventory management:

- **Product management** — create products, retrieve a single product or the full product list, delete products (restricted to users with the `admin` role)
- **Stock operations** — receive incoming stock and issue outgoing stock
- **Business-rule validation** — enforces domain constraints such as preventing stock from being issued beyond the available quantity
- **User management** — create users with role-based access control
- **Operation history** — every operation performed on a product is logged and retrievable, providing a full audit trail

## Tech Stack

- **Backend:** Python, Flask
- **Database:** MongoDB
- **Testing:** pytest, coverage.py, behave (BDD), Locust (load testing)

## Getting Started

### Prerequisites

- Python 3.x
- MongoDB instance (local or Docker)

### Running the application

```bash
py -m flask --app app/api.py --debug run
```

## Testing

The project maintains a complete, automated test suite covering four layers of quality assurance.

### Unit & API tests (pytest)

```bash
py -m pytest
```

Check test coverage (project enforces 100% coverage):

```bash
py -m coverage report --fail-under=100
```

### Behavior-driven tests (BDD)

```bash
py -m behave
```

### Performance / load tests (Locust)

Requires the Flask server to be running (see above).

```bash
py -m locust -f ./tests/performance/locustfile.py --headless --run-time 10s -u 20 -r 5
```

## Author

**Maksymilian Suchecki**
