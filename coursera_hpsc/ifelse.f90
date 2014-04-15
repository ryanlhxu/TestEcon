program ifelse
	implicit none 
	real(kind=8) :: x 
	integer :: i 

	i=3
	if (i<=2) then 
	    print *, "i is less or equal to 2"
	else if (i/=5) then 
	    print *, "i is greater than 2, not equal to 5"
	else 
		print *, " i is equal to 5"
    endif
end program ifelse


