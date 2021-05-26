import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3Client;
import com.amazonaws.services.s3.model.GetObjectRequest;
import com.amazonaws.services.s3.model.S3Object;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class DecryptData {

	public static final Map<String,String> MAP_DECRYPT_LOOKUP_TABLE = new HashMap<String,String>();

	
	public void createDecryptLookupTable() {
		
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
					
					MAP_DECRYPT_LOOKUP_TABLE.put(arrLookupTable[1], arrLookupTable[0]);
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
	
	public String decryptPassword(String password) {
		
	    String[] arrSplittedPassword = password.split("(?<=\\G..)");
	    
	    String decryptedPassword = "";
	    
	    for(int i = 0; i< arrSplittedPassword.length; i++) {
	    	decryptedPassword += MAP_DECRYPT_LOOKUP_TABLE.get(arrSplittedPassword[i]);
	    }
	    
	    return decryptedPassword;
	}
}