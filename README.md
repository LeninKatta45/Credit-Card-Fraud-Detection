# Credit-Card-Fraud-Detection
[![Python application test with Github Actions](https://github.com/LeninKatta45/Credit-Card-Fraud-Detection/actions/workflows/main.yml/badge.svg)](https://github.com/LeninKatta45/Credit-Card-Fraud-Detection/actions/workflows/main.yml)

## Overview

The **Credit Card Fraud Detection System** is designed to detect fraudulent transactions in real-time using machine learning. The system leverages the **Random Forest** algorithm for high accuracy and uses **SMOTE** to balance the dataset. The project features a web interface built using **Flask** and **FastAPI**, and is deployed on **AWS** to ensure scalability. Continuous integration and deployment are managed through **GitHub Actions**.

## Key Features

- **Random Forest Model:** A robust classifier for fraud detection.
- **SMOTE for Data Balancing:** Addresses class imbalance to improve prediction reliability.
- **Web Interface:** User-friendly web interface for fraud prediction.
- **AWS Cloud Deployment:** Scalable infrastructure on AWS.
- **CI/CD Pipeline:** Integrated with GitHub Actions for continuous testing and deployment.

## Performance Metrics

- **Accuracy:** High accuracy in detecting fraudulent transactions.
- **Balanced Dataset:** SMOTE implementation to handle imbalanced fraud data.

## Technologies Used

- **Programming Language:** Python
- **Machine Learning Libraries:** Scikit-learn (Random Forest), Pandas, NumPy
- **Web Frameworks:** Flask, FastAPI
- **Cloud Platform:** AWS
- **CI/CD Tools:** GitHub Actions for automation and deployment

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/LeninKatta45/Credit-Card-Fraud-Detection.git
    cd credit-card-fraud-detection
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the web application:

    ```bash
    python app.py
    ```

2. Access the web interface at `http://localhost:5000` to input transaction data and receive predictions on fraud likelihood.

## Web Interface

The web interface allows users to input transaction details and receive real-time predictions about whether the transaction is fraudulent or not. The backend logic is powered by Flask, and FastAPI is used for creating robust REST APIs.

## Deployment

The project is deployed on AWS for scalability. The setup includes:
- AWS EC2 instance for hosting the application.
- GitHub Actions for CI/CD pipeline to ensure that every update is tested and deployed seamlessly.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any queries or feedback, feel free to reach out:

- **Lenin Balaji Katta**
- [Email](mailto:leninbalaji45@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/leninkatta)
- [GitHub](https://github.com/LeninKatta45)
