from collections import defaultdict
import os
import httpx

base_def = """from enum import StrEnum

class lexicon(StrEnum):
    \"\"\"Base class for all lexicon enums\"\"\"
    pass
"""

enum_header_template = """
class {name}(lexicon):
    \"\"\"[{label}](https://atproto-tools.getgrist.com/p2SiVPSGqbi8/atproto-tools/p/27#a1.s127.r{id}.c664)\"\"\"
"""

line_template = """    {name} = '{nsid}'\n    '''[{nsid}]({url})'''"""
undocumented_template = """    {name} = '{nsid}'\n    '''{nsid}'''"""

if __name__ == "__main__":
    r = httpx.get("https://docs.getgrist.com/api/docs/p2SiVPSGqbi8oCHS24PnMj/tables/Tags_lexicon_record_types/records")
    t = [rec["fields"] for rec in r.json()["records"] if rec["fields"].get("Lexicons")]

    lex_domains_refs = {rec["id"]: rec["fields"] for rec in httpx.get("https://docs.getgrist.com/api/docs/p2SiVPSGqbi8oCHS24PnMj/tables/Lexicons/records").json()["records"]}

    enum_dict = defaultdict(list)
    for record in t:
        lex_name, rec_name = record["name_pair"].split(" ")
        domain_id = record["Lexicons"]
        lex_name = enum_header_template.format(name=lex_name, label=lex_domains_refs[domain_id]["label"], id=domain_id)
        url = record["web_url"]
        out_template = line_template if url else undocumented_template
        enum_dict[lex_name].append(out_template.format(url=url, name=rec_name, nsid=record["nsid"]))

    code = base_def + "\n".join(
        header + "\n".join(lines)
        for header, lines in enum_dict.items()
    ) + "\n"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "at_url_converter", "lex.py")
    with open(output_path, 'w') as f:
        f.write(code)
