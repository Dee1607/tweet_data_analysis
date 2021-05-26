import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3Client;
import com.amazonaws.services.s3.model.GetObjectRequest;
import com.amazonaws.services.s3.model.S3Object;

public class EncryptData {

	public static final Map<String,String> MAP_LOOKUP_TABLE = new HashMap<String,String>();
	
	public void createLookupTable() {
	

		BufferedReader reader;
		try {
			
			AmazonS3 s3Client = new AmazonS3Client(new ProfileCredentialsProvider());        
			S3Object object = s3Client.getObject(new GetObjectRequest("csci5410-a1-bucket", "Lookup5410.txt"));
			InputStream objectData = object.getObjectContent();
			
			
			
			reader = new BufferedReader(new InputStreamReader(objectData));
			String line = reader.readLine();

			// Process the objectData stream.

			int counter = 1;
			while (line != null) {
				if(counter != 1) {
					String[] arrLookupTable = line.split("	");
					
					MAP_LOOKUP_TABLE.put(arrLookupTable[0], arrLookupTable[1]);
				}
				
				// read next line
				line = reader.readLine();
				counter++;
			}
			
			objectData.close();
			
			reader.close();
	
		}catch(Exception e) {
			e.printStackTrace();
		}	
	}
	
	public String encryptPassword(String password) {
		String encryptedPassword = "";
		
		password = password.toLowerCase();
		
		for(int i = 0; i < password.length(); i++ ) {
			
			String tempReplaceValue = MAP_LOOKUP_TABLE.get(String.valueOf(password.charAt(i)));
			encryptedPassword += tempReplaceValue;
		}
		
		return encryptedPassword;

	}
}
