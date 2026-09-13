import subprocess


PROGRAMAS = {
    "firefox": ["snap", "run", "firefox"],
    "vscodium": ["flatpak", "run", "com.vscodium.codium"],
}


def abrir_programa(nome):
    comando = PROGRAMAS.get(nome)

    if comando is None:
        return "Eu ainda não conheço esse programa."

    subprocess.Popen(comando)

    return f"Abrindo o {nome}."