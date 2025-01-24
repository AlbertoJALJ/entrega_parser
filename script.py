import csv
import json
import sys


def csv_to_json(csv_file_path, json_file_path, tipo, cantidad_cajas, numero_envio):
    with open(csv_file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        productos = []
        # Conjunto para llevar el control de numero_sanchez únicos
        numero_sanchez_vistos = set()

        for row in reader:
            # Convertir 'numero_sanchez' a string
            num_sanchez = str(row["numero_sanchez"])

            # Verificar si ya existe en el conjunto de vistos
            if num_sanchez in numero_sanchez_vistos:
                # Si ya existe, saltamos esta fila
                continue

            # Marcar como visto
            numero_sanchez_vistos.add(num_sanchez)

            # Eliminar comillas simples en costo
            costo_limpio = row["costo"].replace("'", "")

            # Crear el diccionario del producto
            producto = {
                "numero_sanchez": num_sanchez,
                "enviados": int(row["enviados"]),  # Convierte a entero
                "costo": costo_limpio,  # String sin comillas simples
                "linea": str(row["linea"]),
            }
            productos.append(producto)

    # Estructura JSON final
    data = {
        "tipo": str(tipo),
        "cantidad_cajas": int(cantidad_cajas),
        "numero_envio": str(numero_envio),
        "productos": productos,
    }

    # Guardar la estructura en un archivo JSON
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    """
    Ejemplo de uso:
        python csv_to_json.py archivo.csv salida.json "Canasta" 2 70
    """
    if len(sys.argv) < 6:
        print(
            "Uso: python csv_to_json.py <csv_file> <json_file> <tipo> <cantidad_cajas> <numero_envio>"
        )
        sys.exit(1)

    csv_file = sys.argv[1]
    json_file = sys.argv[2]
    tipo = sys.argv[3]
    cantidad_cajas = sys.argv[4]
    numero_envio = sys.argv[5]

    csv_to_json(csv_file, json_file, tipo, cantidad_cajas, numero_envio)
    print(f"JSON generado correctamente en {json_file}")
