import typing as t
from .core import PkgFile
from wheel_inspect import inspect_wheel, inspect_dist_info_dir

def getPkgInfo(pkg: PkgFile) -> t.Optional[dict]:  # Replace dict with actual class
    output = inspect_wheel(pkg.fn)
    metadata = output['dist_info']['metadata']
    pkgInfo = {}
    pkgInfo["info"] = {'author':'', 'author_email':'', 'classifier': metadata['classifier'], 'description': metadata['readme']}

    return pkgInfo
