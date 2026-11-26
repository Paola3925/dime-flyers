# Flyers de luces decorativas de Dime. Uso: python3 flyers_deco.py  (lee PRICES; si un producto no tiene precio muestra "Consultá precio")
from PIL import Image, ImageDraw, ImageFont
import os
HERE=os.path.dirname(os.path.abspath(__file__))
A=HERE+'/assets/'
D=A+'deco/'
F='/usr/share/fonts/truetype/google-fonts/'
BG=(32,32,32); OR=(247,148,30); CREAM=(250,246,242)
bold=lambda s: ImageFont.truetype(F+'Poppins-Bold.ttf',s)
med=lambda s: ImageFont.truetype(F+'Poppins-Medium.ttf',s)
PRICES={'manguera_solar':'$48.400','estrella_solar':'$14.500','lampara_pared':'$29.000','tira_arroz':'$8.700','vela_solar_x6':'$5.600','gota_solar': '$16.500', 'abeja_solar': '$26.600', 'cortina_lluvia': '$11.400', 'cortina_3x3': '$30.200', 'red_2x2': '$18.400', 'ramo_hada': '$32.700', 'cerezo_solar': '$44.800', 'kermes_solar': '$67.800'}
logo=Image.open(A+'logo_orig.png').convert('RGBA')
SETS={
 'solares':('LUCES SOLARES','Sin cables y sin gasto de luz',[
   ('manguera_solar','Manguera solar 20 m','Luz cálida para exterior'),
   ('estrella_solar','Guirnalda estrellas','Solar, 5 m, 20 LED'),
   ('gota_solar','Guirnalda gotas','Solar, 5 m, 20 LED cálida'),
   ('abeja_solar','Guirnalda abejas','Solar, 7 m, 50 luces')]),
 'navidad':('NAVIDAD','Cortinas y guirnaldas para brillar',[
   ('cortina_lluvia','Cortina lluvia','3 m, 100 LED, efectos'),
   ('cortina_3x3','Cortina 3x3 m','300 LED, interconectable'),
   ('red_2x2','Red 2x2 m','168 LED cálida'),
   ('tira_arroz','Guirnalda arroz','10 m, 220 V, efectos')]),
 'rincon':('DECORÁ TU RINCÓN','Luces que cambian el ambiente',[
   ('ramo_hada','Ramo de hadas','144 LED cálida, 2,2 m'),
   ('vela_solar_x6','Vela solar sueltas','Efecto llama, valor c/u'),
   ('cerezo_solar','Árbol flor de cerezo','Solar, pack x2'),
   ('lampara_pared','Lámpara de pared','Recargable, 3 tonos RGB')]),
}
def cover(img,w,h):
    img=img.convert('RGB'); r=max(w/img.width,h/img.height)
    img=img.resize((int(img.width*r)+1,int(img.height*r)+1)); x=(img.width-w)//2; y=(img.height-h)//2
    return img.crop((x,y,x+w,y+h))
