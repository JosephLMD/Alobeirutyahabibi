# -*- coding: utf-8 -*-
"""Genera las seis páginas de Aló Beirut Yahabibi desde un solo sitio.

POR QUÉ UN GENERADOR Y NO SEIS ARCHIVOS SUELTOS

Son seis páginas que comparten barra, menú lateral, pie, botón flotante y
datos de contacto. Escritas a mano, cambiar el teléfono significa tocar seis
archivos y olvidarse de uno. Aquí el teléfono está una vez, en TEL.

La navegación también sale de una sola lista, PAGINAS, así que ninguna página
puede quedar huérfana: todas aparecen en la barra, en el menú lateral y en el
pie, y todas enlazan de vuelta.

Para publicar: python3 construir.py y subir la carpeta a GitHub Pages.
"""
import json, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
DOMINIO = 'https://alobeirutyahabibi.com'
TEL_E164 = '573235056278'
TEL_BONITO = '323 505 6278'
WA = f'https://wa.me/{TEL_E164}'

# ── el orden de aquí es el orden del menú en todas las páginas ──────────
PAGINAS = [
    ('index.html',    'Inicio',           'Inicio'),
    ('menu.html',     'Menú de catering', 'Menú'),
    ('eventos.html',  'Servicio completo','Servicio'),
    ('historia.html', 'La historia',      'Historia'),
    ('ciudades.html', 'Dónde atendemos',  'Ciudades'),
    ('contacto.html', 'Contacto',         'Contacto'),
]

SVG_WA = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 '
 '2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.9 9.9 0 004.79 1.22h.01c5.46 0 '
 '9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm5.8 14.13c-.25.69-1.44 1.32-1.99 1.37-.53.05-1.02'
 '.24-3.45-.72-2.9-1.14-4.73-4.1-4.87-4.29-.14-.19-1.16-1.54-1.16-2.94s.73-2.09 1-2.37c.26-.29.57-'
 '.36.76-.36.19 0 .38 0 .55.01.18.01.41-.07.64.49.24.57.81 1.97.88 2.11.07.14.12.31.02.5-.09.19-.14'
 '.31-.28.47-.14.17-.3.37-.42.5-.14.14-.29.29-.12.57.16.29.73 1.2 1.56 1.95 1.07.95 1.98 1.25 2.26 '
 '1.39.28.14.44.12.6-.07.17-.19.69-.81.88-1.09.19-.28.37-.23.63-.14.26.1 1.65.78 1.93.92.28.14.47.21'
 '.54.33.07.11.07.65-.18 1.34z"/></svg>')


def wa_btn(texto, clase='btn wa', msg=None):
    url = WA + ('?text=' + re.sub(r'\s+', '%20', msg) if msg else '')
    return (f'<a class="{clase}" href="{url}" target="_blank" rel="noopener">{SVG_WA}{texto}</a>')


