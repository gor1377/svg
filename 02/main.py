import svgwrite

dwg = svgwrite.Drawing("pyphagore.svg", profile='tiny')
# размер холста
dwg.viewbox(minx=0, miny=0, width=400, height=400, )

# заливка фона
dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='rgb(250,255,251)'))

# вывод таблица пифагора
for i in range(1,11):
    for j in range(1,11):
            text = str(i * j)
            dwg.add(dwg.text(
                text,
                insert=(i * 35, j * 35),
                fill='black',
                font_size='20px',
                font_weight="bold"))
            # добавление рамки
            dwg.add(dwg.rect(
                insert=(i * 35, j * 35),
                size = (40, 40) ,
                fill='red',
                stroke=svgwrite.rgb(255, 255, 0, '%')))

dwg.save()