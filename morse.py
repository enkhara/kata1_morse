
morse = {
    'A':'·—', 
    'B':'—···', 
    'C': '—·—·', 
    'D': '—··', 
    'E': '·', 
    'F': '··—·',  
    'G': '——·',
    'H': '····', 
    'I': '··',
    'J': '·———',
    'K': '—·—',
    'L': '·—··',
    'M': '——',
    'N': '—·',
    'Ñ': '——·——', 
    'O': '———',
    'P': '·——·',
    'Q': '——·—',
    'R': '·—·', 
    'S': '···',
    'T': '—',
    'U': '··—',
    'V': '···—',
    'W': '·——',
    'X': '—··—',
    'Y': '—·——', 
    'Z': '——··',
    '0': '—————',
    '1': '·————',
    '2': '··———',
    '3': '···——',
    '4': '····—',
    '5': '·····',
    '6': '—····',
    '7': '——···', 
    '8':'———··',
    '9': '————·',
    '.': '·—·—·—',
    ',': '—·—·——',
    '?': '··——··',
    '"': '·—··—·',
    '!': '——··——'
    }

reverso = {}

for key in morse:
    valor = morse[key]
    reverso[valor] = key

def toMorse(texto):
    texto = texto.upper()
    resultado = ''
    for letra in texto:
        if letra in morse:
            resultado += morse[letra]
            resultado += ' '
        else:
           resultado += ' '
    
    return resultado

def toPlain(codigo):
    codigo = codigo.split(' ')


    resultado = ''
    for i  in range(len(codigo)):
        
        if codigo[i] in reverso:
            resultado += reverso[codigo[i]]
            resultado += ''
        else:
            resultado += ' '
    return(resultado.capitalize())

def telegram(remitente, destinatario, mensaje):
    document = Document()
    fechahora = datatime.now()
    hoy = fecha