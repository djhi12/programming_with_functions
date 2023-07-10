# import csv

# def read_dictionary(filename, key_column_index):
#     """Read the contents of a CSV file into a compound
#     dictionary and return the dictionary.

#     Parameters
#         filename: the name of the CSV file to read.
#         key_column_index: the index of the column
#             to use as the keys in the dictionary.
#     Return: a compound dictionary that contains
#         the contents of the CSV file.
#     """
#     compound_dict = {}
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             key = row[key_column_index]
#             compound_dict[key] = row
#     return compound_dict

# def main():
#     products_dict = read_dictionary('products.csv', 0)
#     print(products_dict)

#     with open('request.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header row
#         for row in reader:
#             product_number = row[0]
#             quantity = int(row[1])

#             if product_number in products_dict:
#                 product = products_dict[product_number]
#                 product_name = product[1]
#                 product_price = float(product[2])

#                 print(f"Product: {product_name}")
#                 print(f"Quantity: {quantity}")
#                 print(f"Price: ${product_price:.2f}")
#                 print()

# if __name__ == '__main__':
#     main()


import csv
import datetime


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dict = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            compound_dict[key] = row
    return compound_dict


def print_receipt():
    try:
        products_dict = read_dictionary('products.csv', 0)

        total_quantity = 0
        subtotal = 0.0
        order_items = []

        with open('request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                if product_number in products_dict:
                    product = products_dict[product_number]
                    product_name = product[1]
                    product_price = float(product[2])

                    total_quantity += quantity
                    item_total = product_price * quantity
                    subtotal += item_total

                    order_items.append(
                        f"{product_name} x {quantity}: ${item_total:.2f}")
                else:
                    raise KeyError(f"Invalid product number: {product_number}")

        # Print receipt details
        print("Store Name")
        print("------------------------")
        for item in order_items:
            print(item)
        print("------------------------")
        print(f"Total Items: {total_quantity}")
        print(f"Subtotal: ${subtotal:.2f}")
        sales_tax = subtotal * 0.06
        print(f"Sales Tax (6%): ${sales_tax:.2f}")
        total_due = subtotal + sales_tax
        print(f"Total Due: ${total_due:.2f}")
        print("------------------------")
        print("Thank you for shopping!")
        print(
            f"Date/Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except KeyError as e:
        print(f"Error: {str(e)}")


if __name__ == '__main__':
    print_receipt()
