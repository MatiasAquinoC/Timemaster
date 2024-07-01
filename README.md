# Proyecto de Fin de Asignatura: Gestor de Tiempo Multipropósito "TimeMaster"

## Descripción
El proyecto tiene como objetivo desarrollar una aplicación de gestión de tiempo multipropósito llamada "TimeMaster". Esta aplicación combinará un temporizador, una alarma y un temporizador Pomodoro. Permitirá a los usuarios configurar y gestionar diferentes tipos de temporizadores según sus necesidades, con la capacidad de iniciar, pausar, reiniciar y salir de cada uno de ellos. Además, la aplicación incluirá un ring de 3 segundos que se activará al finalizar cada temporizador.

## Objetivos del Proyecto
- Desarrollar una aplicación que satisfaga las necesidades de gestión de tiempo de los usuarios.
- Implementar un temporizador estándar, una alarma y un temporizador Pomodoro con funcionalidades completas.
- Proporcionar una interfaz intuitiva y fácil de usar para configurar y controlar los temporizadores.
- Integrar un sistema de notificación al finalizar cada temporizador para mejorar la experiencia del usuario.

## Integrantes del Equipo de Desarrollo
- Contreras Bullón Daniel
- Llacza Isidro Miguel
- Vilcarano De la Cruz Frank
- Aquino Castro Matias
- Patiño Reynoso Alberto

## Requerimientos Técnicos
1. Base de Datos SQLite: Utilizar una base de datos SQLite para almacenar la configuración de los temporizadores y los registros de uso.
2. Lenguaje de Programación: Desarrollar la aplicación utilizando el lenguaje de programación Python.
3. Control de Versiones: Utilizar un sistema de control de versiones como Git para gestionar el código fuente del proyecto y utilizar GitHub para compartir el código.
4. Docker: Configurar la aplicación para ejecutarse en un contenedor Docker, facilitando la implementación y la gestión de dependencias.
5. Pruebas:
   - Pruebas Unitarias: Desarrollar pruebas unitarias para validar el comportamiento individual de cada componente.
   - Pruebas de Integración: Realizar pruebas de integración para verificar la interacción entre los diferentes módulos de la aplicación.
   - Pruebas del Sistema: Realizar pruebas del sistema para validar el funcionamiento global de la aplicación.
   - Pruebas de Aceptación: Realizar pruebas de aceptación para verificar que la aplicación cumple con los requisitos funcionales y no funcionales especificados.

## Tecnologías utilizadas
- Flask
- MySQL
- Railway
- Pytest
- HTML y CSS

## Pasos para configurar el proyecto
Comandos para inicializar el proyecto.
```
python -m virtualenv env
pip install -r requirements.txt
```
Link de configuración de ejemplo para la base de datos en Railway (tiempo limite de 36 horas) por link, tiene que ser asignado al valor SQLALCHEMY_DATABASE_URI
```
mysql://root:jAZCoqCuPCosufYyDcuSIKCHWAjfFXNi@roundhouse.proxy.rlwy.net:45746/railway
```
Comando para ejecutar los tests
```
pytest
```
Comando para ejecutar el proyecto
```
python index.py
```
