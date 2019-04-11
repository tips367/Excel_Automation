import ProcessWorkbook
import AddChart
from pathlib import Path

path = Path('workbooks')
for file in path.glob('*.xlsx'):
    ProcessWorkbook.process_workbook(file)
    AddChart.add_chart(file)

