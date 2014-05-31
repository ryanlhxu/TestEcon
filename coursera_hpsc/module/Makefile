# Makefile

output.txt: main.exe
	./main.exe>output.txt

main.exe: main.o sub1.o sub2.o 
	gfortran main.f90 sub1.o sub2.o -o main.exe

%.o: %.f90
	gfortran -c $<

 