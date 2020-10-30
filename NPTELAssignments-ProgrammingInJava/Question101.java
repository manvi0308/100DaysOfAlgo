import java.sql.*;
import java.lang.*;

public class Question101 {
    public static void main(String args[]) {
        try {
              Connection conn = null;
              Statement stmt = null;
              String DB_URL = "jdbc:sqlite:/tempfs/db";
              System.setProperty("org.sqlite.tmpdir", "/tempfs");


              // Open a connection
              conn = DriverManager.getConnection(DB_URL);
              System.out.print(conn.isValid(1));
              conn.close();

        }
       catch(Exception e){ System.out.println(e);}  
    }
}
