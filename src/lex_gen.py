from collections import defaultdict
import os
import httpx

enum_template = """
class {name}(StrEnum):
{lines}
"""

line_template = """    {name} = '{nsid}'\n    '''[{nsid}]({url})'''"""
undocumented_template = """    {name} = '{nsid}'\n    '''{nsid}'''"""

if __name__ == "__main__":
    r = httpx.get("https://docs.getgrist.com/api/docs/p2SiVPSGqbi8oCHS24PnMj/tables/Tags_lexicon_record_types/records")
    t = r.json()

    enum_dict = defaultdict(list)
    for record in t['records']:
        fields = record["fields"]
        lex_name, rec_name = fields["name_pair"].split(" ")
        url = fields["html_url"]
        template = line_template if url else undocumented_template
        line = template.format(url=url, name=rec_name, nsid=fields["nsid"])

        enum_dict[lex_name].append(line)

    code = "".join([enum_template.format(name=enum_name, lines='\n'.join(lines)) for enum_name, lines in enum_dict.items()])

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "atproto_url_converter", "lex.py")
    with open(output_path, 'w') as f:
        f.write("from enum import StrEnum\n")
        f.write(code)
