#cython: language_level=3, boundscheck=False, wraparound=False, cdivision=True
# -*- coding: utf-8 -*-
"""
This is the randomization method summator, implemented in cython.
"""

import numpy as np

cimport cython

from cython.parallel import prange

cimport numpy as np
from libc.math cimport cos, sin


def summate(
    const double[:, :] cov_samples,
    const double[:] z_1,
    const double[:] z_2,
    const double[:, :] pos
    ):
    cdef int i, j, d
    cdef double phase
    cdef int dim = pos.shape[0]

    cdef int X_len = pos.shape[1]
    cdef int N = cov_samples.shape[1]

    cdef double[:] summed_modes = np.zeros(X_len, dtype=float)

    for i in prange(X_len, nogil=True):
        for j in range(N):
            phase = 0.
            for d in range(dim):
                phase += cov_samples[d, j] * pos[d, i]
            summed_modes[i] += z_1[j] * cos(phase) + z_2[j] * sin(phase)

    return np.asarray(summed_modes)


cdef (double) abs_square(const double[:] vec) nogil:
    cdef int i
    cdef double r = 0.

    for i in range(vec.shape[0]):
        r += vec[i]**2

    return r


def summate_incompr(
    const double[:, :] cov_samples,
    const double[:] z_1,
    const double[:] z_2,
    const double[:, :] pos
    ):
    cdef int i, j, d
    cdef double phase
    cdef double k_2
    cdef int dim = pos.shape[0]

    cdef double[:] e1 = np.zeros(dim, dtype=float)
    e1[0] = 1.
    cdef double[:] proj = np.empty(dim)

    cdef int X_len = pos.shape[1]
    cdef int N = cov_samples.shape[1]

    cdef double[:, :] summed_modes = np.zeros((dim, X_len), dtype=float)

    for i in range(X_len):
        for j in range(N):
            k_2 = abs_square(cov_samples[:, j])
            phase = 0.
            for d in range(dim):
                phase += cov_samples[d, j] * pos[d, i]
            for d in range(dim):
                proj[d] = e1[d] - cov_samples[d, j] * cov_samples[0, j] / k_2
                summed_modes[d, i] += proj[d] * (z_1[j] * cos(phase) + z_2[j] * sin(phase))

    return np.asarray(summed_modes)
