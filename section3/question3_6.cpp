/*
procedure FIXED_POINT(A, low, high)
2:   if low > high then
3:       return false
4:   mid ← floor((low + high) / 2)
5:   if A[mid] = mid then
6:       return true
7:   else if A[mid] < mid then
8:       return FIXED_POINT(A, mid + 1, high)
9:   else
10:      return FIXED_POINT(A, low, mid - 1)
11:  end if
12: end procedure

*/