#ifndef SAMPLE_CLASS_H
#define SAMPLE_CLASS_H

#include <Eigen/Dense>

namespace simple_setup_test_py {
namespace calc {
  class SampleClass {
    public:
    void setValue(int val);
    int getValue();

    private:
      int value;
  };
}
}

#endif