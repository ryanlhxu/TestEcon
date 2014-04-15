program array
	
	real(kind=8),dimension(:),allocatable :: x
	allocate(x(10))
    x = (/1,2,3,4,5,6,7,8,9,10/)
    print *, x
end program array