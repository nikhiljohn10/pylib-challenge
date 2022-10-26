#!/usr/bin/env python3

from sample_lib.sample import Cart


def main():
    cart = Cart()
    cart.add_item("Apple", 23)
    cart.add_item("Orange", 15)
    cart.add_item("Grape", 19)
    print(cart)


if __name__ == "__main__":
    main()
