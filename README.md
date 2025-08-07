# Armería América – Backend API

**armeria‑america** es el backend de una API REST desarrollado en Python utilizando Flask. Fue creado como proyecto académico en el marco de una materia, aplicando diversas herramientas, patrones de diseño y buenas prácticas en el desarrollo de software.

---

##  Contenido

1. [Tecnologías y herramientas](#tecnologías‑y‑herramientas)  
2. [Estructura del proyecto](#estructura‑del‑proyecto)
3. [Instalación y configuración](#instalación‑y‑configuración)  
4. [Ejecución de la aplicación](#ejecución‑de‑la‑aplicación)  


---

## Tecnologías y herramientas

- **Python** y **Flask** como framework web principal  
- Virtualenv o venv para manejo de entornos virtuales  
- Archivos de scripts para entornos:
  - `linux_install.sh` / `windows_install.cmd` para configuración de entornos
  - `linux_boot.sh` / `windows_boot.cmd` para iniciar el servidor
- Ficheros:
  - `requirements.txt` para dependencias  
  - `.gitignore` para ignorar archivos no deseados  

---

## Estructura del proyecto

```text
armeria‑america/
├── app/
│   └── ... (módulos, rutas, controladores, modelos)
├── doc/
│   └── ... (documentación, diagramas UML)
├── app.py
├── requirements.txt
├── linux_install.sh / windows_install.cmd
├── linux_boot.sh / windows_boot.cmd
├── .scannerwork
└── .gitignore
```

---


## ⚙️ Instalación y configuración

### Prerrequisitos
- Python 3.8+
- pip
- PostgreSQL (opcional, se puede usar SQLite para desarrollo)

### Pasos de Instalación

1. **Clonar el repositorio**
  ```bash
   git clone https://github.com/Tote1958/armeria-america.git
   cd armeria-america
  ```

2. **Crear entorno virtual**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configurar variables de entorno necesarias:
   Crear un archivo .env en la carpeta app con las siguentes variables de entorno:
   - USER_DB (Administrador de la base de datos)
   - PASS_DB (Contraseña de la base de datos)
   - URL_DB (URL de la base de datos)
   - NAME_DB (Nombre de la base de datos)

---


## Ejecucion de la Aplicacion
- En Linux/macOS:
  ```bash
   ./linux_boot.sh
  ```
- En Windows:
  ```bash
   .\windows_boot.cmd
  ```

---


## Autores
Proyecto desarrollado por Santino Beltrán Román, Dante Matias Illesca y Franco Roldán como parte de la materia Diseño de Sistemas.