def cabecera(archivo, titulo, descripcion, og_img='hero-catering-arabe-bogota.jpg', extra_ld=None):
    canon = DOMINIO + '/' + ('' if archivo == 'index.html' else archivo)
    ACT = ' aria-current="page"'
    nav = ''.join('<a href="%s"%s>%s</a>' % (a, ACT if a == archivo else '', corto)
                  for a, _t, corto in PAGINAS)
    panel_nav = ''.join('<a href="%s"%s>%s</a>' % (a, ACT if a == archivo else '', largo)
                        for a, largo, _c in PAGINAS)

    ld = {
      "@context":"https://schema.org","@type":"FoodEstablishment",
      "additionalType":"https://schema.org/CateringBusiness",
      "name":"Aló Beirut Yahabibi",
      "description":"Catering árabe y libanés para matrimonios, quinceañeros y eventos en Bogotá y las principales ciudades de Colombia.",
      "url":DOMINIO+'/',
      "image":f"{DOMINIO}/img/hero-catering-arabe-bogota.jpg",
      "logo":f"{DOMINIO}/img/logo-alo-beirut-yahabibi.jpg",
      "telephone":"+57 "+TEL_BONITO,
      "servesCuisine":["Árabe","Libanesa","Palestina","Costeña"],
      "priceRange":"$$",
      "founder":{"@type":"Person","name":"Zamira Eslait"},
      "address":{"@type":"PostalAddress","addressLocality":"Bogotá",
                 "addressRegion":"Cundinamarca","addressCountry":"CO"},
      "areaServed":[{"@type":"City","name":c} for c in
                    ("Bogotá","Medellín","Cartagena","Barranquilla","Cali")],
      "openingHoursSpecification":[{"@type":"OpeningHoursSpecification",
        "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
        "opens":"09:00","closes":"19:00"}],
    }
    bloques = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    if extra_ld:
        bloques += f'\n<script type="application/ld+json">{json.dumps(extra_ld, ensure_ascii=False)}</script>'

    return f'''<!DOCTYPE html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#1F7A4C">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_CO">
<meta property="og:site_name" content="Aló Beirut Yahabibi">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMINIO}/img/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="img/logo-alo-beirut-yahabibi.jpg">
<link rel="stylesheet" href="estilos.css">
{bloques}
</head>
<body>

<header class="barra">
  <div class="barra-in">
    <a class="marca" href="index.html">
      <img src="img/logo-alo-beirut-yahabibi.jpg" alt="Aló Beirut Yahabibi" width="44" height="55">
      <span><b>Aló Beirut Yahabibi</b><i>Sabores árabes con amor</i></span>
    </a>
    <nav class="nav">{nav}</nav>
    <button class="rayas" id="rayas" aria-expanded="false" aria-controls="panel" aria-label="Abrir menú">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div class="velo" id="velo"></div>
<aside class="panel" id="panel" aria-hidden="true">
  <div class="panel-top">
    <button class="rayas" id="cerrar" aria-label="Cerrar menú"><span></span><span></span><span></span></button>
  </div>
  <nav>{panel_nav}</nav>
  {wa_btn('Cotizar por WhatsApp', 'btn wa ancho')}
  <p class="panel-tel">WhatsApp {TEL_BONITO}<br>Lunes a domingo, 9:00 a 19:00</p>
</aside>
'''


JS_LUPA = '''
<script>
/* LUPA · toca una foto y se abre en grande con su descripción.

   No hay que marcar nada en el HTML: el script recorre las fotos de
   platos, de la carta y de las galerías, y saca el título y el texto
   de lo que ya está escrito al lado de cada una. Así no hay dos
   fuentes de verdad que se puedan desincronizar. */
(function(){
  var fotos = [].slice.call(document.querySelectorAll(
    '.plato img, .item img, .galeria img'));
  if(!fotos.length) return;

  /* de dónde sale el texto de cada foto, según dónde viva */
  function datos(img){
    var p;
    if((p = img.closest('.plato')))
      return {t:(p.querySelector('h3')||{}).textContent || img.alt,
              d:(p.querySelector('p')||{}).textContent || ''};
    if((p = img.closest('.item')))
      return {t:(p.querySelector('b')||{}).textContent || img.alt,
              d:(p.querySelector('small')||{}).textContent || ''};
    if((p = img.closest('figure')))
      return {t:(p.querySelector('figcaption')||{}).textContent || img.alt,
              d:img.alt};
    return {t:img.alt, d:''};
  }

  var caja = document.createElement('div');
  caja.className = 'lupa';
  caja.setAttribute('aria-hidden','true');
  caja.setAttribute('role','dialog');
  caja.setAttribute('aria-modal','true');
  caja.innerHTML =
    '<button class="lupa-x" aria-label="Cerrar">&times;</button>' +
    '<button class="lupa-n lupa-ant" aria-label="Foto anterior">&#8249;</button>' +
    '<button class="lupa-n lupa-sig" aria-label="Foto siguiente">&#8250;</button>' +
    '<figure><img alt=""><figcaption><b></b><span></span></figcaption></figure>' +
    '<p class="lupa-cuenta"></p>';
  document.body.appendChild(caja);

  var gran = caja.querySelector('img'),
      tit  = caja.querySelector('b'),
      des  = caja.querySelector('span'),
      cnt  = caja.querySelector('.lupa-cuenta'),
      i    = 0, antes = null;

  function pintar(n){
    i = (n + fotos.length) % fotos.length;
    var f = fotos[i], d = datos(f);
    gran.src = f.currentSrc || f.src;
    gran.alt = f.alt;
    tit.textContent = d.t;
    des.textContent = d.d;
    cnt.textContent = (i+1) + ' de ' + fotos.length + ' · usa las flechas del teclado';
  }
  function abrir(n){
    antes = document.activeElement;
    pintar(n);
    caja.classList.add('abierta');
    caja.setAttribute('aria-hidden','false');
    document.body.classList.add('sin-scroll');
    caja.querySelector('.lupa-x').focus();
  }
  function cerrar(){
    caja.classList.remove('abierta');
    caja.setAttribute('aria-hidden','true');
    document.body.classList.remove('sin-scroll');
    if(antes && antes.focus) antes.focus();
  }

  fotos.forEach(function(f, n){
    f.setAttribute('data-lupa','');
    /* que también se pueda con teclado, no solo con el dedo */
    f.setAttribute('tabindex','0');
    f.setAttribute('role','button');
    f.setAttribute('aria-label','Ver "' + (f.alt || 'la foto') + '" en grande');
    f.addEventListener('click', function(){ abrir(n); });
    f.addEventListener('keydown', function(e){
      if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); abrir(n); }
    });
  });

  caja.querySelector('.lupa-x').addEventListener('click', cerrar);
  caja.querySelector('.lupa-ant').addEventListener('click', function(){ pintar(i-1); });
  caja.querySelector('.lupa-sig').addEventListener('click', function(){ pintar(i+1); });
  /* tocar el fondo cierra; tocar la foto o el texto, no */
  caja.addEventListener('click', function(e){ if(e.target === caja) cerrar(); });
  document.addEventListener('keydown', function(e){
    if(!caja.classList.contains('abierta')) return;
    if(e.key === 'Escape')     cerrar();
    if(e.key === 'ArrowLeft')  pintar(i-1);
    if(e.key === 'ArrowRight') pintar(i+1);
  });

  /* deslizar con el dedo, que en celular es lo natural */
  var x0 = null;
  caja.addEventListener('touchstart', function(e){ x0 = e.touches[0].clientX; }, {passive:true});
  caja.addEventListener('touchend', function(e){
    if(x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    if(Math.abs(dx) > 55) pintar(dx < 0 ? i+1 : i-1);
    x0 = null;
  }, {passive:true});
})();
</script>
'''

