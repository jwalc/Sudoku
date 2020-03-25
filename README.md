# Sudoku Solver

This little script can solve a sudoku given by a string. The string should be of
length 81 and contain digits only. The digit 0 is used to represent missing
positions on the sudoku grid.

## Usage
Create a Solver Object by passing a string
```python
s = Solver("012000570600501004400020008020010050004907800070080010700090005500408006038000940")
```
Solve the Sudoku using the `solve()` method
```python
s.solve()
```
You may print the solution by creating a Sudoku Object
```python
solution = Sudoku(s.solution)
print(solution)
```
Output:
```
683|571|294
457|329|168
===========
829|613|457
164|957|832
375|284|619
===========
746|192|385
591|438|726
238|765|941
```
