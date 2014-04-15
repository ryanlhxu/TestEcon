program arrayassign
	implicit none
	! dummy a
	real(kind=8) :: a
	a=1.
	call setvals(a)
	print *, a
end program arrayassign

subroutine setvals(x)
	implicit none
	real(kind=8), intent(inout) :: x(3)
	integer :: i 

	do i=1,3
		x(i)=i 
	enddo 
end subroutine setvals