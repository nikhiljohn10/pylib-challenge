#!/usr/bin/env python3

import file_db as fdb


def main():
    db = fdb.Database("data.db")
    db.write("name", "John")
    db.write("location", "Kochi")
    print(db.read("name"))
    print(db.read("location"))


if __name__ == "__main__":
    main()
