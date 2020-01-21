program matrix_multiply
  implicit none
  integer,parameter :: n=1000
  real*8 mat1(n,n),mat2(n,n),prod(n,n)
  integer k,i,j
  real*8 start_time,stop_time

  ! Initialing mat1, mat2
  do i=1,n
     do j=1,n
       mat1(i,j)=i/j
       mat2(i,j)=j/i
    enddo
  enddo

  !Multiply matrix
  call cpu_time(start_time)
  prod=0.0
  do i=1,n
    do j=1,n
      do k=1,n
        prod(i,j)=prod(i,j)+mat1(i,k)*mat2(k,j)
      enddo
    enddo
  enddo
  call cpu_time(stop_time)
  write(*,*)'time required in loop',stop_time-start_time

  call cpu_time(start_time)
  prod=matmul(mat1,mat2)
  call cpu_time(stop_time)
  write(*,*) 'time required in matmul',stop_time-start_time

end program matrix_multiply
