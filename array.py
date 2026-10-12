
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s"
)

# 1. Unpacking a list
cups = ["cup1", "cup2", "cup3"]

logging.info("Unpacking cups:")
logging.info("%s", " ".join(cups))


# 2. Copying a list
original = [1, 2, 3]
copy = [*original]

logging.info("Original: %s", original)
logging.info("Copy: %s", copy)
logging.info("Same list? %s", copy is original)


# 3. Combining lists
drinks = ["Latte", "Mocha"]
more_drinks = ["Espresso", "Africana"]

all_drinks = [*drinks, *more_drinks]

logging.info("All drinks: %s", all_drinks)


# 4. Adding elements to lists
new_drinks = ["Espresso", *drinks]
new_drinks2 = [*drinks, "Africana"]
new_drinks3 = ["Espresso", *drinks, "Africana"]

logging.info("New drinks 1: %s", new_drinks)
logging.info("New drinks 2: %s", new_drinks2)
logging.info("New drinks 3: %s", new_drinks3)


# 5. Copying a dictionary
original_user = {"name": "Antenyi", "age": 39}
copied_user = {**original_user}

logging.info("Copied user: %s", copied_user)
logging.info("Same dictionary? %s", copied_user is original_user)


# 6. Merging dictionaries
base_order = {
    "drink": "Latte",
    "size": "Large",
    "price": 4.50
}

customizations = {
    "extra_shot": True,
    "syrup": "Vanilla"
}

final_order = {**base_order, **customizations}

logging.info("Final order: %s", final_order)


# 7. Merging dictionaries with overlapping keys
order1 = {"drink": "Latte", "price": 4.50}
order2 = {"drink": "Espresso", "size": "Small"}

merged = {**order1, **order2}

logging.info("Merged order: %s", merged)


# 8. Adding and updating dictionary values
user = {"name": "Antenyi", "age": 39}

updated_user = {**user, "city": "Benue, Nigeria"}
updated_user2 = {**user, "age": 31}

logging.info("User with city: %s", updated_user)
logging.info("User with updated age: %s", updated_user2)
logging.info("Original user: %s", user)


# 9. Rest unpacking with lists
numbers = [1, 2, 3, 4, 5]

first, second, *rest = numbers

logging.info("First: %s", first)
logging.info("Second: %s", second)
logging.info("Rest: %s", rest)


# 10. Collecting remaining dictionary entries
person = {
    "name": "Antenyi",
    "age": 39,
    "city": "Benue, Nigeria",
    "is_active": True
}

name, *unused = [person["name"]]
other_details = {key: value for key, value in person.items() if key != "name"}

logging.info("Name: %s", name)
logging.info("Other details: %s", other_details)


# 11. Variable function arguments
def sum_numbers(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total


logging.info("Sum of 1, 2, 3: %s", sum_numbers(1, 2, 3))
logging.info(
    "Sum of 1, 2, 3, 4, 5: %s",
    sum_numbers(1, 2, 3, 4, 5)
)
