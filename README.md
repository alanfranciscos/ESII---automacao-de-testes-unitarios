## TestesUnitarios
Projeto Aula Testes Unitários | Banco-Usuarios

Disciplina Engenharia de Software II

Professora: Luciane Santos

Curso Sistemas de Informação da FAI - 6º Período Noturno

## SETUP Instalação PyCharm

Link para baixar o PyCharm - https://www.jetbrains.com/pycharm/download/#section=windows

Dicas: https://www.jetbrains.com/help/pycharm/installation-guide.html

Instalação Conda Link para baixar o Conda: https://www.anaconda.com/download/

Dicas:https://conda.io/projects/conda/en/latest/user-guide/install/macos.html


```bash
pip install -r requirements.txt
```

## Unittest

```bash
python -m unittest -v
```

## Pytest

```bash
pytest .
```

## Test Coverage

- `coverage` and `pytest-cov` packages are required
- Add `pragma: no cover` to exclude code from coverage report

### With `pytest`

Terminal report:

 ```bash
pytest --cov-report term-missing --cov .
 ```

HTML report:

```bash
pytest --cov-report html --cov .
```

### With `unittest`

To generate report:

```bash
python -m coverage run -m unittest
```

To view report in terminal:

```bash
python -m coverage report
```

To view report in HTML:

```bash
python -m coverage html
```

