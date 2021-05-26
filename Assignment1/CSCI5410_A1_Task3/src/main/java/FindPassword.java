import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Scanner;

public class FindPassword {

	public void getPasswordFromID() {
		DBConnection objConnect = new DBConnection();
		Connection conn = objConnect.connectToInstance();
		Scanner sc = new Scanner(System.in);

		System.out.println("Enter userId to get password: ");
		String idToFind = sc.nextLine();
    	String foundPassword = "";

		DecryptData objDecryptData = new DecryptData();
		objDecryptData.createDecryptLookupTable();
		
		
		try {
			Statement stmt1 = conn.createStatement();
			ResultSet rs = stmt1.executeQuery("SELECT * FROM aws_testing.users");
			

		      while (rs.next())
		      {
		        String tempIdToMatch = rs.getString("userID");
		        
		        if(idToFind.equals(tempIdToMatch)) {
		        	foundPassword = rs.getString("userPassword");
		        }
		      }
		}catch(Exception e) {
			e.printStackTrace();
		}

		String decryptedPassword = objDecryptData.decryptPassword(foundPassword);
 
		System.out.println("Decrypted Password is: "+decryptedPassword);
	}
	
}
