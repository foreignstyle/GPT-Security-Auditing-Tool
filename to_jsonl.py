import json
import os


if __name__ == '__main__':
    result = list()
    for filename in os.listdir('links/'):
        with open('links/%s' % filename, 'r', encoding = 'utf-8') as infile:
            link = infile.read()
        new_filename=filename.replace('link', 'link')
        with open('checked_links/%s' % new_filename, 'r', encoding = 'utf-8') as infile:
            checked_link = infile.read()
        info = {'prompt': link + '\n\nSCRIPT: ', 'completion': ' ' + checked_link}
        result.append(info)
    with open('dataset.jsonl', 'w') as outfile:
        for i in result:
            json.dump(i, outfile)
            outfile.write('\n')