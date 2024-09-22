# Customer-Segmentation-Project
This project is focused on **customer segmentation analysis** using the **K-Means Clustering** algorithm. The dataset used is the **Online Retail dataset**, which contains transactions from a UK-based online retailer over a period of one year. The goal of the project is to segment customers based on their purchasing behavior to help businesses understand their customer base better and target them effectively.

## Project Overview

In this project, I used the following steps:
- **Data Loading**: Loaded the dataset from an Excel file (`Online Retail.xlsx`).
- **Data Cleaning**: Removed missing values and cleaned the dataset.
- **Feature Engineering**: Created new features such as `TotalSpend`, `Frequency`, and `TotalQuantity` per customer.
- **Data Scaling**: Applied scaling using `StandardScaler` to prepare the data for clustering.
- **Clustering**: Applied K-Means clustering to segment the customers.
- **Visualization**: Used `seaborn` and `matplotlib` to visualize customer segments.

## Dataset

- **Dataset Name**: Online Retail
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Online+Retail) or Kaggle
- **Description**: Contains transaction data of an online retail store, including invoice number, stock code, quantity, invoice date, price, customer ID, and country.

## Project Files

- `customer_segmentation.py`: This is the main Python script that contains the code for the entire analysis, from data cleaning to clustering and visualization.
- `Online Retail.xlsx`: The dataset used for the project.

## Key Concepts and Techniques

- **Pandas**: For data manipulation and preprocessing.
- **Scikit-Learn**: Used for clustering and scaling the data.
- **Matplotlib and Seaborn**: For data visualization.
- **K-Means Clustering**: To group customers into different segments based on their purchasing behavior.

## Steps to Run the Project

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/customer-segmentation-project.git

2.Install the necessary Python libraries:
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl

3.Run the customer_segmentation.py script:
python customer_segmentation.py

Results
The analysis resulted in dividing the customers into 3 main segments:

1.High-value customers: These customers have a high total spend but may not shop frequently.
2.Frequent buyers: These customers shop frequently, but their individual spending might be lower.
3.Low-value customers: These customers shop infrequently and spend less overall.

Technologies Used
Programming Language: Python
Libraries: Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, Openpyxl

Conclusion
This project demonstrates how customer segmentation can help businesses understand their customer base better. By segmenting customers into different groups, businesses can tailor their marketing strategies, improve customer retention, and maximize profits.

Contact Information
If you have any questions or suggestions regarding this project, feel free to reach out:
LinkedIn: www.linkedin.com/in/jeevan--reddy
Email: jeevanreddy.work@gmail.com

