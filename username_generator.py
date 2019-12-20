from itertools import product
import random

class UserNameGenerator(object):
    def __init__(self):
        self.first_name = "jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul","ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren","ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet","lydia", "charles", "pedro", "bradley"
        self.last_name = "barker", "style", "spirits", "murphy", "blacker", "bleacher", "rogers", "warren", "keller"

    def generate_usernames(self, first_name, last_name):
        full_names = ["{} {}".format(f, l) for f, l in product(first_name, last_name) if f != l]
        random.shuffle(full_names)
        return full_names

