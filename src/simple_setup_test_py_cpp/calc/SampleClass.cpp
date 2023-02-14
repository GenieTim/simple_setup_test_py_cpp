#include "SampleClass.h"

namespace simple_setup_test_py {
namespace calc {
  void SampleClass::setValue(int val) { this->value = val; }

  int SampleClass::getValue() { return this->value; }
}
}