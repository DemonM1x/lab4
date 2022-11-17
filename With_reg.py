import re


def format_lines(line):
    global f
    if line.endswith(':\n'):
        return re.findall(ms_tree, line)
    elif line.endswith('[\n'):
        f = 1
        return re.findall(ms_undertree, line)
    else:
        return re.findall(ms_data, line)

title_list = []
close_title_list = []
curly_braces = 0
f = 0
ms_tree = re.compile(r'"(\w*)":\n')
ms_undertree = re.compile(r'"(\w*)": \[\n')
ms_data = re.compile(r'"(\w*)": "([\W\w]*)"')

def start(input_file, output_file):
    global title_list, curly_braces, close_title_list, f
    with open(input_file, 'r', encoding="utf-8") as f1:
        with open(output_file, 'w', encoding="utf-8") as f2:
            f2.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>"+'\n')
            f1.readline()
            for i in range(27-2):
                line = f1.readline()
                for j in range(len(line)):
                    if line[0] == "\t":
                        line = line.replace("\t", "", 1)
                    else:
                        break
                if len(line.split()[0]) <= 2:
                    if line.split()[0] == '{':
                        if f >= 1:
                            if f > 1:
                                f2.write(' '*curly_braces*2 + title_list[-1] + '\n')
                            f += 1
                        curly_braces += 1

                    elif line.split()[0] == "},":
                        curly_braces -= 1
                        f2.write(' '*curly_braces*2 + close_title_list[-1]+'\n')


                    elif line.split()[0] == "}]" or line.split()[0] == "}":
                        curly_braces -= 1
                        f = 0
                        f2.write(' '*curly_braces*2 + close_title_list[-1] + '\n')
                        close_title_list.pop(-1)

                else:
                    words = format_lines(line)
                    if len(words[0]) > 2:
                        title_list.append("<" + str(words[0]) + ">")
                        close_title_list.append("</" + str(words[0]) + ">")
                        f2.write(' '*curly_braces*2 + title_list[-1] + '\n')
                    else:
                        title_list.append("<" + words[0][0] + ">")
                        close_title_list.append("</" + words[0][0] + ">")
                        data = words[0][1]
                        data = data.replace("\"", "&quot;")
                        data = data.replace("<", "&lt;")
                        data = data.replace(">", "&gt;")
                        data = data.replace("\\t", "\t")
                        f2.write(' '*curly_braces*2 + title_list[-1] + data + close_title_list[-1] + '\n')
                        title_list.pop(-1)
                        close_title_list.pop(-1)
    set_default()


def set_default():
    global title_list, close_title_list, curly_braces, f
    title_list, close_title_list, curly_braces, f = [], [], 0, 0

start('Tuesdayj.json','Tuesdayx3.xml')