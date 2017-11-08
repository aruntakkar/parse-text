import collections

with open("customerdata.txt", 'r',
          encoding='utf-8') as customers_file:
    data_list = customers_file.readlines()

# deleting the first entry of titles
data_list.pop(0)


def total_orders():
    return len(data_list)


def total_orders_amount():
    total_amount = 0
    for each in data_list:
        total_amount += int(each[-4:])
    return total_amount


def get_customers(orders):
    customers_names_list = []
    for each in data_list:
        customers_names_list.append(each[24:-5].replace(",", ""))
        orders_collection = collections.Counter(customers_names_list)

    customers_list = []

    for user, order_status in orders_collection.items():
        # For upto 4 orders
        if order_status == orders:
            customers_list.append(user)
        # For 5+ plus orders
        elif order_status >= orders:
            customers_list.append(user)
    return customers_list


with open('reports.txt', 'w') as output_file:
    output_file.write(
        "Total Numbers of Orders \n" '{} \n'.format(total_orders()))
    output_file.write(
        "\nTotal orders Amount \n" '{} \n'.format(total_orders_amount()))
    output_file.write("\nList of customers who order only once \n")
    output_file.write(', '.join(get_customers(1)) + '\n')
    output_file.write("\nOrders | Count of Customers \n")
    output_file.write("------|---------- \n")
    output_file.write("1|" '{} \n'.format(len(get_customers(1))))
    output_file.write("2|" '{} \n'.format(len(get_customers(2))))
    output_file.write("3|" '{} \n'.format(len(get_customers(3))))
    output_file.write("4|" '{} \n'.format(len(get_customers(4))))
    output_file.write("5+|" '{} \n'.format(len(get_customers(5))))
