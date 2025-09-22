import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class GastosApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Gastos Mensuales")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Etiquetas y campos
        self.alquiler_label = QLabel("Alquiler:")
        self.alquiler_input = QLineEdit()
        layout.addWidget(self.alquiler_label)
        layout.addWidget(self.alquiler_input)

        self.comida_label = QLabel("Comida:")
        self.comida_input = QLineEdit()
        layout.addWidget(self.comida_label)
        layout.addWidget(self.comida_input)

        self.transporte_label = QLabel("Transporte:")
        self.transporte_input = QLineEdit()
        layout.addWidget(self.transporte_label)
        layout.addWidget(self.transporte_input)

        self.otros_label = QLabel("Otros gastos:")
        self.otros_input = QLineEdit()
        layout.addWidget(self.otros_label)
        layout.addWidget(self.otros_input)

        # Botón
        self.calcular_btn = QPushButton("Calcular Total")
        self.calcular_btn.clicked.connect(self.calcular_total)
        layout.addWidget(self.calcular_btn)

        # Resultado
        self.resultado_label = QLabel("Total: $0.00")
        layout.addWidget(self.resultado_label)

        self.setLayout(layout)

    def calcular_total(self):
        try:
            total = sum([
                float(self.alquiler_input.text() or 0),
                float(self.comida_input.text() or 0),
                float(self.transporte_input.text() or 0),
                float(self.otros_input.text() or 0)
            ])
            self.resultado_label.setText(f"Total: ${total:.2f}")
        except ValueError:
            self.resultado_label.setText("Por favor, ingresa solo números.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GastosApp()
    ventana.show()
    sys.exit(app.exec_())