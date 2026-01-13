# Function to simulate fetching sales data from a database or file
def fetch_sales():
    print("fetching the sales data ... ")

# Function to filter out invalid or incorrect sales records
def filter_valid_sales():
    print("filtering valid sales data ...")

# Function to summarize the final sales data (like totals, averages, etc.)
def summarize_data():
    print("summarizing sales data ...")

# Main function that generates the complete report
def generate_report():
    # Step 1: Fetch the raw sales data
    fetch_sales()
    
    # Step 2: Filter valid sales from the fetched data
    filter_valid_sales()
    
    # Step 3: Summarize the filtered sales data
    summarize_data()

    # Final message after report generation is complete
    print("report is ready")

# Calling the main function to generate the report
generate_report()
