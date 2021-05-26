import java.sql.*;
import java.util.Scanner;
import java.sql.Connection;
import java.io.InputStream;
import java.sql.PreparedStatement;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3Client;
import com.amazonaws.services.s3.model.S3Object;
import com.amazonaws.services.s3.model.GetObjectRequest;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;

public class mainUI {
	public static void main(String args[]) {
		
		String filePath = "/Users/deeppatel/Desktop/Task-3/Lookup5410.txt";
		UploadFile objUpload = new UploadFile();
		objUpload.uploadFileToS3Bucket(filePath);		
	
		AddUser objAddUser = new AddUser();
		objAddUser.addUserIntoDatabase();
		
		FindPassword objFindPassword = new FindPassword();
		objFindPassword.getPasswordFromID();
	}
}