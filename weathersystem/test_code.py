import unittest
from unittest.mock import patch
from weather_analyzer import plot_temperatures

class TestPlotTemperaturesFunction(unittest.TestCase):

    @patch('matplotlib.pyplot.plot')
    @patch('matplotlib.pyplot.show')
    @patch('seaborn.lineplot')
    @patch('plotly.graph_objects.Figure.show')
    def test_plot_temperatures_calls(self, mock_plotly_show, mock_seaborn_lineplot, mock_matplotlib_show, mock_matplotlib_plot):
        # Example data
        temperatures = [20, 22, 21, 23]
        average = 21.5
        highest = 23
        lowest = 20

        # Call the function
        plot_temperatures(temperatures, average, highest, lowest)

        # Assert Matplotlib plot was called (adjust based on your implementation)
        self.assertTrue(mock_matplotlib_plot.called)

        # Assert Matplotlib show was called once
        mock_matplotlib_show.assert_called_once()

        # If your implementation uses Seaborn, check if Seaborn's lineplot was called
        # self.assertTrue(mock_seaborn_lineplot.called)

        # If your implementation uses Plotly, check if Plotly's show was called
        # self.assertTrue(mock_plotly_show.called)

if __name__ == '__main__':
    unittest.main()
