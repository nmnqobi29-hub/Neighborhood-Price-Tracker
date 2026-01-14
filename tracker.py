import pandas as pd
import schedule
import time
import logging
import os

# 1. Setup Logging to track when the script runs
logging.basicConfig(
    filename='neighborhood_tracker.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def analyze_prices():
    # Finds the exact folder where tracker.py is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "local_prices.csv")

    try:
        # Load the data using the semicolon separator seen in your file
        # We skip the first row because of the 'Header;Header' line
        df = pd.read_csv(csv_path, sep=';', skiprows=1)
        
        # Clean column names to remove hidden spaces
        df.columns = df.columns.str.strip()

        print("\n" + "="*30)
        print("   DAILY PRICE REPORT")
        print("="*30)
        print(df)

        # 2. Calculation Logic
        total_cost = df['price'].sum()
        avg_price = df['price'].mean()
        expensive_item = df.loc[df['price'].idxmax()]

        print(f"\nTotal Basket:    R {total_cost:.2f}")
        print(f"Average Price:   R {avg_price:.2f}")
        print(f"Highest Price:   {expensive_item['item']} (R {expensive_item['price']:.2f})")
        print("="*30)
        
        logging.info(f"Report generated successfully. Total: R{total_cost:.2f}")

    except Exception as e:
        logging.error(f"Error running analysis: {e}")
        print(f"Error: {e}. Check if local_prices.csv is in the same folder as this script.")

# 3. Scheduling
# Change "10:30" to your preferred time
schedule.every().day.at("17:10").do(analyze_prices)

if __name__ == "__main__":
    print("Tracker is now active and running on OneDrive.")
    print("Scheduled to run daily at 17:10 (Press Ctrl+C to stop)")
    
    # Run once immediately so you can see the results now
    analyze_prices()
    
    # Keep the script awake to wait for the scheduled time
    while True:
        schedule.run_pending()
        time.sleep(60)