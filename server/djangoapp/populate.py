from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Nissan Motor Company is a multinational automobile manufacturer"},
        {"name": "Mercedes", "description": "Mercedes-Benz is a German luxury automobile manufacturer"},
        {"name": "Audi", "description": "Audi is a German automobile manufacturer"},
        {"name": "Kia", "description": "Kia Corporation is a South Korean automobile manufacturer"},
        {"name": "Toyota", "description": "Toyota Motor Corporation is a multinational automotive manufacturer"},
        {"name": "Ford", "description": "Ford Motor Company is an American multinational automobile manufacturer"},
        {"name": "BMW", "description": "Bayerische Motoren Werke AG is a German multinational manufacturer"},
    ]

    car_make_instances = []
    for data in car_make_data:
        obj = CarMake.objects.get_or_create(
            name=data['name'], defaults={'description': data['description']})[0]
        car_make_instances.append(obj)

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Sorento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Cerato", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Corolla", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Mustang", "type": "COUPE", "year": 2023, "car_make": car_make_instances[5]},
        {"name": "F-150", "type": "TRUCK", "year": 2023, "car_make": car_make_instances[5]},
        {"name": "Explorer", "type": "SUV", "year": 2023, "car_make": car_make_instances[5]},
        {"name": "3 Series", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[6]},
        {"name": "5 Series", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[6]},
        {"name": "X5", "type": "SUV", "year": 2023, "car_make": car_make_instances[6]},
    ]

    for data in car_model_data:
        CarModel.objects.get_or_create(
            name=data['name'],
            car_make=data['car_make'],
            defaults={'type': data['type'], 'year': data['year']}
        )