JS_MENU = '''
<script>
/* menú de tres rayas: panel lateral, se cierra con Escape, con el velo y
   al tocar cualquier enlace. El foco vuelve al botón al cerrar. */
(function(){
  var b=document.getElementById('rayas'), p=document.getElementById('panel'),
      v=document.getElementById('velo'), c=document.getElementById('cerrar');
  function abrir(si){
    b.setAttribute('aria-expanded', si);
    p.classList.toggle('abierto', si);
    v.classList.toggle('abierto', si);
    p.setAttribute('aria-hidden', !si);
    document.body.classList.toggle('sin-scroll', si);
    if(!si) b.focus();
  }
  b.addEventListener('click', function(){ abrir(b.getAttribute('aria-expanded')!=='true'); });
  c.addEventListener('click', function(){ abrir(false); });
  v.addEventListener('click', function(){ abrir(false); });
  p.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', function(){ abrir(false); }); });
  document.addEventListener('keydown', function(e){ if(e.key==='Escape') abrir(false); });
})();
</script>
'''


def pie(archivo):
    enlaces = ''.join(f'<li><a href="{a}">{largo}</a></li>' for a, largo, _c in PAGINAS if a != archivo)
    return f'''
<footer>
  <div class="wrap">
    <div class="pie-g">
      <div>
        <h3>Aló Beirut Yahabibi</h3>
        <p>Catering árabe y libanés para eventos. Cocina propia en Bogotá y servicio en las
        principales ciudades de Colombia.</p>
        {wa_btn('Escribir por WhatsApp')}
      </div>
      <div>
        <h3>Contacto</h3>
        <ul>
          <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp {TEL_BONITO}</a></li>
          <li>Bogotá, Colombia</li>
          <li>Lunes a domingo, 9:00 a 19:00</li>
        </ul>
      </div>
      <div>
        <h3>El sitio</h3>
        <ul>{enlaces}</ul>
      </div>
    </div>
    <div class="legal">
      <span>&copy; 2026 Aló Beirut Yahabibi · Sabores árabes con amor</span>
      <span>Hecho en Bogotá</span>
    </div>
  </div>
</footer>

{wa_btn('Cotizar', 'btn wa flota')}
''' + JS_MENU + JS_LUPA + '''
</body>
</html>
'''


