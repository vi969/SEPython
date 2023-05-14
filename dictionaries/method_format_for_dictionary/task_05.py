import sys

name = sys.argv[1]
height_meter = sys.argv[2]
height_feet = sys.argv[3]

mountain = {
    "name": name,
    "height": {
        "meters": int(height_meter),
        "feet": int(height_feet)
    }
}
m_template = "{m[name]} - {m[height][meters]} м ({m[height][feet]} ф)"
m_template = m_template.format(m=mountain)
print(m_template)
