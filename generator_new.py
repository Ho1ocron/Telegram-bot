import os
from docx.shared import Pt
from docx import Document


def opendocx():
    run = doc.add_paragraph().add_run("Just a word.") 
    run.font.size = Pt(24)
    run.bold = False
    for i in sub.keys(): 
        doc.save(f"{sub7[i]}.docx")
        doc.save(f"{sub8[i]}.docx") 
        doc.save(f"{sub9[i]}.docx") 
        

path = os.path.abspath(__file__)
path = path.replace("\generator.py", "")


folder = list(os.walk(path))
print(folder)

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
    "Информатика": "Information_science",
    "Программирование": "Programming",
}
sub7 = {
    "Алгебра": "Algebra7",
    "Физика": "Physics7",
    "Русский": "Russian7",
    "Биология": "Biology7",
    "География": "Geography7",
    "Литература": "Literature7",
    "Геометрия": "Geometry7",
    "История": "History7",
    "Обществознание": "Social_Studies7",
    "ОБЖ": "OBJ7",
    "Информатика": "Information_science7",
    "Программирование": "Programming7",
}
sub8 = {
    "Алгебра": "Algebra8",
    "Физика": "Physics8",
    "Русский": "Russian8",
    "Биология": "Biology8",
    "География": "Geography8",
    "Литература": "Literature8",
    "Геометрия": "Geometry8",
    "История": "History8",
    "Обществознание": "Social_Studies8",
    "ОБЖ": "OBJ8",
    "Информатика": "Information_science8",
    "Программирование": "Programming8",
}
sub9 = {
    "Алгебра": "Algebra9",
    "Физика": "Physics9",
    "Русский": "Russian9",
    "Биология": "Biology9",
    "География": "Geography9",
    "Литература": "Literature9",
    "Геометрия": "Geometry9",
    "История": "History9",
    "Обществознание": "Social_Studies9",
    "ОБЖ": "OBJ9",
    "Информатика": "Information_science9",
    "Программирование": "Programming9",
}

opendocx()