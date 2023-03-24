from docx.shared import Pt
from docx import Document


sub = {
    "Алгебра": "Algebra",
    "Физика": "Physics",
    "Русский": "Russian",
    "Биология": "Biology",
    "География": "Geography",
    "Литература": "Literature",
    "Геометрия": "Geometry",
    "История": "History",
    "Обществознание": "Society",
    "ОБЖ": "OBJ"
}

doc = Document()


def opendocx():
    for _ in range(len(sub)):
        for i in sub.keys():
            run = Document().add_paragraph().add_run([i])
            run.font.size = Pt(24)
            run.bold = True
            doc.save(f"{sub[i]}.docx")


if __name__ == "__main__":
    opendocx()
