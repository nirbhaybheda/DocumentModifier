from docx import Document
def replace_string(filename, data):
    replace_data = data["replace"]
    doc = Document(filename)
    for p in doc.paragraphs:
        for old_text, new_text in replace_data.iteritems():
            if old_text in p.text:
                inline = p.runs
                # Loop added to work with runs (strings with same style)
                for i in range(len(inline)):
                    if old_text in inline[i].text:
                        text = inline[i].text.replace(old_text, new_text)
                        inline[i].text = text
                print p.text
    doc.save('modify_input.docx')
    return 1
