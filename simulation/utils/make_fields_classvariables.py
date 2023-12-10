from dataclasses import fields as dataclass_fields

def make_fields_classvariables(class_):
    """Make the fields of a dataclass also classmethods, that take in an instance of the class 
    itself and returns the field value.
    """

    fields = dataclass_fields(class_)
    for field in fields:
        exec(f"""
@classmethod
def {field.name}(cls, satellite):
    return satellite.{field.name}
        """)
        exec(f"class_.{field.name} = {field.name}")
        exec(f"del {field.name}")
    return class_