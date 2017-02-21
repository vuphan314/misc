// I don't know why your code is incorrect

#include <iostream>
using namespace std;

int pivotselection(int [], int, int);

void quicksort(int d[], int low, int high) {
  int pivot_location;

  if(low<high){
    pivot_location = pivotselection(d,low,high);
    quicksort(d,low,pivot_location);
    quicksort(d,pivot_location+1,high);
  }
}

int pivotselection(int d[], int low, int high) {
  int pivot = d[low];
  int left = low;
  int x, i, n;
  for(i = low + 1; i <= high; i++) {
    if (d[i] < pivot) {
      x = d[i];
      d[i] = d[left];
      d[left] = x;
      left = left + 1;
    }
  }
  n = pivot;
  pivot = d[left];
  d[left] = n;

  return left;
}

int main() {
  int d = 4;
  int a[] = {4,8,2,5};
  int b;
  quicksort(a, 0, d - 1);
  cout << "Quick sort ran..." << endl;
  for (b = 0; b < d; b++) {
    cout << a[b] << endl;
  }
/*
  int x,b,d,a[20];
  cout<<"Enter number here: "<<endl;
  cout<<"Enter how many elements in list"<<endl;
  cin>>d;
  cout<<"Enter element to add to the list"<<endl;
  for(b=0;b<d;b++){
    cin>>a[b];
  }
  quicksort(a,0,d);
  cout<<"Quick sort ran..."<<endl;
  for(b=0; b<d;b++){
      cout<<a[b]<<endl;
  }
*/
return 0;
}
