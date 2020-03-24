import re
import os
import json
import file_io


if __name__ == "__main__":
    j = 0

    #ps = []
    d = {}
    files = os.listdir('.')
    for file in files:
        if '.txt' in file and 'q' not in file:
            lines = file_io.read_all_lines(file)
            question = ''
            for i in range(len(lines)):
                line = lines[i]
                if (i-3) % 6 == 0:
                    j += 1
                    # print(line)
                    p = re.findall('<p>.*</p>', line)
                    if len(p) > 0:
                        p = p[0]
                        p = p.replace(r'\"', r'"')
                        # /u**** to chinese
                        p = p.encode('utf-8').decode('unicode_escape')
                        # ps.append(f'<p style="color:red">{j}</p>')  # index

                        # ps.append(p)
                        question = p
                elif '.answer=true' in line:
                    print(line)
                    p = re.findall('<p>.*</p>', line)[0]
                    p = p.replace(r'\"', r'"')
                    # /u**** to chinese
                    p = p.encode('utf-8').decode('unicode_escape')
                    # ps.append(p)
                    # ps.append('<hr />')
                    d[question] = p

    # print(ps)
    # file_io.write_all_lines('answer.html', ps)
    # print(d)
    file_io.write_all_text('answer.json', json.dumps(d))
