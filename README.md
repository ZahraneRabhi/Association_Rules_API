# Association Rules API

A FastAPI-based service that provides association rules mining capabilities for order data. This API analyzes purchase patterns to identify frequently co-occurring items.

## Overview

This project implements a REST API that leverages the Apriori algorithm to mine frequent itemsets and generate association rules from transaction data. It identifies valuable purchase patterns such as "customers who bought X also bought Y." The API functions as a dedicated microservice for a restaurant application, providing an insights portal that helps restaurant owners analyze performance metrics and discover their most popular menu item combinations.

## Features

- Extracts frequent itemsets from order data
- Generates association rules with metrics like lift
- Provides results through a simple REST API
- Uses the efficient mlxtend library implementation

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Setup

1. Clone the repository:
```
git clone https://github.com/ZahraneRabhi/AssociationRulesApi.git
cd AssociationRulesApi
```

2. Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install fastapi pandas mlxtend
```

## Usage

### Running the API

Start the API server:

```
fastapi dev main.py
```

The API will be available at http://127.0.0.1:8000

### API Endpoints

- `GET /`: Welcome message
- `GET /most_frequent_items`: Returns the top 5 most frequent item associations

### Example Response

```json
{
  "most": [
    {
      "antecedents": ["Beverage Item 1"],
      "consequents": ["Pizza Item 1"]
    },
    {
      "antecedents": ["Extra Item 4"],
      "consequents": ["Pizza Item 1"]
    }
  ]
}
```

## Project Structure

```
AssociationRulesApi/
├── data/
│   └── Orders.csv          # Sample order data
├── utils/
│   └── utils.py            # Association rules mining functions
├── main.py                 # FastAPI application
├── .gitignore
├── LICENSE
└── README.md
```

## Data Format

The API works with order data in CSV format. The required columns are:
- OrderId: Unique identifier for each order
- MenuItemName: Name of the menu item ordered

## Dependencies

- FastAPI: Modern, fast web framework for building APIs
- mlxtend: Machine learning library with implementations of Apriori algorithm
- pandas: Data manipulation library

## License

This project is licensed under the MIT License - see the LICENSE file for details.
