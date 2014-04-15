program loop
    implicit none
    integer, parameter :: n=10
    real(kind=8), dimension(n) :: x,y
    integer :: i 

    do i=1,n 
       x(i)=3.d0 * i 
       enddo

    do i=1,n
       y(i)=2.d0*i 
       enddo 

    do i=1,n 
       print *, "y(i)=", y(i) 
       enddo
end program loop