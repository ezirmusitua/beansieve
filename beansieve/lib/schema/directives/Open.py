import copy
import json
from beancount.core import data

from .DirectiveWriter import DirectiveWriter


class OpenWriter(DirectiveWriter):
    type = data.Open

    columns = """
      account             VARCHAR
      currencies          VARCHAR
      metadata            VARCHAR
    """

    def get_detail(self, entry):
        metadata = copy.copy(entry.meta)
        metadata.pop('filename')
        metadata.pop('lineno')
        return (entry.account, ','.join(entry.currencies or []), json.dumps(metadata))

    def field_values(self, entry):
        out = [entry[5]]
        if entry[6] is not None:
            out.append(" ".join(entry[6].split(",")))
        metadata: dict = json.loads(entry[7])
        for key in metadata.keys():
            out.append(f"\n\t{key}: \"{metadata[key]}\"")
        return out
