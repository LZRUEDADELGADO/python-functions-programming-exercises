
def render_person(name, birthdate, eye_color, age, gender):
    return f"{name} is a {age} years old {gender} born in {birthdate} with {eye_color} eyes"

print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))
