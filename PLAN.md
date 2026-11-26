# Dime Iluminación y Electricidad – plan de redes (para ejecutar en sesiones programadas)

Negocio: Recta Martinoli 8791, Córdoba. WhatsApp 351 349 8646. Instagram @dime_iluminacion (Windsor connector `instagram`, cuenta 17841441557324448).
Tienda online: https://claude.ai/artifact/5dZ5V7nhw8FvUB4SeBL7b7
Promo diciembre: descuento especial pagando en EFECTIVO (no inventar porcentaje).

## Productos y precios de venta (IVA incluido)
- Colgante Hersh soga y metal: $62.900 (assets/hersh_armado.jpg, hersh_kit.png)
- Colgante Mann blanco: $71.200 (mann_blanco.png, mann_ambiente.png)
- Colgante Tas 100 negro lineal LED 120 cm: $125.800 (tas-100-colgante_negro-ambiente.png)
- Colgante Jade Hexagon negro LED: $232.300 (jade-hexagon_negro.png)
- Plafón Medusa Wood 5 luces negro: $157.300 (medusa-wood-5-luces_negro.png, _ambiente.png)
- Plafón Gad negro/blanco: $203.300 (gad_negro.png, gad_blanco.png, gad_ambiente.png)
- Plafón Bag 30 cm negro/blanco: $145.200 (bag-30cm_blanco.png, bag-30cm_ambiente.png)
- Velador Petit táctil cobre: $36.300 (petit_cobre-colores.png)

## Estilo de flyer (ver flyer_colgantes.jpg y flyer_colgantes_estado.jpg)
Fondo gris oscuro #202020, naranja #F7941E, títulos blancos en Poppins Bold (/usr/share/fonts/truetype/google-fonts/), tarjetas blancas con foto, nombre, descripción y precio naranja, pie naranja con logo (assets/logo_orig.png), "Pedí por WhatsApp 351 349 8646" y "Recta Martinoli 8791 · Córdoba".
Feed: 1080x1350 JPG. Historia/estado: 1080x1920 JPG (flyer centrado, título "NOVEDAD EN DIME" arriba).

## Publicar
Subir el JPG a este repo (rama main) y usar la URL https://raw.githubusercontent.com/Paola3925/dime-flyers/main/<archivo>.jpg con Windsor `create_image_post` / `create_story` (connector instagram). Caption: gancho corto + precio + WhatsApp + dirección + 10 a 12 hashtags (#iluminacion #colgantes #decoracion #diseñodeinteriores #cordoba #cordobaargentina #iluminacioncordoba #deco #hogar #arquitectura #electricidad). Nombrar archivos con fecha: AAAA-MM-DD_tema.jpg.

## Calendario (hasta 24/12/2026)
Sem 26/11-2/12 colgantes y plafones. 3-9/12 luces decorativas y veladores de regalo. 10-16/12 ambientá tus fiestas. 17-24/12 última semana, retiro rápido y horarios.
Lun feed + historia. Mar historia consejo/encuesta. Mié reel (no se puede crear video: usar historia). Jue feed. Vie historia "para el finde". Sáb historia/consejo. Dom nada en Instagram.
Siempre dejar el flyer vertical para el estado de WhatsApp y avisar por push (la dueña lo sube a mano; WhatsApp no tiene API de estados).

## Luces decorativas (proveedor Topluva) – flyers ya armados
Fotos recortadas en assets/deco/. Script flyers_deco.py: completar el dict PRICES con los precios de venta cuando la dueña los pase (regla: costo x2 x1,21 redondeado a $100) y volver a correrlo para regenerar los flyers con precio. Mientras no haya precio los flyers dicen "Consultá precio".
Flyers listos (feed 1080x1350 y vertical *_estado.jpg 1080x1920) en la raíz del repo: deco_navidad.jpg (cortinas y guirnaldas de Navidad), deco_solares.jpg (guirnaldas y mangueras solares), deco_rincon.jpg (ramo de hadas, velas solares, árbol cerezo, lámpara de pared).
Orden sugerido: lun 30/11 feed deco_navidad; jue 3/12 feed deco_solares; lun 7/12 feed deco_rincon; los días de historia usar las versiones *_estado.jpg de esos mismos tres. Hasta el 24/12 priorizar Navidad y solares. Si faltan precios, el caption dice "Consultá precio por WhatsApp 351 349 8646".
Antes de publicar cualquiera de estos, confirmar con la dueña que el producto está en stock en el local (no prometer disponibilidad).
