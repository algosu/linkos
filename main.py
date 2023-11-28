import re

# Input and output file names
input_file_name = "linkos.txt"
output_file_name = "clean_linkos.txt"

# Define the specific URL endings to filter
endings_to_filter = [".ad", ".ae", ".af", ".ag", ".ai", ".al", ".am", ".an", ".ao", ".aq",
    ".ar", ".as", ".at", ".au", ".aw", ".ax", ".az", ".ba", ".bb", ".bd",
    ".be", ".bf", ".bg", ".bh", ".bi", ".bj", ".bm", ".bn", ".bo", ".bq",
    ".bs", ".bt", ".bv", ".bw", ".by", ".bz", ".ca", ".cc", ".cd", ".cf",
    ".cg", ".ch", ".ci", ".ck", ".cl", ".cm", ".cn", ".cr", ".cu",
    ".cv", ".cw", ".cx", ".cy", ".cz", ".de", ".dj", ".dk", ".dm", ".do",
    ".dz", ".ec", ".ee", ".eg", ".eh", ".er", ".es", ".et", ".eu", ".fi",
    ".fj", ".fk", ".fm", ".fo", ".ga", ".gb", ".gd", ".ge", ".gf", ".gg",
    ".gh", ".gi", ".gl", ".gm", ".gn", ".gp", ".gq", ".gr", ".gs", ".gt",
    ".gu", ".gw", ".gy", ".hk", ".hm", ".hn", ".hr", ".ht", ".hu", ".id",
    ".ie", ".il", ".im", ".in", ".io", ".iq", ".ir", ".is", ".je", ".jm",
    ".jo", ".jp", ".ke", ".kg", ".kh", ".ki", ".km", ".kn", ".kp", ".kr",
    ".kw", ".ky", ".kz", ".la", ".lb", ".lc", ".li", ".lk", ".lr", ".ls",
    ".lt", ".lu", ".lv", ".ly", ".ma", ".mc", ".md", ".me", ".mg", ".mh",
    ".mk", ".ml", ".mm", ".mn", ".mo", ".mp", ".mq", ".mr", ".ms", ".mt",
    ".mu", ".mv", ".mw", ".mx", ".my", ".mz", ".na", ".nc", ".ne", ".nf",
    ".ng", ".ni", ".nl", ".no", ".np", ".nr", ".nu", ".nz", ".om", ".pa",
    ".pe", ".pf", ".pg", ".ph", ".pk", ".pl", ".pm", ".pn", ".pr", ".ps",
    ".pt", ".pw", ".py", ".qa", ".re", ".ro", ".rs", ".ru", ".rw", ".sa",
    ".sb", ".sc", ".sd", ".se", ".sg", ".sh", ".si", ".sj", ".sk", ".sl",
    ".sm", ".sn", ".so", ".sr", ".ss", ".st", ".sv", ".sx", ".sy", ".sz",
    ".tc", ".td", ".tf", ".tg", ".th", ".tj", ".tk", ".tl", ".tm", ".tn",
    ".to", ".tr", ".tt", ".tv", ".tw", ".tz", ".ua", ".ug", ".us", ".uy",
    ".uz", ".va", ".vc", ".ve", ".vg", ".vi", ".vn", ".vu", ".wf", ".ws",
    ".xk", ".ye", ".yt", ".za", ".zm", ".zw", ".co.uk",".com.au",".com.cn",
    ".co.jp",".com.br",".co.za",".com.sg",".co.nz",".co.kr",".gov", ".gov.uk", ".gov.au"]


# Read URLs from the input file and filter them
filtered_urls = []

with open(input_file_name, "r") as input_file:
    urls = input_file.readlines()

for url in urls:
    url = url.strip()  # Remove leading/trailing whitespace
    if not any(ending in url and not url.endswith(".com" + ending) for ending in endings_to_filter):
        filtered_urls.append(url)

# Save the filtered URLs to the output file
with open(output_file_name, "w") as output_file:
    for url in filtered_urls:
        output_file.write(url + "\n")

print(f"Filtered URLs have been saved to {output_file_name}")
