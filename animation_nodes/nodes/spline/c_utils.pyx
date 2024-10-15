import cython
from libc.math cimport cos
from libc.math cimport M_PI as PI
from ... data_structures.meshes.mesh_data import calculateCrossProducts
from .. mesh.c_utils import matricesFromNormalizedAxisData
from ... data_structures cimport (
    Vector3DList, EdgeIndicesList, FloatList,
    Spline, Matrix4x4List, VirtualFloatList
)
from ... math cimport scaleMatrix3x3Part, Vector3, subVec3, angleVec3

def getMatricesAlongSpline(Spline spline, Py_ssize_t amount, distribution):
    assert spline.isEvaluable()
    spline.ensureNormals()
    cdef Vector3DList points = spline.getDistributedPoints(amount, distributionType = distribution)
    cdef Vector3DList tangents = spline.getDistributedTangents(amount, distributionType = distribution)
    cdef Vector3DList normals = spline.getDistributedNormals(amount, distributionType = distribution)
    cdef FloatList radii = spline.getDistributedRadii(amount, distributionType = distribution)

    tangents.normalize()
    normals.normalize()
    cdef Vector3DList bitangents = calculateCrossProducts(normals, tangents)

    cdef Matrix4x4List matrices = matricesFromNormalizedAxisData(points, normals, bitangents, tangents)
    cdef Py_ssize_t i
    for i in range(amount):
        scaleMatrix3x3Part(matrices.data + i, radii.data[i])

    return matrices

def tiltSplinePoints(Spline spline, VirtualFloatList tilts, bint accumulate):
    cdef FloatList splineTilts = spline.tilts
    cdef Py_ssize_t i
    cdef float offset = 0
    if accumulate:
        for i in range(len(splineTilts)):
            offset += tilts.get(i)
            splineTilts.data[i] += offset
    else:
        for i in range(len(splineTilts)):
            splineTilts.data[i] += tilts.get(i)

    spline.markChanged()

def wrapSplineParameters(FloatList parameters):
    cdef FloatList result = FloatList(length = len(parameters))
    cdef Py_ssize_t i
    for i in range(len(parameters)):
        result.data[i] = parameters.data[i] % 1.0
        if parameters.data[i] != 0 and result.data[i] == 0:
            result.data[i] = 1.0
    return result
