import morse
from docx import Document

mensaje = input('Dime algo: ')

telegrama = morse.toMorse(mensaje)
print(telegrama)
original = morse.toPlain(telegrama)
print(original)