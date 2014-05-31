! full code

program demo 
	print *, "In main program"
	call sub1()
	call sub2()
end program demo 

subroutine sub1()
	print *, "In sub1"
end subroutine

subroutine sub2()
	print *, "In sub2"
end subroutine
