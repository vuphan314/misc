#include <iostream>

using namespace std;

int pivotselection(int*, int, int);

void quicksort(int* d, int low, int high) {
  int pivot_location;

  if(low<high) {
    pivot_location = pivotselection(d, low, high);
    quicksort(d, low, pivot_location);
    quicksort(d, pivot_location + 1, high);
  }
}

int pivotselection(int* d, int low, int high) {
  int pivot = d[low];
  int left = low;
  int x, i;
  for (i = low + 1; i <= high; i++) {
    if (d[i] < pivot) {
      left = left + 1;

      x = d[i];
      d[i] = d[left];
      d[left] = x;
    }
  }
  d[low] = d[left];
  d[left] = pivot;

  return left;
}

void mainHardCoded() {
  int d = 3;
  int a[d] = {20, 30, 10};

  quicksort(a, 0, d - 1);
  cout << "Quick sort ran..." << endl;

  for (int b = 0; b < d; b++) {
    cout << a[b] << " ";
  }
}

void mainUserInput() {
  int b,d,a[20];

  cout<<"Enter how many elements in list"<<endl;
  cin>>d;

  cout<<"Enter element to add to the list"<<endl;
  for(b=0;b<d;b++){
    cin>>a[b];
  }

  quicksort(a,0,d-1);
  cout<<"Quick sort ran..."<<endl;
  for(b=0; b<d;b++){
      cout<<a[b]<<endl;
  }
}

int main() {
  mainHardCoded();
  // mainUserInput();
}
