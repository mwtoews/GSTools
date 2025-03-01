# -*- coding: utf-8 -*-
"""
GStools subpackage providing miscellaneous tools.

.. currentmodule:: gstools.tools

Export
^^^^^^

.. autosummary::
   :toctree: generated

   vtk_export
   vtk_export_structured
   vtk_export_unstructured
   to_vtk
   to_vtk_structured
   to_vtk_unstructured

Special functions
^^^^^^^^^^^^^^^^^

.. autosummary::
   :toctree: generated

   confidence_scaling
   inc_gamma
   inc_gamma_low
   exp_int
   inc_beta
   tplstable_cor
   tpl_exp_spec_dens
   tpl_gau_spec_dens

Geometric
^^^^^^^^^

.. autosummary::
   :toctree: generated

   rotated_main_axes
   set_angles
   set_anis
   no_of_angles
   rotation_planes
   givens_rotation
   matrix_rotate
   matrix_derotate
   matrix_isotropify
   matrix_anisotropify
   matrix_isometrize
   matrix_anisometrize
   ang2dir
   generate_grid
   generate_st_grid

Misc
^^^^

.. autosummary::
   EARTH_RADIUS

----

.. autodata:: EARTH_RADIUS
"""

from gstools.tools.export import (
    to_vtk,
    to_vtk_structured,
    to_vtk_unstructured,
    vtk_export,
    vtk_export_structured,
    vtk_export_unstructured,
)
from gstools.tools.geometric import (
    ang2dir,
    generate_grid,
    generate_st_grid,
    givens_rotation,
    matrix_anisometrize,
    matrix_anisotropify,
    matrix_derotate,
    matrix_isometrize,
    matrix_isotropify,
    matrix_rotate,
    no_of_angles,
    rotated_main_axes,
    rotation_planes,
    set_angles,
    set_anis,
)
from gstools.tools.special import (
    confidence_scaling,
    exp_int,
    inc_beta,
    inc_gamma,
    inc_gamma_low,
    tpl_exp_spec_dens,
    tpl_gau_spec_dens,
    tplstable_cor,
)

EARTH_RADIUS = 6371.0
"""float: earth radius for WGS84 ellipsoid in km"""


__all__ = [
    "vtk_export",
    "vtk_export_structured",
    "vtk_export_unstructured",
    "to_vtk",
    "to_vtk_structured",
    "to_vtk_unstructured",
    "confidence_scaling",
    "inc_gamma",
    "inc_gamma_low",
    "exp_int",
    "inc_beta",
    "tplstable_cor",
    "tpl_exp_spec_dens",
    "tpl_gau_spec_dens",
    "set_angles",
    "set_anis",
    "no_of_angles",
    "rotation_planes",
    "givens_rotation",
    "matrix_rotate",
    "matrix_derotate",
    "matrix_isotropify",
    "matrix_anisotropify",
    "matrix_isometrize",
    "matrix_anisometrize",
    "rotated_main_axes",
    "ang2dir",
    "generate_grid",
    "generate_st_grid",
    "EARTH_RADIUS",
]
