import os
import webbrowser

print('remember to put fonts on ./fonts/*.ttf\nYes. only ttf files')

dir = './fonts/'

page = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>is my fonts monospace?</title>
  <style>{{font-family-def}}</style>
  <style>{{div-dev}}</style>
</head>
<body>
  <h1 id="Title"></h1>
  {{fonts}}
  <script>
  document.addEventListener("DOMContentLoaded", ()=>{
    setTimeout(()=>{
      document.querySelectorAll("[class^=font_]").forEach((...Fuente)=>{
          let fuente = Fuente[0]
          if (fuente.children[1].offsetWidth !== fuente.children[2].offsetWidth)
              fuente.remove()
      })
      if (document.querySelectorAll("[class^=font_]").length === 0)
          document.write('Non of your fonts is monospaced')
      else
          document.getElementById("Title").innerText = 'Only ' + document.querySelectorAll("[class^=font_]").length + ' of your fonts are technically monospaced'

    },3000)
  });
  </script>
</body>
</html>
"""

style_1 = ''
style_2 = ''
fonts = ''

font_list = os.listdir(dir)

if len(font_list) == 0:
    print('you have no fonts in ./fonts/*')
    exit()

for fuente in os.listdir(dir):
    archivo = fuente.replace('.ttf', '').replace('.TTF', '').replace('(', '_').replace(')', '_').replace(
        ' ', '_').replace('$', '_').replace('.', '_').replace("'", '_').replace('!', '_')
    style_1 += f'@font-face {{ font-family: font_{archivo}; src: url("./fonts/{fuente}"); }}'
    style_2 += f'.font_{archivo} {{ font-family: font_{archivo}; }}'
    fonts += f'<div class="font_{archivo}"><p>{fuente}</p><span>00000000</span><span>11111111</span><span>~ ! # $ % ^ & * ( ) _ + , . / | \ ` - = < > ? {{ }} [ ] : " ;</span></div>'

page = page.replace('{{font-family-def}}', style_1)
page = page.replace('{{div-dev}}', style_2)
page = page.replace('{{fonts}}', fonts)

f = open("result.html", "w")
f.write(page)
f.close()

webbrowser.open('file://' + os.path.realpath('result.html'))

print('bye!')
