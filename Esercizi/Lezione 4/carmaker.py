def make_car(manufacturer, model_name, **kwargs):
    car={manufacturer:model_name}
    for key, value in kwargs.items():
        car[key]=value
    return car