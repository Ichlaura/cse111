import unittest
from unittest.mock import patch, MagicMock
from tkinter import messagebox
from PIL import Image
import pandas as pd

class TestEvaluacionRespuestas(unittest.TestCase):

    @patch('PIL.Image.open')
    @patch('tkinter.filedialog.askopenfilenames')
    @patch('tkinter.filedialog.askopenfilename')
    def test_cargar_respuestas_estudiantes(self, mock_askopenfilename, mock_askopenfilenames, mock_image_open):
        print("Running test_cargar_respuestas_estudiantes...")
        
        # Simulamos que el archivo se selecciona y se abre correctamente
        mock_askopenfilenames.return_value = ['estudiante1.png', 'estudiante2.png']
        mock_image_open.return_value = MagicMock()  # Simulamos que no hay error al abrir la imagen

        # Llamamos a la función que queremos probar
        cargar_respuestas_estudiantes()  # Asegúrate de que esta función esté definida y funcionando

        # Verificamos que las respuestas se hayan cargado correctamente
        try:
            self.assertEqual(len(respuestas_estudiantes), 2)
            self.assertIn('estudiante1.png', respuestas_estudiantes)
            self.assertIn('estudiante2.png', respuestas_estudiantes)
        except AssertionError as e:
            print(f"Error en test_cargar_respuestas_estudiantes: {e}")
            raise

    @patch('PIL.Image.open')
    @patch('tkinter.filedialog.askopenfilename')
    def test_cargar_respuesta_profesor(self, mock_askopenfilename, mock_image_open):
        print("Running test_cargar_respuesta_profesor...")

        # Simulamos que el archivo del profesor se carga correctamente
        mock_askopenfilename.return_value = 'respuesta_profesor.png'
        mock_image_open.return_value = MagicMock()

        # Llamamos a la función de cargar respuesta del profesor
        cargar_respuesta_profesor()

        # Verificamos que la respuesta del profesor se cargó correctamente
        try:
            self.assertEqual(len(respuestas_profesor), 1)
            self.assertEqual(respuestas_profesor[0], 'respuesta_profesor.png')
        except AssertionError as e:
            print(f"Error en test_cargar_respuesta_profesor: {e}")
            raise

    @patch('PIL.Image.open')
    @patch('tkinter.messagebox.showerror')
    def test_analizar_respuestas(self, mock_showerror, mock_image_open):
        print("Running test_analizar_respuestas...")

        # Simulamos que no se han cargado respuestas
        respuestas_estudiantes.clear()
        respuestas_profesor.clear()

        # Llamamos a la función analizar_respuestas
        analizar_respuestas()

        # Verificamos que se haya mostrado el error correcto
        try:
            mock_showerror.assert_called_with('Error', 'Por favor, cargue las respuestas de los estudiantes y la respuesta correcta primero.')
        except AssertionError as e:
            print(f"Error en test_analizar_respuestas: {e}")
            raise

    @patch('PIL.Image.open')
    @patch('tkinter.messagebox.showerror')
    def test_mostrar_estadisticas(self, mock_showerror, mock_image_open):
        print("Running test_mostrar_estadisticas...")

        # Simulamos que no se han cargado respuestas
        respuestas_estudiantes.clear()
        respuestas_profesor.clear()

        # Llamamos a la función de mostrar estadísticas
        mostrar_estadisticas()

        # Verificamos que se haya mostrado el error adecuado
        try:
            mock_showerror.assert_called_with('Error', 'Por favor, cargue las respuestas de los estudiantes y la respuesta correcta primero.')
        except AssertionError as e:
            print(f"Error en test_mostrar_estadisticas: {e}")
            raise

if __name__ == '__main__':
    unittest.main()
