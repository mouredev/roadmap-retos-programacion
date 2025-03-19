# -- exercise
def callback(a, b):
    print("Sum = {0}".format(a + b))


def main(a, b, f=None):
    print("Add any two digits.")
    if f is not None:
        f(a, b)


main(1, 2, callback)


# -- extra challenge
def confirm(order, f):
    print("Confirming order: {0}".format(order))
    f(order)


def ready(order):
    print("Order {0} is ready.".format(order))


def deliver(order):
    print("Delivering order {0}.".format(order))


def process_order(order, confirm, ready, deliver):
    confirm(order, ready)
    confirm(order, deliver)
    print("Order {0} processed.".format(order))


def main():
    order = "Pizza"
    process_order(order, confirm, ready, deliver)
    order = "Burger"
    process_order(order, confirm, ready, deliver)
    order = "Salad"
    process_order(order, confirm, ready, deliver)

    print("All orders processed.")


if __name__ == "__main__":
    main()
