"""Approximate Nudi (legacy ASCII Kannada) -> Unicode decoder, plus Kannada -> Latin transliteration."""
import re
V = {'ಾ','ಿ','ೀ','ು','ೂ','ೃ','ೆ','ೇ','ೈ','ೊ','ೋ','ೌ'}
BASE = [  # longest first handled by sort
 ('ªÀÄ','ಮ'),('ªÀi','ಮ'),('ªÉÄÊ','ಮೈ'),('ªÉÄÃ','ಮೇ'),('ªÉÄ','ಮೆ'),('ªÉÆÃ','ಮೋ'),('ªÉÆ','ಮೊ'),('ªÉÇÃ','ವೋ'),('ªÉÇ','ವೊ'),('AiÀi','ಯ'),('AiÉÄ','ಯೆ'),('AiÉÆ','ಯೊ'),('AiÉÆÃ','ಯೋ'),('AiÀÄ','ಯ'),('gÀhÄ','ಝ'),('«Ä','ಮಿ'),('¬Ä','ಯಿ'),('jhÄ','ಝಿ'),
 ('zs','ಧ'),('¨s','ಭ'),('¥s','ಫ'),('qs','ಢ'),('Ws','ಘ'),('¢ü','ಧಿ'),('¦ü','ಫಿ'),('¨ü','ಭಿ'),('rü','ಢಿ'),
 ('P','ಕ'),('R','ಖ'),('U','ಗ'),('W','ಘ'),('Y','ಙ'),('Z','ಚ'),('b','ಛ'),('d','ಜ'),('k','ಞ'),('l','ಟ'),('o','ಠ'),
 ('q','ಡ'),('t','ಣ'),('v','ತ'),('x','ಥ'),('z','ದ'),('£','ನ'),('¥','ಪ'),('§','ಬ'),('¨','ಭ'),('g','ರ'),('®','ಲ'),('¯','ಲ'),
 ('ª','ವ'),('±','ಶ'),('µ','ಷ'),('¸','ಸ'),('º','ಹ'),('¼','ಳ'),
 ('Q','ಕಿ'),('T','ಖಿ'),('V','ಗಿ'),('X','ಘಿ'),('a','ಚಿ'),('c','ಛಿ'),('f','ಜಿ'),('m','ಟಿ'),('n','ಠಿ'),('r','ಡಿ'),
 ('w','ತಿ'),('y','ಥಿ'),('¢','ದಿ'),('¤','ನಿ'),('¦','ಪಿ'),('©','ಬಿ'),('j','ರಿ'),('°','ಲಿ'),('«','ವಿ'),('²','ಶಿ'),('´','ಷಿ'),
 ('¹','ಸಿ'),('»','ಹಿ'),('½','ಳಿ'),
 ('C','ಅ'),('D','ಆ'),('E','ಇ'),('F','ಈ'),('G','ಉ'),('H','ಊ'),('J','ಎ'),('K','ಏ'),('L','ಐ'),('M','ಒ'),('N','ಓ'),('O','ಔ'),
 ('ÉÆÃ','ೋ'),('ÉÆ','ೊ'),('ÉÃ','ೇ'),('ÉÊ','ೈ'),('É','ೆ'),('Ë','ೌ'),('Á','ಾ'),('Â','ಿ'),('Ã','ೀ'),('Ä','ು'),('Å','ು'),
 ('Æ','ೂ'),('Ç','ೂ'),('È','ೃ'),('À',''),('A','ಂ'),('B','ಃ'),('ï','್'),
]
SUB = 'ಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯ'
SUBS = {chr(0xCC+i): c for i, c in enumerate(SUB)}
SUBS.update({'á':'ಷ','æ':'ರ','ç':'ರ','è':'ಲ','é':'ವ','ê':'ಶ','ë':'ಷ','ì':'ಸ','í':'ಹ','î':'ಳ'})
BASE.sort(key=lambda p: -len(p[0]))
KN = re.compile('[ಀ-೿]')

def decode(s):
    r = _decode(s)
    for a, b in (('್ರ್ರ','್ರ'),('ಿೆ','ೆ'),('ಿೊ','ೊ'),('ಿೇ','ೇ'),('ಿೋ','ೋ'),('uಾ','ಣ')):
        r = r.replace(a, b)
    return r

def _decode(s):
    s = str(s)
    if KN.search(s): return s          # already Unicode
    out = []; i = 0
    while i < len(s):
        ch = s[i]
        if ch in SUBS:                   # subscript: insert before trailing vowel signs
            j = len(out)
            while j > 0 and out[j-1] in V: j -= 1
            out[j:j] = ['್', SUBS[ch]]; i += 1; continue
        if ch == 'ð':                    # reph: ರ್ before last consonant (+its subscripts)
            j = len(out)
            while j > 0 and (out[j-1] in V or out[j-1] == '್' or (j>=2 and out[j-2]=='್')): j -= 1
            j = max(j-1, 0)
            out[j:j] = ['ರ', '್']; i += 1; continue
        for k, u in BASE:
            if s.startswith(k, i):
                if u in V and out and out[-1] and out[-1][-1] == 'ಿ' and u in ('ೀ',):
                    out[-1] = out[-1][:-1]  # ಿ + Ã -> ೀ
                if u == 'ು' and out and out[-1] in ('ು',):
                    pass
                if u == '': i += len(k); break
                out.append(u) if len(u) != 2 or u[1] not in V else out.extend([u[0], u[1]])
                i += len(k); break
        else:
            out.append(ch); i += 1
    return ''.join(out)

CONS = dict(zip('ಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲವಶಷಸಹಳ',
  ['k','kh','g','gh','n','ch','chh','j','jh','n','t','th','d','dh','n','t','th','d','dh','n','p','ph','b','bh','m','y','r','l','v','sh','sh','s','h','l']))
VS = {'ಾ':'a','ಿ':'i','ೀ':'i','ು':'u','ೂ':'u','ೃ':'ru','ೆ':'e','ೇ':'e','ೈ':'ai','ೊ':'o','ೋ':'o','ೌ':'au','್':''}
IV = dict(zip('ಅಆಇಈಉಊಋಎಏಐಒಓಔ',['a','a','i','i','u','u','ru','e','e','ai','o','o','au']))
def translit(u):
    r = []; s = list(u)
    for i, c in enumerate(s):
        if c in CONS:
            r.append(CONS[c]); nx = s[i+1] if i+1 < len(s) else ''
            if nx not in VS: r.append('a')
        elif c in VS: r.append(VS[c])
        elif c in IV: r.append(IV[c])
        elif c == 'ಂ': r.append('n')
        elif c == 'ಃ': r.append('h')
        else: r.append(c)
    return ''.join(r)
if __name__ == '__main__':
    import sys; sys.stdout.reconfigure(encoding="utf-8")
    for t in ['\xb2P\xc1j\xa5\xc0\xc4g\xc0','w\xc3x\xc0\xf0\xba\xc0\xbd\xee','v\xc0\xc4\xaa\xc0\xc4P\xc0\xc6g\xc0\xc4','aP\xc0\xcc\xa3\xc1Ai\xc0\xc4P\xc0\xa3\xc0','f\xaf\xc1\xe8','g\xc1d\xe5','\xab\xa8s\xc1U\xc0','P\xc0\xc4t\xc2U\xc0\xaf\xef','\xa9\xc3z\xc0g\xef','\xabzs\xc1\xa3\xc0\xb8\xc0\xa8s\xc1 P\xc0\xe1\xc9\xc3v\xc0\xe6']:
        d = decode(t); print(d, translit(d))
