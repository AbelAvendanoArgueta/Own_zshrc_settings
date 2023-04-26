import os
import shutil

# Definir la ruta del archivo de origen y el archivo de destino
origen = os.path.join(os.environ['HOME'], '.zshrc')
destino = '.zshrc'

# Copiar el contenido del archivo de origen al archivo de destino
shutil.copy(origen, destino)
