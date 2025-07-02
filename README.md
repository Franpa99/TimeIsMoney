# TimeIsMoney

**TimeIsMoney** es una aplicación web que permite convertir montos entre diferentes monedas y ajustar su valor histórico según la inflación en Estados Unidos.

---

## Características

- Conversión entre distintas monedas usando tasas de cambio actuales.
- Ajuste de valores monetarios entre diferentes años según el Índice de Precios al Consumidor (CPI) de EE. UU.
- Conversión combinada: permite convertir un monto desde una moneda y año de origen a otra moneda y año destino, considerando inflación y tipo de cambio.
- Interfaz web simple y amigable desarrollada con Flask.

---

## Instalación

1. Clonar este repositorio:

   ```bash
   git clone https://github.com/Franpa99/TimeIsMoney.git
   cd TimeIsMoney
   ```

2. (Opcional, recomendado) Crear y activar un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Verificar que el archivo `data/cpi_us.csv` esté presente (ya incluido en el repositorio).

5. Obtener una API Key gratuita en [ExchangeRate-API](https://www.exchangerate-api.com/) y reemplazar el valor correspondiente en `app.py`:

   ```python
   EXCHANGE_API_KEY = 'tu_api_key_aqui'
   ```

---

## Uso

Ejecutar la aplicación:

```bash
python app.py
```

Luego, abrir el navegador y acceder a: [http://localhost:5000](http://localhost:5000)

Ingresá el monto, moneda y año de origen, así como la moneda y año de destino, para obtener el valor ajustado por inflación y convertido.

---

## Estructura del proyecto

```
TimeIsMoney/
├── app.py
├── requirements.txt
├── data/
│   └── cpi_us.csv
├── templates/
│   ├── index.html
│   └── result.html
└── README.md
```

---

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.

---

## Autor

[@Franpa99](https://github.com/Franpa99)