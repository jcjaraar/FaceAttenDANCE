#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para limpiar caracteres especiales de archivos .md
Reemplaza emojis y acentos por alternativas ASCII
Ejecutar desde la raíz del repositorio: python limpiar_caracteres.py
"""

import os
import re
from pathlib import Path

# Colores para terminal (opcional, funciona en Windows y Linux)
class Colores:
    VERDE = '\033[92m' if os.name != 'nt' else ''
    AMARILLO = '\033[93m' if os.name != 'nt' else ''
    ROJO = '\033[91m' if os.name != 'nt' else ''
    AZUL = '\033[94m' if os.name != 'nt' else ''
    RESET = '\033[0m' if os.name != 'nt' else ''

# Diccionario de reemplazos (mapeo directo)
REEMPLAZOS = {
    # Emojis comunes
    '🎯': '[OBJETIVO]',
    '✅': '[OK]',
    '❌': '[ERROR]',
    '⚠️': '[ADVERTENCIA]',
    '⚠': '[ADVERTENCIA]',
    '📁': '[CARPETA]',
    '📂': '[CARPETA]',
    '📊': '[GRAFICO]',
    '📈': '[GRAFICO]',
    '📉': '[GRAFICO]',
    '🔍': '[BUSCAR]',
    '🔎': '[BUSCAR]',
    '📝': '[NOTA]',
    '📚': '[LIBROS]',
    '📖': '[LIBRO]',
    '📸': '[FOTO]',
    '📷': '[FOTO]',
    '🔒': '[PRIVADO]',
    '🔓': '[PUBLICO]',
    '💃': '[BAILE]',
    '🕺': '[BAILE]',
    '⭐': '[ESTRELLA]',
    '🌟': '[ESTRELLA]',
    '🔧': '[HERRAMIENTA]',
    '🛠️': '[HERRAMIENTA]',
    '📋': '[LISTA]',
    '📌': '[PIN]',
    '📍': '[PIN]',
    '🔗': '[ENLACE]',
    '📎': '[ADJUNTO]',
    '📏': '[REGLA]',
    '⚙️': '[CONFIG]',
    '⚙': '[CONFIG]',
    '🧪': '[TEST]',
    '🎓': '[TESIS]',
    '📄': '[DOC]',
    '📑': '[DOCS]',
    '📦': '[PAQUETE]',
    '🌐': '[WEB]',
    '📱': '[MOVIL]',
    '💻': '[PC]',
    '🖥️': '[PC]',
    '⌨️': '[TECLADO]',
    '🐍': '[PYTHON]',
    '🐳': '[DOCKER]',
    '🐙': '[GITHUB]',
    '🤝': '[APRETON]',
    '🙏': '[GRACIAS]',
    '👋': '[SALUDO]',
    '🎉': '[FELICIDADES]',
    '✨': '[DESTACADO]',
    '🔥': ['[FUEGO]', ''],
    '💡': '[IDEA]',
    '❓': '[DUDA]',
    '❗': '[IMPORTANTE]',
    '‼️': '[IMPORTANTE]',
    '💾': '[GUARDAR]',
    '📥': '[DESCARGAR]',
    '📤': '[SUBIR]',
    '📧': '[EMAIL]',
    '🔔': '[NOTIFICACION]',
    '🔕': '[SILENCIO]',
    '⏳': '[ESPERA]',
    '⌛': '[ESPERA]',
    '🔄': '[ACTUALIZAR]',
    '▶️': '[REPRODUCIR]',
    '⏸️': '[PAUSA]',
    '⏹️': '[DETENER]',
    '✅': '[OK]',
    '☑️': '[CHECK]',
    '❎': '[NO]',
    '✔️': '[OK]',
    '✖️': '[ERROR]',
    '➕': '[MAS]',
    '➖': '[MENOS]',
    '➗': '[DIVIDIR]',
    '✖': '[MULTIPLICAR]',
    '🔢': '[NUMEROS]',
    '🔣': '[SIMBOLOS]',
    '🔤': '[LETRAS]',
    '💬': '[COMENTARIO]',
    '🗨️': '[DIALOGO]',
    '👤': '[USUARIO]',
    '👥': '[USUARIOS]',
    '👪': '[FAMILIA]',
    '🏠': '[INICIO]',
    '🏢': '[EMPRESA]',
    '🏫': '[ESCUELA]',
    '⏰': '[HORA]',
    '⌚': '[RELOJ]',
    '📅': '[CALENDARIO]',
    '📆': '[CALENDARIO]',
    '🗓️': '[CALENDARIO]',
    '🌡️': '[TEMPERATURA]',
    '🧮': '[CALCULADORA]',
    '🔬': '[MICROSCOPIO]',
    '🔭': '[TELESCOPIO]',
    '💊': '[MEDICINA]',
    '💉': '[INYECCION]',
    '🧬': '[ADN]',
    '🔌': '[CONECTOR]',
    '💡': '[BOMBILLA]',
    '📟': '[BUSCAPERSONAS]',
    '📠': '[FAX]',
    '📺': '[TV]',
    '📻': '[RADIO]',
    '🎙️': '[MICROFONO]',
    '🎚️': '[CONTROL]',
    '🎛️': '[CONTROL]',
    '🧰': '[CAJA_HERRAMIENTAS]',
    '🧲': '[IMAN]',
    '🧪': '[TUBO_ENSAYO]',
    '🧫': '[PLACA_PETRI]',
    '🧬': '[ADN]',
    '🔬': '[MICROSCOPIO]',
    '🔭': '[TELESCOPIO]',
    '📡': '[ANTENA]',
    '💫': '[ESTRELLA_FUGAZ]',
    '⭐': '[ESTRELLA]',
    '🌟': '[ESTRELLA_BRILLANTE]',
    '🌠': '[ESTRELLA_FUGAZ]',
    '🌌': '[VIA_LACTEA]',
    '☄️': '[COMETA]',
    '🪐': '[PLANETA]',
    '🌍': '[TIERRA]',
    '🌎': '[TIERRA]',
    '🌏': '[TIERRA]',
    '🌕': '[LUNA_LLENA]',
    '🌖': '[LUNA_GIBOSA]',
    '🌗': '[LUNA_MENOS]',
    '🌘': '[LUNA_MENGUANTE]',
    '🌑': '[LUNA_NUEVA]',
    '🌒': '[LUNA_CRECIENTE]',
    '🌓': '[CUARTO_CRECIENTE]',
    '🌔': '[LUNA_GIBOSA]',
    '🌙': '[LUNA]',
    '☀️': '[SOL]',
    '☁️': '[NUBE]',
    '⛅': '[NUBLADO]',
    '⛈️': '[TORMENTA]',
    '🌤️': '[SOL_NUBE]',
    '🌥️': '[NUBE]',
    '🌦️': '[LLUVIA]',
    '🌧️': '[LLUVIA]',
    '🌨️': '[NIEVE]',
    '🌩️': '[RAYO]',
    '🌪️': '[TORNADO]',
    '🌫️': '[NIEBLA]',
    '🌬️': '[VIENTO]',
    '🎄': '[NAVIDAD]',
    '🎆': '[FUEGOS_ARTIFICIALES]',
    '🎇': '[FUEGOS_ARTIFICIALES]',
    '🧨': '[PETARDO]',
    '✨': '[DESTELLO]',
    '🎈': '[GLOBO]',
    '🎉': ['[CONFETI]', '[CELEBRACION]'],
    '🎊': '[CONFETI]',
    '🎋': '[ARBOL]',
    '🎍': '[ADORNO]',
    '🎎': '[MUNECAS]',
    '🎏': '[COMETA]',
    '🎐': '[CAMPANA]',
    '🎑': '[LUNA]',
    '🎀': '[MOÑO]',
    '🎁': '[REGALO]',
    '🎗️': '[LAZO]',
    '🎟️': '[ENTRADA]',
    '🎫': '[TICKET]',
    '🏆': '[TROFEO]',
    '🏅': '[MEDALLA]',
    '🥇': '[ORO]',
    '🥈': '[PLATA]',
    '🥉': '[BRONCE]',
    '⚽': '[FUTBOL]',
    '⚾': '[BEISBOL]',
    '🥎': '[PELOTA]',
    '🏀': '[BASQUET]',
    '🏐': '[VOLEY]',
    '🏈': '[FUTBOL_AMERICANO]',
    '🏉': '[RUGBY]',
    '🎾': '[TENIS]',
    '🥏': '[DISCO]',
    '🎳': '[BOWLING]',
    '🏏': '[CRICKET]',
    '🏑': '[HOCKEY]',
    '🏒': '[HOCKEY_HIELO]',
    '🥍': '[LACROSSE]',
    '🏓': '[PING_PONG]',
    '🏸': '[BADMINTON]',
    '🥊': '[BOXEO]',
    '🥋': '[KARATE]',
    '🥅': '[ARCO]',
    '⛳': '[GOLF]',
    '⛸️': '[PATIN]',
    '🎣': '[PESCA]',
    '🤿': '[BUCEO]',
    '🎽': '[CAMISETA]',
    '🎿': '[ESQUI]',
    '🛷': '[TRINEO]',
    '🥌': '[CURLING]',
    '🎯': '[DARDO]',
    
    # Acentos y caracteres especiales
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'ñ': 'n',
    'Á': 'A',
    'É': 'E',
    'Í': 'I',
    'Ó': 'O',
    'Ú': 'U',
    'Ñ': 'N',
    'ü': 'u',
    'Ü': 'U',
    'à': 'a',
    'è': 'e',
    'ì': 'i',
    'ò': 'o',
    'ù': 'u',
    'À': 'A',
    'È': 'E',
    'Ì': 'I',
    'Ò': 'O',
    'Ù': 'U',
    'â': 'a',
    'ê': 'e',
    'î': 'i',
    'ô': 'o',
    'û': 'u',
    'Â': 'A',
    'Ê': 'E',
    'Î': 'I',
    'Ô': 'O',
    'Û': 'U',
    'ã': 'a',
    'õ': 'o',
    'Ã': 'A',
    'Õ': 'O',
    'ç': 'c',
    'Ç': 'C',
    
    # Símbolos
    '¿': '?',
    '¡': '!',
    '…': '...',
    '—': '-',
    '–': '-',
    '•': '-',
    '·': '-',
    '℃': '°C',
    '℉': '°F',
    '№': 'No.',
    '™': '(TM)',
    '®': '(R)',
    '©': '(C)',
    '±': '+/-',
    '×': 'x',
    '÷': '/',
    '≈': '~',
    '≠': '!=',
    '≤': '<=',
    '≥': '>=',
    '∞': '[infinito]',
    '√': '[raiz]',
    '∑': '[suma]',
    '∏': '[producto]',
    '∂': '[derivada]',
    '∫': '[integral]',
    '∆': '[delta]',
    '∇': '[nabla]',
    '∈': '[en]',
    '∉': '[no_en]',
    '∋': '[contiene]',
    '∅': '[vacio]',
    '∩': '[interseccion]',
    '∪': '[union]',
    '⊂': '[subconjunto]',
    '⊃': '[superconjunto]',
    '⊆': '[subconjunto_igual]',
    '⊇': '[superconjunto_igual]',
    '⊕': '[mas_circulo]',
    '⊗': '[por_circulo]',
    '⊥': '[perpendicular]',
    '∠': '[angulo]',
    '∴': '[por_tanto]',
    '∵': '[porque]',
    '∶': '[razon]',
    '∷': '[proporcion]',
    '⟨': '<',
    '⟩': '>',
}

def limpiar_texto(texto):
    """Limpia el texto reemplazando caracteres especiales."""
    for especial, ascii_reemp in REEMPLAZOS.items():
        # Si el reemplazo es una lista, probar cada opción
        if isinstance(ascii_reemp, list):
            for opcion in ascii_reemp:
                if opcion:  # Solo si no está vacío
                    texto = texto.replace(especial, opcion)
        else:
            texto = texto.replace(especial, ascii_reemp)
    
    # Limpiar posibles emojis no mapeados (rangos Unicode de emojis)
    # Rango básico de emojis: U+1F300 a U+1F6FF y otros rangos comunes
    emoji_pattern = re.compile(
        "["
        "\U0001F300-\U0001F6FF"  # Símbolos y pictogramas
        "\U0001F900-\U0001F9FF"  # Símbolos y pictogramas suplementarios
        "\U0001F700-\U0001F77F"  # Símbolos alquímicos
        "\U0001F780-\U0001F7FF"  # Símbolos geométricos
        "\U0001F800-\U0001F8FF"  # Símbolos de flechas suplementarios
        "\U0001F900-\U0001F9FF"  # Símbolos y pictogramas suplementarios
        "\U0001FA00-\U0001FA6F"  # Símbolos de ajedrez
        "\U0001FA70-\U0001FAFF"  # Símbolos y pictogramas
        "\U00002702-\U000027B0"  # Símbolos de dingbats
        "\U000024C2-\U0001F251"  # Símbolos varios
        "]+",
        flags=re.UNICODE
    )
    texto = emoji_pattern.sub('[EMOJI]', texto)
    
    return texto

def limpiar_archivo(ruta):
    """Limpia un archivo de caracteres especiales."""
    try:
        # Leer archivo
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Limpiar contenido
        contenido_limpio = limpiar_texto(contenido)
        
        # Si hubo cambios, guardar
        if contenido_limpio != contenido:
            # Crear backup (opcional)
            # backup = ruta.with_suffix(ruta.suffix + '.bak')
            # with open(backup, 'w', encoding='utf-8') as f:
            #     f.write(contenido)
            
            # Guardar archivo limpio
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(contenido_limpio)
            
            return True, len(contenido_limpio) - len(contenido)
        else:
            return False, 0
            
    except Exception as e:
        return False, str(e)

def main():
    """Limpia todos los archivos .md del proyecto recursivamente."""
    print(f"{Colores.AZUL}{'='*70}{Colores.RESET}")
    print(f"{Colores.AMARILLO}🧹 LIMPIANDO CARACTERES ESPECIALES EN ARCHIVOS .md{Colores.RESET}")
    print(f"{Colores.AZUL}{'='*70}{Colores.RESET}")
    
    raiz = Path('.')
    total_archivos = 0
    modificados = 0
    total_cambios = 0
    
    # Buscar todos los archivos .md recursivamente
    for ruta in raiz.rglob('*.md'):
        # Excluir carpetas del sistema
        if any(p in str(ruta) for p in ['.git', 'venv', '__pycache__', '.venv']):
            continue
        
        total_archivos += 1
        print(f"{Colores.AZUL}Procesando: {ruta}{Colores.RESET}")
        
        modificado, cambios = limpiar_archivo(ruta)
        
        if modificado:
            modificados += 1
            if isinstance(cambios, int):
                total_cambios += cambios
                print(f"{Colores.VERDE}  ✓ Modificado ({cambios} caracteres){Colores.RESET}")
            else:
                print(f"{Colores.ROJO}  ✗ Error: {cambios}{Colores.RESET}")
        else:
            print(f"  - Sin cambios")
    
    print(f"{Colores.AZUL}{'='*70}{Colores.RESET}")
    print(f"{Colores.VERDE}✅ PROCESO COMPLETADO{Colores.RESET}")
    print(f"   Archivos encontrados: {total_archivos}")
    print(f"   Archivos modificados: {modificados}")
    if total_cambios:
        print(f"   Total caracteres reemplazados: {total_cambios}")
    print(f"{Colores.AZUL}{'='*70}{Colores.RESET}")
    
    if modificados > 0:
        print(f"\n{Colores.AMARILLO}📝 NOTA: Se modificaron {modificados} archivos.{Colores.RESET}")
        print(f"   Revisa los cambios con 'git diff' antes de commitear.")

if __name__ == "__main__":
    main()