import csv
import os
from datetime import datetime, timedelta

def read_dictionary(filename, key_column_index):
    """Reads a CSV file and returns a dictionary using key_column_index."""
    dictionary = {}
    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header
        for row in reader:
            if len(row) == 0:
                continue
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

def main():
    try:
        # Get the current folder path of this script
        current_folder = os.path.dirname(__file__)
        products_path = os.path.join(current_folder, "products.csv")
        request_path = os.path.join(current_folder, "request.csv")

        # Read products into a dictionary
        products_dict = read_dictionary(products_path, 0)

        # Print store name
        print("Inkom Emporium\n")

        total_items = 0
        subtotal = 0

        # Read request file and process
        with open(request_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header
            for row in reader:
                if len(row) != 2:
                    continue

                prod_num = row[0]
                quantity = int(row[1])

                # KeyError will be raised here if product ID not in dict
                prod_info = products_dict[prod_num]
                name = prod_info[1]
                price = float(prod_info[2])

                print(f"{name}: {quantity} @ {price:.2f}")

                total_items += quantity
                subtotal += price * quantity

        # Calculate tax and total
        tax = subtotal * 0.06
        total = subtotal + tax

        # Print receipt totals
        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {tax:.2f}")
        print(f"Total: {total:.2f}")
        print("\nThank you for shopping at the Inkom Emporium.")

        # Print current date and time
        current_time = datetime.now()
        print(f"{current_time:%a %b %d %I:%M:%S %Y}")

        # Bonus: return-by date and days until New Year
        return_by = current_time + timedelta(days=30)
        print(f"Return by: {return_by:%A %B %d at 9:00 PM}")
        
        new_year = datetime(current_time.year + 1, 1, 1)
        days_until_new_year = (new_year - current_time).days
        print(f"{days_until_new_year} days until the New Year's Sale!")

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
    except PermissionError as e:
        print("Error: permission denied")
        print(e)
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)

if __name__ == "__main__":
    main()
