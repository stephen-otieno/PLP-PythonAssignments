class Smartphone:
    def __init__(self, brand, model, screen_size, storage):
        self.brand = brand
        self.model = model
        self.screen_size = screen_size
        self.__storage = storage  # encapsulated attribute

    def get_specs(self):
        return f"{self.brand} {self.model} with {self.screen_size} inch screen "

    def get_storage(self):  # encapsulated access
        return self.__storage


class Smartwatch(Smartphone):  # inheriting attributes of smartphone class
    def __init__(self, brand, model,  storage):
        super().__init__(brand, model, screen_size=1.5, storage=storage)

    def get_specs(self):
        return f"{self.brand} {self.model} Smartwatch with {self.screen_size} inch display"


phone = Smartphone("Samsung", "Galaxy A03 Core", 16, 64)
watch = Smartwatch("Apple", "Series 5", 32)


print("*****Smartphone*****")
print(f"Phone specifications: {phone.get_specs()}")
print(f"Phone Storage: {phone.get_storage()} GB")

print("*****Smartwatch*****")
print(f"Watch specifications: {watch.get_specs()}")
