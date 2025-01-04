#!/usr/bin/env python3
# Implementation of do_create method with parameter parsing in the command interpreter

def do_create(self, arg):
    args = arg.split()
    if not args:
        print("** class name missing **")
        return
    class_name = args[0]
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return

    params = args[1:]  # Remaining arguments are parameters
    kwargs = {}
    for param in params:
        if "=" not in param:
            continue
        key, value = param.split("=", 1)
        value = self.parse_value(value)
        if value is not None:
            kwargs[key] = value

    new_instance = self.classes[class_name](**kwargs)
    new_instance.save()
    print(new_instance.id)

def parse_value(self, value):
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1].replace('_', ' ').replace('\\"', '"')
        return value
    try:
        if '.' in value:
            return float(value)
        return int(value)
    except ValueError:
        return None

