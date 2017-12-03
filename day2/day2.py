import random, string
 
 
def rand_str(num, length=7):
    char_list = []
    chars = string.ascii_letters + string.digits
    while len(char_list) < num:
        s = [random.choice(chars) for i in range(length)]
        char_rand = "".join(list(s))
        if char_rand not in char_list:
            char_list.append(char_rand)
    return char_list


def write_str(chars):
    f = open("Activation_code.txt","w")
    for i in chars:
        f.write(i+'\n')

if __name__ == '__main__':
    chars = rand_str(200)
    write_str(chars)