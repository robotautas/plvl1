'''
1. Parašyti klasę House, kuri turi 1-ą savybę size.
Klasė turi turėti metodus roof, walls, ir floor.
Klasė turi būti parašyta taip, kad inicijavus objektą, 
instrukcija print(objektas) atspausdintų 
atitinkamo dydžio namą, pvz.:
namas = House(6)
print(namas)
  /\  
 /  \ 
/    \
|    |
|    |
|    |
======

t.y. 6 eilutės + grindys.

2. Parašyikite dar vieną klasę Diamond, kuri paveldėtų klasę House 
ir atitinkamai spausdintų nurodyto dydžio rombą. Pvz.:
print(Diamond(4))
 /\
/  \
\  /
 \/
'''

class House:
    def __init__(self, size):
        self.size = size 

    def roof(self):
        roof_string = ''
        for i in range(int(self.size/2)):
            center_position_l = int(self.size/2 - 1)
            center_position_r = int(self.size/2)
            slope_left = center_position_l - i 
            slope_right = center_position_r + i
            roof_level_list = self.size * [' ']
            roof_level_list[slope_left] = '/'
            roof_level_list[slope_right] = '\\'
            roof_string += ''.join(roof_level_list) + '\n'
        return roof_string

    def walls(self):
        walls_string = ''
        for i in range(int(self.size/2)):
            wall_list = self.size * [' ']
            wall_list[0] = '|'
            wall_list[-1] = '|'
            walls_string += ''.join(wall_list) + '\n'
        return walls_string
    
    def floor(self):
        return self.size * '='

    def __repr__(self):
        return self.roof() + self.walls() + self.floor()


class Diamond(House):
    def lower_part(self):
        upper_part = self.roof()[:-1]
        lower_part = []
        for i in upper_part.split('\n'):
            replaced_temp = i.replace('\\', 'x')
            replaced = replaced_temp.replace('/', '\\')
            replaced = replaced.replace('x', '/')
            lower_part.append(replaced)
        return '\n'.join(lower_part[::-1])

    def __repr__(self):
        return self.roof() + self.lower_part()
       
print(Diamond(4))