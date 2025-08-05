import java.sql.*;

public class testJDBC {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("Driver loaded!");

            Connection conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/testDB", "gowtham", "root123"
            );

            System.out.println("Connected to MySQL!");

            // Create table
            Statement stmt = conn.createStatement();
            stmt.executeUpdate("CREATE TABLE IF NOT EXISTS students (rollno INT PRIMARY KEY, name VARCHAR(50))");

            // Insert 10 sample records
            stmt.executeUpdate("INSERT INTO students (rollno, name) VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie'), (4, 'David'), (5, 'Eve'), (6, 'Frank'), (7, 'Grace'), (8, 'Heidi'), (9, 'Ivan'), (10, 'Judy')");

            System.out.println("Table created and data inserted!");
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
