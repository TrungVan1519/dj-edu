# How to fix pylint-django error display message

[Solution](https://stackoverflow.com/questions/65761250/pylint-django-raising-error-about-django-not-being-configured-when-thats-not-th "Solution")

`.vscode/settings.json`

```json
{
  "python.pythonPath": "<path_to_virtual_enviroment_python_interpreter>",
  "python.linting.pylintArgs": [
    "--load-plugins",
    "pylint_django",
    "pylint_django.checkers.migrations",
    "--disable=C0114, C0115, C0116, W0222, W0511",
    "--disable=imported-auth-user",
    "--disable=invalid-name",
    "--disable=line-too-long",
    "--disable=django-not-configured",
    "--django-settings-module=djEdu.settings"
  ]
}

```
