# Rene Oswaldo Orellana de la O
# Allisson Lourdes Guevara Palma

Planteamiento del problema:

En la vida cotidiana, muchas personas enfrentan dificultades para llevar un control claro de sus gastos mensuales. La falta de organizacion financiera puede generar desequilibrios en el presupuesto, impidiendo tomar decisiones informadas sobre ahorro, inversiones o consumo.
Este problema se agrava cuando los gastos estan dispersos en diferentes categorias (alquiler, comida, transporte, entre otras) y no se cuenta con una herramienta sencilla que permite visualizar el total de manera rapida y confiable

Objetivo de la solucion:

Desarrollamos un programa de escritorio con interfaz grafica utilizando Python y PyQt5 que permita al usuario ingresar sus gastos mensuales por categorias y calcular automaticamente el total. La interfaz debe ser clara, funcional y le agregamos al menos 5 widgets basicos de PyQt5.

Solución implementada en el código:

La aplicación realiza las siguientes funciones:
1. Interfaz gráfica amigable
- Se construye con QWidget y QVBoxLayout para organizar los elementos verticalmente.
- Se incluyen etiquetas (QLabel) para cada categoría de gasto: alquiler, comida, transporte y otros.
- Se usan campos de entrada (QLineEdit) para que el usuario ingrese los montos correspondientes.

2. Botón de acción
- Un botón (QPushButton) permite al usuario ejecutar el cálculo del total.
- Al hacer clic, se activa una función que toma los valores ingresados, los convierte a números y los suma.

3. Visualización del resultado
- El total calculado se muestra en una etiqueta (QLabel) en formato monetario.
- Si el usuario ingresa un valor no numérico, se muestra un mensaje de error amigable.

4. Validación básica
- Se evita que el programa falle si algún campo está vacío o contiene texto no numérico.
- Se usa try-except para manejar errores de conversión.

 Impacto de la solución:

Esta herramienta permite al usuario:
- Tener una visión clara de sus gastos mensuales.
- Evitar errores de cálculo manual.
- Tomar decisiones más informadas sobre su economía personal.