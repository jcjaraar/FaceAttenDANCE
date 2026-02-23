🚀 Guía de Configuración de Entorno de Desarrollo: WSL2 + Docker + Git + VS Code

📋 Requisitos Previos
Windows 10/11 (actualizado)
Hardware con virtualización habilitada en BIOS (AMD-V o Intel VT-x)
Conexión a internet

⚙️ PASO 1: Configuración Base de Windows
1.1 Activar características necesarias

# PowerShell como Administrador
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:HypervisorPlatform /all /norestart

1.2 Instalar WSL con distribución por defecto
wsl --install
Esto instala Ubuntu como distribución predeterminada

1.3 Configurar WSL2 como versión predeterminada
wsl --set-default-version 2

1.4 Actualizar kernel de WSL (opcional pero recomendado)
wsl --update
Reiniciar el equipo

📁 PASO 3: Configuración Global de WSL2 (Optimización de Recursos)

3.1 Crear archivo .wslconfig
# PowerShell (como usuario normal, no admin)
notepad "$env:USERPROFILE\.wslconfig"

3.2 Contenido del archivo (ajustar según RAM total)
[wsl2]
# Limitar memoria (ajustar según RAM del equipo)
# - Para 8GB RAM: 3-4GB
# - Para 16GB RAM: 6-8GB
memory=4GB
# Limitar procesadores virtuales
processors=2
# Desactivar swap para evitar uso de disco
swap=0
# Configuraciones experimentales para mejor gestión de memoria
[experimental]
autoMemoryReclaim=gradual

3.3 Aplicar configuración
wsl --shutdown

🐧 PASO 4: Configuración Inicial de Ubuntu

4.1 Iniciar Ubuntu y establecer usuario/contraseña
wsl ~
# Seguir instrucciones: crear usuario y contraseña para Linux

4.2 Actualizar paquetes
sudo apt update && sudo apt upgrade -y
sudo apt autoremove -y

4.3 Instalar herramientas básicas
sudo apt install -y curl wget git htop build-essential

4.4 Verificar conectividad
ping google.com

🔑 PASO 5: Configuración de Git

5.1 Configurar identidad global

git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"

5.2 Configurar editor por defecto (VS Code)
git config --global core.editor "code --wait"

5.3 Configurar saltos de línea (importante para Windows/Linux)
git config --global core.autocrlf input


5.4 Configurar alias útiles
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --all"

5.5 Verificar configuración
git config --list

5.6 Generar clave SSH (para GitHub/GitLab)
ssh-keygen -t ed25519 -C "tu.email@ejemplo.com"
# Aceptar ubicación por defecto (~/.ssh/id_ed25519)
# Opcional: agregar passphrase

# Mostrar clave pública para agregar a GitHub/GitLab
cat ~/.ssh/id_ed25519.pub

📝 PASO 6: Configuración de Visual Studio Code

6.1 Instalar VS Code en Windows
Descargar desde code.visualstudio.com
Instalación estándar

6.2 Instalar extensión "Remote - WSL"
Abrir VS Code
Ir a Extensiones (Ctrl+Shift+X)
Buscar "Remote - WSL" (Microsoft)
Instalar

6.3 Conectar VS Code a WSL

# Método 1: Desde terminal WSL
cd ~/tu-proyecto
code .

# Método 2: Desde PowerShell
wsl ~ -c "cd ~/tu-proyecto && code ."

# Método 3: Comando en VS Code
# F1 → "Remote-WSL: Open Folder in WSL"


6.4 Extensiones recomendadas para WSL
Una vez conectado a WSL, instalar estas extensiones en el entorno WSL:

Extensión					Uso
Remote - WSL				Ya instalada, permite la conexión
GitLens						Visualización avanzada de Git
Git Graph					Visualizar ramas Git
Docker						Manejar contenedores desde VS Code
Prettier					Formateador de código
ESLint						Linting para JavaScript/TypeScript
Python						Si usas Python
Live Share					Colaboración en tiempo real

6.5 Configuración de VS Code para WSL
Crear archivo de configuración en WSL:

# Dentro de WSL, abre settings.json
code ~/.vscode-server/data/Machine/settings.json

Configuración recomendada: (json)

{
    "terminal.integrated.defaultProfile.linux": "bash",
    "terminal.integrated.fontFamily": "Consolas, 'Courier New', monospace",
    "editor.formatOnSave": true,
    "editor.renderWhitespace": "boundary",
    "files.autoSave": "onFocusChange",
    "git.enableSmartCommit": true,
    "git.confirmSync": false
}

🐳 PASO 7: Instalación y Configuración de Docker Desktop

7.1 Descargar e instalar Docker Desktop

Descargar desde docker.com
Instalación estándar (marcar opciones por defecto)

7.2 Configurar integración con WSL2
Abrir Docker Desktop

Settings → Resources → WSL Integration
Activar: "Enable integration with my default WSL distro"
Seleccionar Ubuntu en la lista
Apply & Restart

