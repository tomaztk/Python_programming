import os
import pypandoc

LESSONS_DIR = "lessons"   # folder with 01, 02, ..., 24
OUTPUT_MD = "merged_lessons_v2.md"
OUTPUT_PDF = "lessons_book_v2.pdf"


def strip_yaml_frontmatter(text):
    """Remove YAML metadata blocks starting with --- at the beginning of a file."""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return "\n".join(lines[i+1:])
    return text


def merge_markdown(lessons_dir):
    with open(OUTPUT_MD, "w", encoding="utf-8") as outfile:

        outfile.write("---\n")
        outfile.write("title: Lessons Book for Python Programming\n")
        outfile.write("author: Inspire Academy\n")
        outfile.write("Date: August, 2025\n")
        outfile.write("geometry: margin=1in\n")
        outfile.write("fontsize: 11pt\n")
        outfile.write("linkcolor: blue\n")
        outfile.write("---\n\n")

        # Pandoc and TOC?????
        outfile.write("# Table of Contents\n\n")
        outfile.write("[[_TOC_]]\n\n")

        lesson_folders = sorted(
            [d for d in os.listdir(lessons_dir) if os.path.isdir(os.path.join(lessons_dir, d))]
        )

        for lesson_folder in lesson_folders:
            lesson_path = os.path.join(lessons_dir, lesson_folder)
            outfile.write(f"# Lesson {lesson_folder}\n\n")


            md_files = sorted([f for f in os.listdir(lesson_path) if f.endswith(".md")])

            for md_file in md_files:
                md_path = os.path.join(lesson_path, md_file)

                if "theory" in md_file.lower():
                    outfile.write("## Theory\n\n")
                elif "exercise" in md_file.lower():
                    outfile.write("## Exercise\n\n")
                else:
                    outfile.write(f"## {os.path.splitext(md_file)[0].title()}\n\n")

                with open(md_path, "r", encoding="utf-8") as mdfile:
                    content = strip_yaml_frontmatter(mdfile.read())
                    outfile.write(content + "\n\n")


def convert_to_pdf():
    pypandoc.convert_text(
        open(OUTPUT_MD, encoding="utf-8").read(),
        to="pdf",
        format="md",
        outputfile=OUTPUT_PDF,
        extra_args=[
            "--toc",          
            "--toc-depth=2",  
            "--pdf-engine=xelatex",
            "-V", "colorlinks=true",  
            "-V", "linkcolor=blue",  
        ],
    )
    print(f" PDF created: {OUTPUT_PDF}")


if __name__ == "__main__":
    #merge_markdown(LESSONS_DIR)
    convert_to_pdf()