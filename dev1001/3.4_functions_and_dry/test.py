import csv


def display_order():
    with open("order.csv", "r") as f:
        reader = csv.reader(f)
        reader.__next__()        
        for row in reader:
            print(f"{row[-1]}x {row[0]} @ ${row[1]} = {float(row[-1]) * float(row[1])}")
        


def add_item():
    with open("order.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(["Chips", 6.5, 1])


if __name__ == '__main__':
    add_item()
    display_order()
