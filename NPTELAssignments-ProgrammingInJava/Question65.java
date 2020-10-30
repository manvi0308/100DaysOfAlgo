class Question65 extends Thread{  
  public void run(){  
    System.out.println("Thread is running.");  
  }  
 public static void main(String args[]){  
    Question65 t=new Question65();  
    System.out.println("Name of thread 't':"+ t.getName());  

// start the thread  
  t.start();  
// set the name
  t.setName("NPTEL");  

   System.out.println("New name of thread 't':"+ t.getName());  
 }  
}

