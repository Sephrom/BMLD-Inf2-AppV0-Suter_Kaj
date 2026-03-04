# Simple Calculator Application

This project is a simple calculator application that includes a Body Mass Index (BMI) calculator and a dilution calculator. It is built using Python and Flask, providing a web interface for users to perform calculations.

## Project Structure

```
calculator-app
├── src
│   ├── app.py                # Entry point of the application
│   ├── calculators           # Directory for calculator modules
│   │   ├── __init__.py       # Marks the calculators directory as a package
│   │   ├── bmi.py            # BMI calculation functions
│   │   └── dilution.py       # Dilution calculation functions
│   ├── templates             # HTML templates for the application
│   │   ├── home.html         # Home page template
│   │   └── calculator.html    # Calculator page template
│   └── static                # Static files (CSS)
│       └── style.css         # Styles for the application
├── tests                     # Directory for unit tests
│   └── test_calculators.py   # Tests for calculator functions
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd calculator-app
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Start the Flask application by running:
   ```
   python src/app.py
   ```
   The application will be available at `http://127.0.0.1:5000`.

## Usage

- Navigate to the home page to choose between the BMI calculator and the dilution calculator.
- Enter the required values in the input fields and submit the form to see the results.

## Contributors

- [Your Name](mailto:your.email@example.com)
- [Contributor Name](mailto:contributor.email@example.com)

## License

This project is licensed under the MIT License - see the LICENSE file for details.