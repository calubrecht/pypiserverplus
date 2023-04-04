import typing as t
from .core import PkgFile
from wheel_inspect import inspect_wheel, inspect_dist_info_dir

def getPkgInfo(pkg: PkgFile) -> t.Optional[dict]:  # Replace dict with actual class
    if not pkg:
        return {}
    if pkg.fn.endswith("whl"):
      output = inspect_wheel(pkg.fn)
    else:
      output = inspect_dist_info_dir(pkg.fn)
    if "validation_error" in output:
        return {}
    metadata = output['dist_info']['metadata']
    pkgInfo = {}
    pkgInfo["info"] = {'author':'', 'author_email':'', 'classifier': metadata['classifier'], 'description': metadata['readme']}

    return pkgInfo
