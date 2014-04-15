program vectorops
	implicit none 
	real(kind=8), dimension(3,2) :: a 
	real(kind=8), dimension(2,3) :: b 
	real(kind=8), dimension(3,3) :: c 

    integer :: i
	
	a=reshape((/1.,2.,3.,4.,5.,6./),(/3,2/))

    print *, "a = "
	do i=1,3 
		print *, a(i,:)
	enddo 

    B=transpose(a)
	print *, "B ="
	do i=1,2
		print *, B(i,:)
	enddo  
    
    print *, "c = "
    c=matmul(a,b)
    do i=1,3
		print *, c(i,:)
	enddo 
end program vectorops 