COTIZADOR_JS = '''
<script>
/* El cotizador no manda nada a ningún servidor: arma un texto y lo abre en
   WhatsApp. Para una cocina de tres personas sin CRM, el chat ES el CRM, y
   así el sitio sigue siendo estático y gratis de alojar. */
(function(){
  var TEL='%s', el={evento:'',personas:'',ciudad:''};
  var caja=document.getElementById('cotizador'); if(!caja) return;
  caja.querySelectorAll('.opciones').forEach(function(g){
    var k=g.dataset.k;
    g.addEventListener('click', function(e){
      var b=e.target.closest('button'); if(!b) return;
      var ya=b.getAttribute('aria-pressed')==='true';
      g.querySelectorAll('button').forEach(function(o){o.setAttribute('aria-pressed','false');});
      b.setAttribute('aria-pressed', ya?'false':'true');
      el[k]= ya?'':b.dataset.v; pintar();
    });
  });
  var f=document.getElementById('fecha'); if(f) f.addEventListener('change', pintar);
  function pintar(){
    var d=f?f.value:'', t='¡Hola Zamira! Quiero cotizar catering';
    if(el.evento)   t+=' para '+el.evento;
    if(el.personas) t+=', '+el.personas;
    if(el.ciudad)   t+=', '+el.ciudad;
    if(d){ var p=d.split('-'); t+=', el '+p[2]+'/'+p[1]+'/'+p[0]; }
    t+='. ¿Me ayudas con el precio?';
    document.getElementById('vista').textContent=t;
    document.getElementById('enviar').href='https://wa.me/'+TEL+'?text='+encodeURIComponent(t);
  }
  pintar();
})();
</script>
''' % TEL_E164


def cotizador(titulo='Cotiza tu evento en treinta segundos',
              intro='Marca lo que aplique y el mensaje se arma solo. Lo abres en WhatsApp, lo envías y Zamira te responde con el precio.'):
    def grupo(k, et, ops):
        bs = ''.join(f'<button type="button" data-v="{v}">{t}</button>' for v, t in ops)
        return (f'<div class="campo"><span class="et">{et}</span>'
                f'<div class="opciones" data-k="{k}" role="group" aria-label="{et}">{bs}</div></div>')
    return f'''
<section id="cotizar" class="cot">
  <div class="wrap estrecho">
    <h2>{titulo}</h2>
    <p class="lead">{intro}</p>
    <div class="caja-cot" id="cotizador">
      {grupo('evento','¿Qué evento es?',[
        ('un matrimonio','Matrimonio'),('un quinceañero','Quinceañero'),
        ('un bautizo o baby shower','Bautizo o baby shower'),('una despedida de soltera','Despedida'),
        ('un evento de empresa','Empresa'),('una reunión en casa','Reunión en casa')])}
      {grupo('personas','¿Para cuántas personas?',[
        ('de 10 a 25 personas','10 a 25'),('de 25 a 50 personas','25 a 50'),
        ('de 50 a 100 personas','50 a 100'),('más de 100 personas','Más de 100')])}
      {grupo('ciudad','¿En qué ciudad?',[
        ('en Bogotá','Bogotá'),('en Medellín','Medellín'),('en Cartagena','Cartagena'),
        ('en Barranquilla','Barranquilla'),('en Cali','Cali'),('en otra ciudad','Otra ciudad')])}
      <div class="campo">
        <label for="fecha">¿Qué día? (opcional)</label>
        <input type="date" id="fecha">
      </div>
      <p class="vista" id="vista">Tu mensaje aparecerá aquí.</p>
      <a class="btn wa ancho" id="enviar" href="{WA}" target="_blank" rel="noopener">{SVG_WA}Enviar por WhatsApp</a>
    </div>
  </div>
</section>
'''


def miga(actual):
    return (f'<p class="miga"><a href="index.html">Inicio</a> › {actual}</p>')


def plato(img, alt, h3, p, w=1100, h=974):
    return (f'<article class="plato"><img src="img/{img}" alt="{alt}" loading="lazy" '
            f'width="{w}" height="{h}"><div class="cuerpo"><h3>{h3}</h3><p>{p}</p></div></article>')


def galeria(items):
    fs = ''.join(f'<figure><img src="img/{i}" alt="{a}" loading="lazy"><figcaption>{c}</figcaption></figure>'
                 for i, a, c in items)
    return f'<div class="galeria">{fs}</div>'
