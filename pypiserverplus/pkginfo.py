import typing as t
from .core import PkgFile
from wheel_inspect import inspect_wheel, inspect_dist_info_dir
from functools import partial

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

def appendPkgVersions(info: dict, wheelFiles: list, getAbsUrl:partial):
    releases = {}
    for wheelFile in wheelFiles:
        wheel = inspect_wheel(wheelFile.fn)
        vInfo = {"comment_text": "", "digests": {"md5": wheel["file"]["digests"]["md5"], "sha256": wheel["file"]["digests"]["sha256"]}, "filename": wheel["filename"]}
        vInfo["url"] = getAbsUrl(wheelFile.relfn)
        releases[wheel["version"]] = vInfo

    info["releases"] = releases
