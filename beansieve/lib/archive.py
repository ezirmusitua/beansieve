from beansieve.lib.beanfile.Reader import BeancountFileReader
from beansieve.lib.fs import mkdir
from beansieve.lib.structure import Structure


def archive(source: str, dest: str, period: str):
    mkdir(dest)
    entries, option = BeancountFileReader.read(source)
    structure = Structure(dest, option)
    for entry in entries:
        if entry < period:
            structure.append(entry)
        else:
            structure.append_main(entry)
    structure.write()
