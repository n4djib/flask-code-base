
# https://pbpython.com/python-word-template.html
# pip install docx-mailmerge

from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

template = "merge.docx"

document = MailMerge(template)
print(document.get_merge_fields())


document.merge( test1='Gold' )

document.write('test-output.docx')

