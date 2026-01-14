Neighborhood Price Tracker (Python)
Project Overview
The Neighborhood Price Tracker is a Python-based automation tool designed to help consumers monitor the cost of essential groceries. By reading data from a local CSV file, the script performs statistical analysis on current prices and logs the results at a scheduled time every day.

Key Objectives
Automation: Eliminate manual price checks by scheduling daily reports at a specific time (e.g., 17:05).

Data Analysis: Automatically calculate the total basket cost, average item price, and identify the most expensive essential item.

Historical Tracking: Create a permanent record of price fluctuations using a local log file to observe inflation trends over time.

Technical Components
Python & Pandas: Used for efficient data manipulation and mathematical calculations.

Schedule Library: Powers the automation, allowing the script to run without human intervention.

CSV Data Store: A lightweight file (local_prices.csv) that serves as the database for item prices.

Logging System: A robust error-handling and recording system that saves report outcomes to neighborhood_tracker.log.

Real-World Impact
Budget Optimization: Users can see exactly when their "Total Basket" price increases, allowing them to adjust their household spending immediately.

Consumer Advocacy: By maintaining a time-stamped log, consumers have data-driven evidence of price increases at local retailers.

Inflation Awareness: The project makes abstract economic concepts like "Inflation" tangible by showing the direct impact on daily essentials like Milk and Bread.