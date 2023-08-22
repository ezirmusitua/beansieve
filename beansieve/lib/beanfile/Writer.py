import copy


class BeanfileWriter():
    def __init__(self, entry):
        self._entry = entry

    def build(self):
        date = self._entry[1]
        return f"{date} {self.directive_content()}{self.multiline_content()}\n"

    def directive_content(self):
        raise Exception(
            f"{type(self._entry)} directive content not implemented")

    def multiline_content(self):
        content = ""
        metadata = copy.copy(self._entry.meta)
        metadata.pop('filename')
        metadata.pop('lineno')
        for key in metadata.keys():
            content += f"\n\t{key}: \"{metadata[key]}\""
        return content
