import java.sql.Connection;
import java.sql.PreparedStatement;

public class AddUser {

	private String userName = "deep";
	private String password = "Deep";

	public void addUserIntoDatabase() {
		
		DBConnection objConnect = new DBConnection();
		Connection conn = objConnect.connectToInstance();
		
		String userName = "deep";
		String password = "Deep";
		
		EncryptData objEncrypt = new EncryptData();
		objEncrypt.createLookupTable();
		
		try {
		      // the mysql insert statement
		      String sql1 = " insert into users (userID, userPassword)" + " values (?, ?)";

		      // create the mysql insert preparedstatement
		      PreparedStatement preparedStmt = conn.prepareStatement(sql1);
		      preparedStmt.setString (1, userName);
		      preparedStmt.setString (2, objEncrypt.encryptPassword(password));

		      // execute the preparedstatement
		      boolean isInserted = preparedStmt.execute();
			
			
			if(isInserted) {
				System.out.println("Data Inserted!!");
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
		finally {
			try {
				conn.close();
			}catch(Exception e) {
				e.printStackTrace();
			}
		}
	}
}