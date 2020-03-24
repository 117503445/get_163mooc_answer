import file_io
import json
import re
if __name__ == "__main__":

    js = file_io.read_all_text('answer.json')
    answer_d = json.loads(js)

    lines = file_io.read_all_lines('q.txt')
    questions = []
    for i in range(len(lines)):
        line = lines[i]
        if (i-3) % 6 == 0:
            # print(line)
            p = re.findall('<p>.*</p>', line)
            if len(p) > 0:
                p = p[0]
                p = p.replace(r'\"', r'"')
                # /u**** to chinese
                p = p.encode('utf-8').decode('unicode_escape')

                questions.append(p)
    print(questions)

    htmls = []
    for q in questions:
        htmls.append(q)
        if q in answer_d:
            htmls.append(answer_d[q])
        else:
            htmls.append('<p>Not Found</p>')
        htmls.append('<hr />')

    file_io.write_all_lines('test.html',htmls)