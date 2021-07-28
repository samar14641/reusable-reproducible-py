""":mod level docstr"""

from typing import List, Tuple


__all__= [
    'reu_repro_py'
]

def reu_repro_py(file1: str, file2: str) -> List[Tuple[str, str]]:
    """Function to open and iter through 2 files
    
    :param file1: file path of first file
    :param file2: file path of second file
    :returns: pairs of lines from the files
    """
    with open(file1) as f1, open(file2) as f2:
        res = []

        for line1, line2 in zip(f1, f2):
            # yield line1, line2
            res.append((line1.strip(), line2.strip()))

    return res