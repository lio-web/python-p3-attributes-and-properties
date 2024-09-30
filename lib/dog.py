#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
    def __init__(self, name="unknown", breed="unknown"):
        self.name=name
        self.breed = breed
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return

        if not isinstance(breed, str) or breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return

        self.name = name
        self.breed = breed
