import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;

public class MoveFiles {
	
	private final static String BUCKET_1 = "csci5410-a1-bucket";
	private final static String BUCKET_1_FILE = "Deep.txt";

	private final static String BUCKET_2 = "csci5410-a1-bucket2";
	private final static String BUCKET_2_FILE = "Deep_Moved.txt";

	public void moveFilesBetweenBuckets() {
		try {
			final AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion(Regions.US_EAST_1).build();

			//Copy file from one bucket to another
			s3.copyObject(BUCKET_1, BUCKET_1_FILE, BUCKET_2, BUCKET_2_FILE);
			System.out.println("Copy Process Complete!");

			
			//Delete file after completion of copy process
		    s3.deleteObject(BUCKET_1, BUCKET_1_FILE);
			System.out.println("Deletion Process Complete!");

		} catch (Exception e) {
			e.printStackTrace();
		}
	System.out.println("Moving Complete!");
	}
}