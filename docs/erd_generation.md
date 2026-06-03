# Generar ERD (erd.png) desde erd.puml

Si PlantUML no está disponible en el entorno, seguir estos pasos localmente para generar la imagen ERD:

1. Instalar PlantUML o descargar plantuml.jar desde https://plantuml.com/download
2. Ejecutar (usando Java):
   java -jar plantuml.jar -tpng -o docs erd.puml
3. Alternativamente, instalar la extensión PlantUML en VS Code y abrir `erd.puml`, luego generar PNG/SVG con la extensión.

Nota: en este repositorio `erd.puml` ya está presente en la raíz. Una vez generado `docs/erd.png`, reemplazar el enlace en README_PROYECTO.md para mostrar la imagen.
