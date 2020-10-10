import os

DOUBLE_EXTENSIONS = ['tar.gz', 'tar.bz2']


def basename(filename, extension_depth=None):
    """
    get file basename
    """
    suffixes = _suffixes(filename)
    if not suffixes:
        return ""
    base = suffixes[0]
    suffixes = suffixes[1:]
    if not suffixes:
        return base
    if isinstance(extension_depth, int) and extension_depth > 0:
        extension_depth = -extension_depth
    else:
        ext = ".".join(suffixes[-2:])
        if ext.lower() in DOUBLE_EXTENSIONS:
            extension_depth = -2
        else:
            extension_depth = -1
    return ".".join([base, *suffixes[:extension_depth]])


def extension(filename, extension_depth=None):
    """
    get file extension
    """
    suffixes = _suffixes(filename)
    if not suffixes:
        return ""
    suffixes = suffixes[1:]
    if not suffixes:
        return ""
    if isinstance(extension_depth, int) and extension_depth > 0:
        return ".".join(suffixes[-extension_depth:])
    else:
        ext = ".".join(suffixes[-2:])
        if ext.lower() in DOUBLE_EXTENSIONS:
            return ext
        else:
            return suffixes[-1]


def _suffixes(filename):
    """
    分解文件名
    """
    if not _not_empty(filename):
        return None
    filename = os.path.basename(filename)
    filename = filename.lstrip('.')
    return filename.split('.')


def _not_empty(obj) -> bool:
    """
    判断字符串是不是为空
    """
    return isinstance(obj, str) and len(obj) > 0