7.3 Optimizar Docker Desktop
Settings → General → Desmarcar "Start Docker Desktop when you sign in"
Settings → Resources → Activar "Resource Saver" (tiempo: 5 minutos)

7.4 Verificar instalación desde Ubuntu
# Dentro de WSL Ubuntu
docker --version
docker run hello-world


🔗 PASO 8: Flujo de Trabajo Integrado

8.1 Estructura recomendada de proyectos

# Dentro de WSL Ubuntu
mkdir -p ~/projects
cd ~/projects

# Clonar un proyecto
git clone git@github.com:tu-usuario/tu-proyecto.git
cd tu-proyecto

# Abrir en VS Code
code .

8.2 Trabajar con Git desde VS Code

Abrir proyecto en VS Code (conectado a WSL)
Usar la interfaz gráfica de Git en el panel izquierdo
O usar terminal integrada (Ctrl+Ñ) para comandos Git

8.3 Trabajar con Docker desde VS Code

Abrir proyecto en VS Code
Usar extensión Docker para ver contenedores
Click derecho en docker-compose.yml → "Compose Up"

✅ PASO 9: Verificación Final

9.1 Comprobar distribuciones WSL
wsl -l -v
Deberías ver:
Ubuntu (versión 2) como predeterminada (*)
docker-desktop (versión 2)
docker-desktop-data (versión 2)

9.2 Probar flujo completo
# En PowerShell
wsl ~
(bash)
# Dentro de WSL
cd ~/projects
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
code .
# VS Code debería abrirse en WSL
# Verificar que la terminal integrada use bash de WSL

9.3 Verificar Git y SSH
ssh -T git@github.com
# Debería responder: "Hi tu-usuario! You've successfully authenticated"

🎯 PASO 9: Verificación Final

9.1 Comprobar distribuciones WSL
wsl -l -v
Deberías ver:
Ubuntu (versión 2) como predeterminada (*)
docker-desktop (versión 2)
docker-desktop-data (versión 2)

9.2 Establecer Ubuntu como distribución predeterminada
wsl --set-default Ubuntu

9.3 Probar acceso directo
wsl ~
# Debe entrar directamente a Ubuntu sin mensajes adicionales

9.4 Probar flujo completo

# En PowerShell
wsl ~

# Dentro de WSL
cd ~/projects
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
code .
# VS Code debería abrirse en WSL
# Verificar que la terminal integrada use bash de WSL

9.5 Verificar Git y SSH

ssh -T git@github.com
# Debería responder: "Hi tu-usuario! You've successfully authenticated"


📝 PASO 10: Notas para el Usuario Final

10.1 Comandos útiles de WSL

# Ver distribuciones instaladas
wsl -l -v

# Apagar WSL (libera recursos)
wsl --shutdown

# Ejecutar comando específico en WSL sin entrar
wsl ~ -c "comando linux"

# Cambiar distribución predeterminada
wsl --set-default NombreDistro


10.2 Comandos útiles de Docker

# Limpiar recursos no utilizados
docker system prune -a

# Ver contenedores en ejecución
docker ps

# Detener todos los contenedores
docker stop $(docker ps -aq)


10.3 Rutas importantes

Archivos de Windows en WSL: /mnt/c/
Archivos de WSL desde Windows: \\wsl$\Ubuntu
Configuración global WSL: C:\Users\%USERNAME%\.wslconfig
Configuración por distro: /etc/wsl.conf (dentro de la distro)
Claves SSH en WSL: ~/.ssh/

10.4 Atajos de VS Code en WSL

Atajo					Acción
Ctrl+Ñ					Abrir terminal integrado (bash de WSL)
Ctrl+Shift+E			Explorador de archivos
Ctrl+Shift+G			Git
Ctrl+Shift+D			Debug
Ctrl+Shift+X			Extensiones
F1						Comandos (escribir "WSL" para ver opciones)

⚠️ Troubleshooting Rápido

Problema						Solución
Error de virtualización			Verificar BIOS: AMD-V o VT-x activado
WSL no inicia					wsl --shutdown y reiniciar
Docker no encuentra WSL			Verificar integración en Docker Settings
Consumo alto de memoria			Ajustar valores en .wslconfig
VS Code no conecta a WSL		Instalar extensión "Remote - WSL"
Git pide usuario/contraseña 	siempre	Configurar SSH o credential helper
Error de permisos en SSH		chmod 600 ~/.ssh/id_ed25519
Docker no encuentra WSL			Verificar integración en Docker Settings
VS Code lento en WSL			Deshabilitar extensiones innecesarias
"git push" pide token			Usar SSH en lugar de HTTPS


✅ Resumen de Archivos de Configuración

C:\Users\%USERNAME%\.wslconfig
[wsl2]
memory=4GB
processors=2
swap=0
[experimental]
autoMemoryReclaim=gradual

~/.gitconfig (dentro de WSL) (ini)
[user]
    name = Tu Nombre
    email = tu.email@ejemplo.com
[core]
    editor = code --wait
    autocrlf = input
[alias]
    co = checkout
    br = branch
    ci = commit
    st = status
    lg = log --oneline --graph --all
