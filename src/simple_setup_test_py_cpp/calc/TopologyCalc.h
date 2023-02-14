#ifndef TOPOLOGY_CALC_H
#define TOPOLOGY_CALC_H

#include <Eigen/Dense>

namespace simple_setup_test_py {
namespace calc {

  Eigen::Vector3d pointsToVector3d(double x, double y, double z)
  {
    Eigen::Vector3d vec;
    vec[0] = x;
    vec[1] = y;
    vec[2] = z;
    return vec;
  }

  bool segmentIntersectsTriangleWhere(Eigen::Vector3d rayOrigin,
                                      Eigen::Vector3d rayTarget,
                                      Eigen::Vector3d vertex0,
                                      Eigen::Vector3d vertex1,
                                      Eigen::Vector3d vertex2,
                                      Eigen::Vector3d& outIntersectionPoint,
                                      const double EPSILON = 1e-6)
  {
    // Möller-Trumbore intersection algorithm, see
    // https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm
    Eigen::Vector3d edge1 = vertex1 - vertex0;
    Eigen::Vector3d edge2 = vertex2 - vertex0;

    Eigen::Vector3d direction = rayTarget - rayOrigin;
    Eigen::Vector3d dir_norm = direction.normalized();

    Eigen::Vector3d h = dir_norm.cross(edge2);
    double a = edge1.dot(h);

    if (a > -EPSILON && a < EPSILON) {
      return false; // This ray is parallel to this triangle.
    }

    Eigen::Vector3d s = rayOrigin - vertex0;
    double f = 1.0 / a;
    double u = f * s.dot(h);

    if (u < 0.0 || u > 1.0) {
      return false;
    }

    Eigen::Vector3d q = s.cross(edge1);
    double v = f * dir_norm.dot(q);

    if (v < 0.0 || u + v > 1.0) {
      return false;
    }

    // At this stage we can compute t to find out where the intersection point
    // is on the line.
    double t = f * edge2.dot(q);

    if (t > EPSILON &&
        t < sqrt(direction.dot(
              direction))) { // here, adaption for segment, as of
                             // https://stackoverflow.com/a/59475111/3909202
      outIntersectionPoint = rayOrigin + dir_norm * t;
      return true;
    }
    // This means that there is a line intersection but not a ray
    // intersection.
    return false;
  };

  bool segmentIntersectsTriangle(Eigen::Vector3d rayOrigin,
                                 Eigen::Vector3d rayTarget,
                                 Eigen::Vector3d vertex0,
                                 Eigen::Vector3d vertex1,
                                 Eigen::Vector3d vertex2,
                                 const double EPSILON = 1e-6)
  {
    Eigen::Vector3d intersectionPoint;
    return segmentIntersectsTriangleWhere(rayOrigin,
                                          rayTarget,
                                          vertex0,
                                          vertex1,
                                          vertex2,
                                          intersectionPoint,
                                          EPSILON);
  }
}
}

#endif
