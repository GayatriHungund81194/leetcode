def find_rotation_point(words):
    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1
    while floor_index < ceiling_index:
        guess_index = floor_index + ((ceiling_index - floor_index) // 2)
        if words[guess_index] >= first_word:
            floor_index = guess_index
        else:
            ceiling_index = guess_index
        if floor_index + 1 == ceiling_index:
            return ceiling_index
find_rotation_point(['k','v','a','b','c','d','e','g','i'])