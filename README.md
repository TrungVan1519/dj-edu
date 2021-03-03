# How to fix pylint-django error display message
```json
{
  "python.pythonPath": "<path_to_virtual_enviroment_python_interpreter>",
  "python.linting.pylintArgs": [
    "--load-plugins",
    "pylint_django",
    "pylint_django.checkers.migrations",
    "--disable=C0114, C0115, W0222",
    "--disable=imported-auth-user",
    "--disable=invalid-name",
    "--disable=line-too-long",
    "--disable=django-not-configured",
    "--django-settings-module=djEdu.settings"
  ]
}
```
