class Sea:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['0'] * width for _ in range(height)]

    def display(self):
        for i in self.grid:
            print(i)

    def get_content_at(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        else:
            return None
    
    def set_content_at(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = str(value)
            return True
        else:
            return False

# Exemple d'utilisation
width = 5
height = 6

sea = Sea(width, height)
sea.display()

print(len(sea.grid))
print(len(sea.grid[0]))

# Interroger le contenu d'une case
x_coord = 2
y_coord = 3
content = sea.get_content_at(x_coord, y_coord)

if content is not None:
    print(f"Le contenu de la case ({x_coord}, {y_coord}) est : {content}")
else:
    print(f"La case ({x_coord}, {y_coord}) est en dehors des limites de la mer.")

# Modifier le contenu d'une case
x_coord = 0
y_coord = 1
new_value = 1

success = sea.set_content_at(x_coord, y_coord, new_value)

if success:
    print(f"Le contenu de la case ({x_coord}, {y_coord}) a été modifié avec succès.")
    sea.display()  # Afficher la mer après la modification
else:
    print(f"La case ({x_coord}, {y_coord}) est en dehors des limites de la mer.")

# Interroger le contenu d'une case
x_coord = 0
y_coord = 1
content = sea.get_content_at(x_coord, y_coord)

if content is not None:
    print(f"Le contenu de la case ({x_coord}, {y_coord}) est : {content}")
else:
    print(f"La case ({x_coord}, {y_coord}) est en dehors des limites de la mer.")