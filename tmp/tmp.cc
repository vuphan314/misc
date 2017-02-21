using namespace std;

#include <iostream>
#include <vector>

template<typename T>
void swapIndicies(vector<T> &A, size_t i, size_t j) {
  T tmp = A[i];
  A[i] = A[j];
  A[j] = tmp;
}

template<typename T>
void swapElement(vector<T> &A, size_t i, T &el) {
  T tmp = A[i];
  A[i] = el;
  el = tmp;
}

template<typename T>
T getPivot(vector<T> &A, size_t low, size_t high) {
  T pivot = A[low];
  size_t left = low;
  for (size_t i = low + 1; i <= high; i++) {
    if (A[i] < pivot) {
      swapIndicies(A, i, left);
      left++;
    }
  }
  swapElement(A, left, pivot);
  return left;
}

template<typename T>
void sortquick(vector<T> &A, size_t low, size_t high) {
  if (low < high) {
    size_t pivot = getPivot(A, low, high);
    sortquick(A, low, pivot);
    sortquick(A, pivot + 1, high);
  }
}

int main(int argc, char const *argv[]) {
  vector<int> A{7,2,5,1,29,6,4,19,11};
  sortquick(A, 0, A.size() - 1);
  for (auto el : A) {
    cout << el << ", ";
  }
}
