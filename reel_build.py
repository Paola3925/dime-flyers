from PIL import Image, ImageDraw, ImageFont
A='/home/claude/dime-flyers/assets/'
F='/usr/share/fonts/truetype/google-fonts/'
BG=(32,32,32); OR=(247,148,30)
W,H=1080,1920
bold=lambda s: ImageFont.truetype(F+'Poppins-Bold.ttf',s)
med=lambda s: ImageFont.truetype(F+'Poppins-Medium.ttf',s)
logo=Image.open(A+'logo_orig.png').convert('RGBA')
def center(d,t,y,f,fill):
    w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=fill)
def fit(img,w,h):
    img=img.convert('RGB'); r=max(w/img.width,h/img.height)
    img=img.resize((int(img.width*r)+1,int(img.height*r)+1)); x=(img.width-w)//2; y=(img.height-h)//2
    return img.crop((x,y,x+w,y+h))
def contain(img,w,h):
    img=img.convert('RGB'); r=min(w/img.width,h/img.height); img=img.resize((int(img.width*r),int(img.height*r)))
    b=Image.new('RGB',(w,h),(255,255,255)); b.paste(img,((w-img.width)//2,(h-img.height)//2)); return b
def slide(name,photo,title,sub,price):
    c=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(c)
    center(d,title,170,bold(70),(255,255,255))
    center(d,sub,265,med(40),(200,200,200))
    p=(contain if photo in ('hersh_armado.jpg','jade-hexagon_negro.png') else fit)(Image.open(A+photo),960,960)
    m=Image.new('L',(960,960),0); ImageDraw.Draw(m).rounded_rectangle((0,0,959,959),40,fill=255)
    c.paste(p,(60,380),m)
    if price:
        center(d,price,1400,bold(120),OR)
    return c,d
def footer(c,d):
    d.rounded_rectangle((60,1640,1020,1820),30,fill=OR)
    lg=logo.copy(); lg.thumbnail((300,90)); d.rounded_rectangle((90,1665,420,1795),20,fill=(250,246,242)); c.paste(lg,(105,1685),lg)
    d.text((450,1670),'Pedí por WhatsApp',font=med(34),fill=(20,20,20)); d.text((450,1712),'351 349 8646',font=bold(54),fill=(20,20,20))
items=[('hersh_armado.jpg','Colgante Hersh','Soga y metal calado','$62.900'),
('mann_ambiente.png','Colgante Mann','Cónico blanco con correa','$71.200'),
('tas-100-colgante_negro-ambiente.png','Colgante Tas 100','Lineal LED negro 120 cm','$125.800'),
('jade-hexagon_negro.png','Colgante Jade Hexagon','LED negro, luz cálida','$232.300')]
for i,(ph,t,s,p) in enumerate(items):
    c,d=slide(i,ph,t,s,p); footer(c,d); c.save(f's{i+1}.png')
# intro
c=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(c)
center(d,'NOVEDAD',640,bold(70),OR); center(d,'COLGANTES',730,bold(150),(255,255,255))
center(d,'desde $62.900',930,bold(80),OR); center(d,'Dale estilo a tu hogar',1080,med(46),(200,200,200))
lg=logo.copy(); lg.thumbnail((600,160)); d.rounded_rectangle((240,1500,840,1680),30,fill=(250,246,242)); c.paste(lg,(240+(600-lg.width)//2,1500+(180-lg.height)//2),lg)
c.save('s0.png')
# outro
c=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(c)
center(d,'Pedí el tuyo',560,bold(100),(255,255,255)); center(d,'por WhatsApp',680,bold(100),OR)
center(d,'351 349 8646',860,bold(90),(255,255,255))
center(d,'Recta Martinoli 8791',1020,med(50),(200,200,200)); center(d,'Córdoba',1085,med(50),(200,200,200))
center(d,'Descuento especial en efectivo',1250,med(46),OR)
lg=logo.copy(); lg.thumbnail((600,160)); d.rounded_rectangle((240,1500,840,1680),30,fill=(250,246,242)); c.paste(lg,(240+(600-lg.width)//2,1500+(180-lg.height)//2),lg)
c.save('s5.png')
