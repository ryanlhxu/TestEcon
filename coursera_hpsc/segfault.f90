program segfault
	implicit none 
	real(kind=8) :: a(3)
	integer :: i 

	do i =1,1000	
		a(i)=5. 
		print *, i 
		enddo 
	print *, "Finishing running"
end program segfault
