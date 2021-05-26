import java.sql.Connection;
import java.sql.DriverManager;

public class DBConnection {
	private static String DRIVER_INFO = "com.mysql.cj.jdbc.Driver";
	private static String DATABASE_URL = "jdbc:mysql://csci5410-dbinstance1.cfprz1ccsmta.ap-south-1.rds.amazonaws.com:3306/aws_testing?user=deep1607&password=Dee16798p*";
	private static String DATABASE_USERNAME = "deep1607";
	private static String DATABASE_PASSWORD = "Dee16798p*";
	
	
	public Connection connectToInstance() {

		Connection conn = null;
		try {
			Class.forName(DRIVER_INFO);
			// conn =
			// DriverManager.getConnection("jdbc:mysql://db.cs.dal.ca:3306/csci3901?serverTimezone=UTC",
			// "dppatel","B00865413");
			
		
			conn = DriverManager.getConnection(DATABASE_URL);
			
			System.out.println("Connection Successful");
						
		} catch (Exception e) {
			System.out.println("ERROR: " + e.getMessage());
		}
		return conn;
	}	
}