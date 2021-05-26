import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.AccessControlList;
import com.amazonaws.services.s3.model.AmazonS3Exception;
import com.amazonaws.services.s3.model.CanonicalGrantee;
import com.amazonaws.services.s3.model.Grant;
import com.amazonaws.services.s3.model.Permission;
import com.amazonaws.services.s3.model.PublicAccessBlockConfiguration;
import com.amazonaws.services.s3.model.SetPublicAccessBlockRequest;

public class CreateBucket {
	
	final static String BUCKET_NAME = "csci5410-a1-bucket2";
	final AmazonS3 s3Bucket = AmazonS3ClientBuilder.standard().withRegion(Regions.US_EAST_1).build();

	public void create_S3_Bucket() {
		
		if (s3Bucket.doesBucketExistV2(BUCKET_NAME)) {
		    System.out.format("Bucket %s already exists.\n", BUCKET_NAME);
		}
		else {
		    try {
		    	s3Bucket.createBucket(BUCKET_NAME);
		    	
		    	System.out.println("Bucket Created Successfully");
		    } catch (AmazonS3Exception e) {
		        System.err.println(e.getErrorMessage());
		    }
		}
	}
	
	
	public void updatePermissions() {
		
		s3Bucket.setPublicAccessBlock(new SetPublicAccessBlockRequest()
					.withBucketName(this.BUCKET_NAME)
					.withPublicAccessBlockConfiguration(new PublicAccessBlockConfiguration()
					.withBlockPublicAcls(true)
					.withIgnorePublicAcls(true)
					.withBlockPublicPolicy(true)
					.withRestrictPublicBuckets(true)));
		
        System.out.format("Permissions updated!");
	}
	
	
	public void setFullControlToUserUsingACL() {
		
		final AccessControlList acl = s3Bucket.getBucketAcl(BUCKET_NAME);
		
        acl.grantAllPermissions(new Grant(new CanonicalGrantee(acl.getOwner().getId()), Permission.FullControl));
        Grant grant1 = new Grant(new CanonicalGrantee(s3Bucket.getS3AccountOwner().getId()), Permission.FullControl);
        
        AccessControlList newBucketAcl = s3Bucket.getBucketAcl(BUCKET_NAME);
        newBucketAcl.grantAllPermissions(grant1);
        s3Bucket.setBucketAcl(BUCKET_NAME, newBucketAcl);
        System.out.format("ACL updated!");

	}
}