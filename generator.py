import os
from docx.shared import Pt
from docx import Document


def opendocx():
    for i in sub.keys():
        run = doc.add_paragraph().add_run("Just a word.")
        run.font.size = Pt(24)
        run.bold = False
        doc.save(f"{sub[i]}.docx")

list0 = []
list1 = []

path = os.path.abspath(__file__)
path = path.replace("\generator.py", "")
print(path)

tree = list(os.walk(path))
for i in tree[0]:
    if type(i) == list:
        list0.append(i)
for i in list0[1]:
    list1.append(i)

doc = Document()

sub = {
    "Алгебра": "Algebra",
    "Физика": "Physics",
    "Русский": "Russian",
    "Биология": "Biology",
    "География": "Geography",
    "Литература": "Literature",
    "Геометрия": "Geometry",
    "История": "History",
    "Обществознание": "Social_Studies",
    "ОБЖ": "OBJ",
    "Информатика": "IT"
}

if __name__ == "__main__":
    for i in sub.values():
        i = f"{i}.docx"
        if i in list1:
            break
        else:
            opendocx()