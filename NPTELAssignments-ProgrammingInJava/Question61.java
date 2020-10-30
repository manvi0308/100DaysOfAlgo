public class Question61 extends Thread{
	public void run(){
		System.out.print("Thread is Running.");
	}

	public static void main(String args[]){  

		// Creating object of thread class
		Question61 thread=new Question61();  

                // Start the thread
		thread.start();
	}  
}
