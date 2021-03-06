from os import path
import fontforge

chars = {{chars}}
font = fontforge.open("{{fontpath}}")
fontname = ""
if not font.cidfamilyname is None :
    fontname = font.cidfamilyname
elif not font.familyname is None :
    fontname = font.familyname
else :
    fontname = os.path.splitext(font.default_base_filename)[0]

print fontname

l = len(chars)
for i in range(0, l):
    char = chars[i]
    try:
        uni = font[char].unicode
        if uni != char:
            chars.append(uni)
        alts = font[char].altuni
        if alts is None:
            continue
        for alt in alts:
            if alt[0] != char:
                chars.append(alt[0])
    except TypeError:
        pass

for c in chars:
    font.selection.select(("more", None), c)
font.selection.invert()
font.clear()

font.generate("{{exportpath}}")