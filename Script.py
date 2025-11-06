print('Mi primer contenedor')

import logging

# Configuración básica del log
logging.basicConfig(
    level=logging.INFO,  # Nivel de los mensajes (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info("La aplicación ha iniciado")
    
    try:
        print("Mi primer contenedor")
        logging.info("Mensaje mostrado correctamente en pantalla")
    except Exception as e:
        logging.error(f"Ocurrió un error: {e}")
    
    logging.info("La aplicación ha finalizado")

if __name__ == "__main__":
    main()

    