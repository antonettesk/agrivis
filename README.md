# Agrivis

## Overview

Agrivis is a Django-based web application designed to analyze and visualize agricultural market trends. It provides users with insights into crop and livestock product prices, production quantities, trade indices, and food balance sheets across various countries and years.

## Features

- Interactive dashboard for visualizing agricultural market data.
- Data filtering by country, product, and year range.
- User preferences for customizable data visualization and notifications.
- API integration for real-time data fetching from the FAOSTAT database.

## Installation

### Prerequisites

- Python 3.6+
- Django 3.2+
- Other dependencies listed in 'requirements.txt'

### Setup

1. Clone the repository:
```bash
    git clone https://github.com/antonettesk/agrivis.git
    cd agrivis
```

2. Install required packages:
```bash
    pip install -r requirements.txt
```

3. Apply migrations:
```bash
    python manage.py migrate
```

4. Run the development server:
```bash
    python manage.py runserver
```

5. Visit 'http://127.0.0.1:8000/' in your browser to access the application.

## Usage

After launching the application, navigate through the interactive dashboard to explore agricultural market data. Use the filters to customize the data visualization according to your interests.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create your feature branch e.g. '(git checkout -b feature/AmazingFeature).'
3. Commit your changes e.g. '(git commit -m 'Add some AmazingFeature').'
4. Push to the branch e.g. '(git push origin feature/AmazingFeature).'
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements

- FAOSTAT for providing the agricultural market data.
- Django community for the comprehensive documentation and support.
