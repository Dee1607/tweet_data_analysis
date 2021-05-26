import java.io.File;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;

public class UploadFile {
	
	public void uploadFileToS3Bucket(String filePath) {
			

		final AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion(Regions.US_EAST_1).build();
		
		String bucketName = "csci5410-a1-bucket";
		String fileName = "Lookup5410.txt";
		
		s3.putObject(bucketName,fileName,new File(filePath));
		
		System.out.println("Updated Successfully!!");
	}
}