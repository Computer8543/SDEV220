import multiprocess
import current_time

if __name__ == "__main__":
    # Set up 3 processes
    process_1 = multiprocess.Process(target=current_time.print_current_time)
    process_2 = multiprocess.Process(target=current_time.print_current_time)
    process_3 = multiprocess.Process(target=current_time.print_current_time)

    # Start processes
    process_1.start()
    process_2.start()
    process_3.start()
    
    # make main program wait until the processes are done
    process_1.join()
    process_2.join()
    process_3.join()
   
    
    
    # end program
    exit()