CONTAIN={'estrella_solar','gota_solar','vela_solar_x6','lampara_pared'}
def contain(img,w,h):
    img=img.convert('RGB'); bgc=img.getpixel((3,3)); r=min(w/img.width,h/img.height)
    im2=img.resize((max(1,int(img.width*r)),max(1,int(img.height*r)))); b=Image.new('RGB',(w,h),bgc); b.paste(im2,((w-im2.width)//2,(h-im2.height)//2)); return b
def flyer(key):
    title,sub,items=SETS[key]
    W,H=1080,1350
    c=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(c)
    d.rectangle((60,60,150,66),fill=OR)
    d.text((60,90),title,font=bold(88 if len(title)<14 else 74),fill=(255,255,255))
    d.text((62,200),sub,font=med(36),fill=(210,210,210))
    for i,(k,n,s) in enumerate(items):
        x=60+(i%2)*510; y=270+(i//2)*465
        card=Image.new('RGB',(470,440),CREAM)
        card.paste((contain if k in CONTAIN else cover)(Image.open(D+k+'.png'),470,300),(0,0))
        cd=ImageDraw.Draw(card)
        cd.text((24,312),n,font=bold(28),fill=(20,20,20))
        cd.text((24,350),s,font=med(21),fill=(110,110,110))
        p=PRICES.get(k)
        cd.text((24,380),p if p else 'Consultá precio',font=bold(36 if p else 28),fill=(215,115,15))
        m=Image.new('L',(470,440),0); ImageDraw.Draw(m).rounded_rectangle((0,0,469,439),32,fill=255)
        c.paste(card,(x,y),m)
    d.rounded_rectangle((60,1200,1020,1320),30,fill=OR)
    lg=logo.copy(); lg.thumbnail((290,80)); d.rounded_rectangle((78,1214,378,1306),20,fill=CREAM); c.paste(lg,(78+(300-lg.width)//2,1214+(92-lg.height)//2),lg)
    d.text((405,1212),'Pedí por WhatsApp',font=med(30),fill=(20,20,20)); d.text((405,1248),'351 349 8646',font=bold(48),fill=(20,20,20))
    d.text((730,1292),'Recta Martinoli 8791',font=med(18),fill=(20,20,20)) if False else None
    return c
def story(im,text='NOVEDAD EN DIME'):
    W,H=1080,1920; y=(H-im.height)//2
    c=Image.new('RGB',(W,H),BG); c.paste(im,(0,y))
    ImageDraw.Draw(c).text((60,y-120),text,font=bold(54),fill=OR); return c
if __name__=='__main__':
    os.makedirs(HERE+'/out',exist_ok=True)
    for k in SETS:
        f=flyer(k); f.save(f'{HERE}/out/deco_{k}.jpg',quality=95); story(f).save(f'{HERE}/out/deco_{k}_estado.jpg',quality=95)

def hero_kermes(price=None):
    """Flyer destacado: Kermés solar 5 m con lámparas vintage."""
    W,H=1080,1350
    c=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(c)
    d.rectangle((60,60,150,66),fill=OR)
    d.text((60,90),'KERMÉS SOLAR',font=bold(88),fill=(255,255,255))
    d.text((62,200),'Lámparas vintage, 5 metros',font=med(36),fill=(210,210,210))
    amb=Image.open(D+'kermes_ambiente.png'); prod=Image.open(D+'kermes_producto.png')
    big=cover(amb,500,860); m=Image.new('L',(500,860),0); ImageDraw.Draw(m).rounded_rectangle((0,0,499,859),32,fill=255); c.paste(big,(60,270),m)
    small=contain(prod,430,330); sm=Image.new('L',(430,330),0); ImageDraw.Draw(sm).rounded_rectangle((0,0,429,329),28,fill=255); c.paste(small,(590,270),sm)
    y=640
    for t,f,col in [('Energía solar',bold(40),(255,255,255)),('Lámparas vintage',med(30),(210,210,210)),('de 5 metros',med(30),(210,210,210)),('para exterior',med(30),(210,210,210))]:
        d.text((590,y),t,font=f,fill=col); y+=52 if f is not None else 0
    d.text((590,1000),price if price else 'Consultá precio',font=bold(44 if price else 38),fill=OR)
    d.rounded_rectangle((60,1190,1020,1320),30,fill=OR)
    lg=logo.copy(); lg.thumbnail((290,80)); d.rounded_rectangle((78,1204,378,1306),20,fill=CREAM); c.paste(lg,(78+(300-lg.width)//2,1204+(102-lg.height)//2),lg)
    d.text((405,1212),'Pedí por WhatsApp',font=med(30),fill=(20,20,20)); d.text((405,1248),'351 349 8646',font=bold(48),fill=(20,20,20))
    return c
if __name__=='__main__':
    h=hero_kermes(PRICES.get('kermes_solar')); h.save(HERE+'/out/deco_kermes.jpg',quality=95); story(h).save(HERE+'/out/deco_kermes_estado.jpg',quality=95)
