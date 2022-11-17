def format_lines(line):
    global f, curly_braces, count, title_list
    if line.endswith(':'):
        curly_braces += 1
        line = line.replace("\"","")
        line = line.replace(":","")
        return ' '*(curly_braces-1)*2 + 'message ' + line + "{\n"
    elif line.endswith('['):
        f = 1
        line = line.replace("\"","")
        line = line.replace(": [","")
        title_list.append(line)
        curly_braces += 1
        return ' '*(curly_braces-1)*2 + 'message ' + line + '{\n'
    else:
        count += 1
        if f == 1:
            a = line.split("\": ")
            return ' '*curly_braces*2 + 'string ' + a[0][1:len(a[0])] + ' = ' + str(count) + ';\n'
        elif f == 0:
            f = 2
            return ' '*curly_braces*2 + 'repeated ' + title_list[-1] + ' ' + title_list[-1][0].upper() + title_list[-1][1:len(title_list[-1])] + ' = ' + str(count) + ';\n'

title_list = []
close_title_list = []
curly_braces = 1
f = 0
count = 0

def start(input_file, output_file):
    global title_list, curly_braces, close_title_list, f, count
    with open(input_file, 'r', encoding="utf-8") as f1:
        with open(output_file, 'w', encoding="utf-8") as f2:
            f2.write("syntax = \"proto3\";\n")
            f1.readline()
            for i in range(27-2):
                line = f1.readline()
                line = line.replace("\n", "")
                for j in range(len(line)):
                    if line[0] == "\t":
                        line = line.replace("\t", "", 1)
                    else:
                        break
                if len(line.split()[0]) <= 2:
                    if line.split()[0] == '{':
                       continue

                    elif line.split()[0] == "},":
                        if f == 1:
                            f = 0



                    elif line.split()[0] == "}]":

                        f = 0
                        title_list.pop(-1)
                        f2.write(' '*curly_braces*2 + '};' + '\n')

                    elif line.split()[0] == "}":
                        curly_braces -= 1
                        f2.write(' '*curly_braces*2 + '};' + '\n')
                else:
                    words = format_lines(line)
                    if words != None:
                        f2.write(words)

    set_default()


def set_default():
    global title_list, close_title_list, curly_braces, f, count
    title_list, close_title_list, curly_braces, f, count = [], [], 0, 0, 0

start('Tuesdayj.json','Tuesdayp.proto')