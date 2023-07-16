import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        clean_string = re.sub(r'<[^>]*>', '', html)
        clean_string = re.sub(r'\n\s*\n', '\n', clean_string)
        with codecs.open(result_file, 'w', 'utf-8') as file:
            file.write(clean_string)


delete_html_tags('draft.html', 'output.txt')
